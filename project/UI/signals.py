from django.db.models.signals import post_save
from .models import Event
from django.dispatch import receiver
from django.http import JsonResponse


@receiver(post_save, sender=Event)
def pre_delete_event(sender, **kwargs):

    if Event.component == "TSTAT":
        if Event.rawvalue >= 20:
            return JsonResponse(event.json())
    if Event.component == "BATT":
        if Event.rawvalue >=85:
            return JsonResponse(event.json())
    #print("You are about to delete something!")