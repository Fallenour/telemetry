from rest_framework import generics

from UI.models import System, Event
from .serializers import EventSerializer, SystemSerializer


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset

class SystemList(generics.ListCreateAPIView):
    serializer_class = SystemSerializer
    queryset = System.objects.all()


# Source: https://www.youtube.com/watch?v=OJdFj5hPAKs