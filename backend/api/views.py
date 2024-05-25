from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.response import Response


from .custom_permissions import *

from .serializers import *

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsUser]

    def update(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])

        if request.data.get('password'):
            user.set_password(request.data['password'])

        if request.data.get('email'):
            user.email = request.data['email']

        if request.data.get('first_name'):
            user.first_name = request.data['first_name']

        if request.data.get('last_name'):
            user.last_name = request.data['last_name']

        user.save()

        return Response({
            'pk': user.pk,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        queryset = Location.objects.all()
        params = request.GET
        if params.get('name'):
            queryset = queryset.filter(name__contains=params['name'])

        if params.get('zip'):
            queryset = queryset.filter(zip__contains=params['zip'])

        data = LocationSerializer(
            queryset,
            many=True,
            context={'request': request}
        ).data

        return Response(
            data,
            status=status.HTTP_200_OK
        )


# noinspection DuplicatedCode
class LocationCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    queryset = LocationComment.objects.all()
    serializer_class = LocationCommentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save(
            userId=self.request.user,
            comment=self.request.data['comment'],
            location=Location.objects.get(id=self.request.data['location'])
        )

    def update(self, request, *args, **kwargs):
        comment = LocationComment.objects.get(id=self.request.data['id'])

        # check if location is the same
        if comment.location.id != self.request.data['location']:
            return Response(
                {'detail': 'can\'t transfer comment to other place'},
                status=status.HTTP_400_BAD_REQUEST
            )

        comment.comment = self.request.data['comment']
        comment.save(args, kwargs)
        return Response(
            {
                'id': comment.id,
                'comment': comment.comment,
                'user': comment.user,
                'location': comment.location_id
            },
            status=status.HTTP_200_OK
        )

    def list(self, request, *args, **kwargs):
        queryset = LocationComment.objects.all()
        params = request.GET

        if params.get('lid'):
            queryset = queryset.filter(location_id=params['lid'])

        # filter by users
        if params.get('user'):
            try:
                users = User.objects.filter(username__contains=params['user'])
                queryset = queryset.filter(userId__in=users)
            except ObjectDoesNotExist:
                pass

        data = LocationCommentSerializer(
            queryset,
            many=True,
            context={'request': request}
        ).data

        return Response(
            data,
            status=status.HTTP_200_OK
        )


class LocationRatingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    queryset = LocationRating.objects.all()
    serializer_class = LocationRatingSerializer
    http_method_names = ['get', 'post', 'put']

    def create(self, request, *args, **kwargs):
        # check if user has already rated this location
        rating = LocationRating.objects.filter(
            userId=request.user,
            location=request.data['location']
        )

        if rating:
            return Response(
                {'detail': 'user has already rated this location'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check if rating is between 1 and 5
        decimal_rating = float(request.data['rating'])
        if decimal_rating < 1 or decimal_rating > 5:
            return Response(
                {'detail': 'rating must be between 1 and 5'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        serializer.save(
            userId=self.request.user,
            rating=self.request.data['rating'],
            location=Location.objects.get(id=self.request.data['location'])
        )

    def update(self, request, *args, **kwargs):
        rating = LocationRating.objects.get(id=kwargs['pk'])

        # check if rating is for the same location
        if rating.location.id != int(request.data['location']):
            return Response(
                {'detail': 'can\'t transfer rating to other place'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check if rating is between 1 and 5
        decimal_rating = float(request.data['rating'])
        if decimal_rating < 1 or decimal_rating > 5:
            return Response(
                {'detail': 'rating must be between 1 and 5'},
                status=status.HTTP_400_BAD_REQUEST
            )

        rating.rating = request.data['rating']
        rating.save(args, kwargs)
        return Response(
            {
                'id': rating.id,
                'rating': rating.rating,
                'user': rating.user,
                'location': rating.location_id
            },
            status=status.HTTP_200_OK
        )

    def list(self, request, *args, **kwargs):
        # filter ratings by user if user is not admin
        if request.user.is_superuser:
            queryset = LocationRating.objects.all()
        else:
            try:
                user = User.objects.get(id=request.user.id)
                queryset = LocationRating.objects.filter(userId=user)
            except ObjectDoesNotExist:
                queryset = LocationRating.objects.none()

        params = request.GET

        if params.get('lid'):
            queryset = queryset.filter(location_id=params['lid'])

        data = LocationRatingSerializer(
            queryset,
            many=True,
            context={'request': request}
        ).data

        return Response(
            data,
            status=status.HTTP_200_OK
        )


# noinspection DuplicatedCode
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'put']

    def create(self, request, *args, **kwargs):
        date = datetime.strptime(request.data['date'], '%Y-%m-%d')
        now = datetime.now()

        if date < now:
            return Response(
                {'detail': 'event date must be in the future'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        serializer.save(
            name=self.request.data['name'],
            description=self.request.data['description'],
            lan=self.request.data['lan'],
            userId=self.request.user,
            location=Location.objects.get(id=self.request.data['location']),
            date=self.request.data['date'],
            capacity=self.request.data['capacity']
        )

    def update(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs['pk'])
        date = datetime.combine(event.date, datetime.min.time())
        now = datetime.now()

        if date < now:
            return Response(
                {'detail': 'can\'t modify past events'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if event.location.id != int(request.data['location']):
            return Response(
                {'detail': 'can\'t transfer event to other place'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.data.get('capacity'):
            if int(request.data['capacity']) < 0:
                return Response(
                    {'detail': 'capacity must be positive'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if int(request.data['capacity']) < event.current_capacity:
                return Response(
                    {'detail': 'capacity must be greater than current number of participants'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        event.name = request.data['name']
        event.description = request.data['description']
        event.date = request.data['date']
        event.capacity = request.data['capacity']

        if request.data.get('lan'):
            if type(request.data['lan']) is not bool:
                event.lan = request.data['lan'].capitalize()
            else:
                event.lan = request.data['lan']

        event.save(args, kwargs)
        return Response(
            {
                'id': event.id,
                'name': event.name,
                'description': event.description,
                'lan': event.lan,
                'user': event.user,
                'location': event.location_id,
                'date': event.date,
                'capacity': event.capacity,
                'current_capacity': event.current_capacity
            },
            status=status.HTTP_200_OK
        )

    def list(self, request, *args, **kwargs):
        queryset = Event.objects.all()
        params = request.GET

        if params.get('name'):
            queryset = queryset.filter(name__contains=params['name'])

        if params.get('lan'):
            queryset = queryset.filter(lan=params['lan'].capitalize())

        # check if user exists and filter by user
        if params.get('user'):
            try:
                user = User.objects.get(username__exact=params['user'])
                queryset = queryset.filter(userId=user)
            except ObjectDoesNotExist:
                pass

        if params.get('lid'):
            queryset = queryset.filter(location_id=params['lid'])

        data = EventSerializer(
            queryset,
            many=True,
            context={'request': request}
        ).data

        return Response(
            data,
            status=status.HTTP_200_OK
        )


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        event = Event.objects.get(id=request.data['event'])

        # check if event is full
        if event.current_capacity >= event.capacity:
            return Response(
                {'detail': 'event is full'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check if user is already registered to this event
        registration = EventRegistration.objects.filter(
            userId=request.user,
            event=request.data['event']
        )

        if registration:
            return Response(
                {'detail': 'user has already registered to this event'},
                status=status.HTTP_400_BAD_REQUEST
            )

        date = datetime.combine(event.date, datetime.min.time())
        now = datetime.now()

        if date < now:
            return Response(
                {'detail': 'can\'t register to past event'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        serializer.save(
            userId=self.request.user,
            event=Event.objects.get(id=self.request.data['event'])
        )

    def list(self, request, *args, **kwargs):
        # return empty list if user is not authenticated
        if not request.user.is_authenticated:
            return Response(
                [],
                status=status.HTTP_200_OK
            )

        queryset = EventRegistration.objects.all()
        params = request.GET

        # return only registrations of events created by user and registrations of user
        # admin can see all registrations
        if not request.user.is_superuser:
            queryset = queryset.filter(Q(event__userId=request.user) | Q(userId=request.user))

        # filter by event id
        if params.get('eid'):
            queryset = queryset.filter(event_id=params['eid'])

        # filter by username
        if params.get('user'):
            queryset = queryset.filter(userId__username__exact=params['user'])

        data = EventRegistrationSerializer(
            queryset,
            many=True,
            context={'request': request}
        ).data

        return Response(
            data,
            status=status.HTTP_200_OK
        )
