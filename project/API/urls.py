from django.urls import path
from .views import EventList, SystemList

urlpatterns = [

    path('event/', EventList.as_view()),
    path('system/', SystemList.as_view()),

]