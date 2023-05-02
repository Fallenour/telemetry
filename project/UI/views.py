from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# from django.http import JsonResponse12
from django.db.models import Q
from django.template import loader
from django.urls import reverse_lazy


from .models import System, Event


##################################################################################################
#                                 Django REST Framework                                          #
##################################################################################################
from rest_framework import viewsets
from .serializers import SystemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


##################################################################################################
#                                 Backend API Data Calls                                         #
##################################################################################################
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        event_count = Event.objects.all().count()
        ops_team_chart_event_count = Event.objects.all().count()*10
        ops_radar_chart_event_count = Event.objects.all().count()*10
        ops_doughut_chart_event_count = Event.objects.all().count() * 45
        ops_line_chart_event_count = Event.objects.all().count() * 35
        ops_pie_chart_event_count = Event.objects.all().count() * 15
        ops_polar_chart_event_count = Event.objects.all().count() * 15
        ops_sales_chart_event_count = Event.objects.all().count() * 15
        ops_singlebar_chart_event_count = Event.objects.all().count() * 15
        labels = ["Events", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [event_count, 23, 2, 3, 12, 2]
        ops_team_chart_labels = ["2015", "2016", "2017", "2018", "2019", "2020", "2021" ]
        ops_team_chart_default_items = [ops_team_chart_event_count, 2, 3, 12, 2, 4, 7]
        ops_radar_chart_labels = []
        ops_radar_chart_default_items = [ops_radar_chart_event_count, 59, 66, 45, 56, 55, 40 ]
        ops_doughut_chart_labels = []
        ops_doughut_chart_default_items = [ops_doughut_chart_event_count, 25, 20, 10  ]
        ops_line_chart_labels = []
        ops_line_chart_default_items = [ops_line_chart_event_count, 44, 67, 43, 76, 45, 12  ]
        ops_pie_chart_labels = []
        ops_pie_chart_default_items = [ops_pie_chart_event_count, 25, 20, 10 ]
        ops_polar_chart_labels = []
        ops_polar_chart_default_items = [ops_polar_chart_event_count, 18, 9, 6, 19]
        ops_sales_chart_labels = []
        ops_sales_chart_default_items = [ops_sales_chart_event_count, 30, 10, 120, 50, 63, 10]
        ops_singlebar_chart_labels = []
        ops_singlebar_chart_default_items = [ops_singlebar_chart_event_count, 55, 75, 81, 56, 55, 40 ]
        data = {
                "labels": labels,
                "default": default_items,
                "ops_team_chart_labels": ops_team_chart_labels,
                "ops_team_chart_default_items": ops_team_chart_default_items,
                "ops_radar_chart_labels": ops_radar_chart_labels,
                "ops_radar_chart_default_items": ops_radar_chart_default_items,
                "ops_doughut_chart_labels": ops_doughut_chart_labels,
                "ops_doughut_chart_default_items": ops_doughut_chart_default_items,
                "ops_line_chart_labels": ops_line_chart_labels,
                "ops_line_chart_default_items": ops_line_chart_default_items,
                "ops_pie_chart_labels": ops_pie_chart_labels,
                "ops_pie_chart_default_items": ops_pie_chart_default_items,
                "ops_polar_chart_labels": ops_polar_chart_labels,
                "ops_polar_chart_default_items": ops_polar_chart_default_items,
                "ops_sales_chart_labels": ops_sales_chart_labels,
                "ops_sales_chart_default_items": ops_sales_chart_default_items,
                "ops_singlebar_chart_labels": ops_singlebar_chart_labels,
                "ops_singlebar_chart_default_items": ops_singlebar_chart_default_items,
        }
        return Response(data)


class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        event_count = Event.objects.all().count()
        ops_team_chart_event_count = Event.objects.all().count()*10
        ops_radar_chart_event_count = Event.objects.all().count()*10
        ops_doughut_chart_event_count = Event.objects.all().count() * 45
        ops_line_chart_event_count = Event.objects.all().count() * 35
        ops_pie_chart_event_count = Event.objects.all().count() * 15
        ops_polar_chart_event_count = Event.objects.all().count() * 15
        ops_sales_chart_event_count = Event.objects.all().count() * 15
        ops_singlebar_chart_event_count = Event.objects.all().count() * 15
        labels = ["Events", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [event_count, 23, 2, 3, 12, 2]
        ops_team_chart_labels = ["2015", "2016", "2017", "2018", "2019", "2020", "2021" ]
        ops_team_chart_default_items = [ops_team_chart_event_count, 2, 3, 12, 2, 4, 7]
        ops_radar_chart_labels = []
        ops_radar_chart_default_items = [ops_radar_chart_event_count, 59, 66, 45, 56, 55, 40 ]
        ops_doughut_chart_labels = []
        ops_doughut_chart_default_items = [ops_doughut_chart_event_count, 25, 20, 10  ]
        ops_line_chart_labels = []
        ops_line_chart_default_items = [ops_line_chart_event_count, 44, 67, 43, 76, 45, 12  ]
        ops_pie_chart_labels = []
        ops_pie_chart_default_items = [ops_pie_chart_event_count, 25, 20, 10 ]
        ops_polar_chart_labels = []
        ops_polar_chart_default_items = [ops_polar_chart_event_count, 18, 9, 6, 19]
        ops_sales_chart_labels = []
        ops_sales_chart_default_items = [ops_sales_chart_event_count, 30, 10, 120, 50, 63, 10]
        ops_singlebar_chart_labels = []
        ops_singlebar_chart_default_items = [ops_singlebar_chart_event_count, 55, 75, 81, 56, 55, 40 ]
        data = {
                "labels": labels,
                "default": default_items,
                "ops_team_chart_labels": ops_team_chart_labels,
                "ops_team_chart_default_items": ops_team_chart_default_items,
                "ops_radar_chart_labels": ops_radar_chart_labels,
                "ops_radar_chart_default_items": ops_radar_chart_default_items,
                "ops_doughut_chart_labels": ops_doughut_chart_labels,
                "ops_doughut_chart_default_items": ops_doughut_chart_default_items,
                "ops_line_chart_labels": ops_line_chart_labels,
                "ops_line_chart_default_items": ops_line_chart_default_items,
                "ops_pie_chart_labels": ops_pie_chart_labels,
                "ops_pie_chart_default_items": ops_pie_chart_default_items,
                "ops_polar_chart_labels": ops_polar_chart_labels,
                "ops_polar_chart_default_items": ops_polar_chart_default_items,
                "ops_sales_chart_labels": ops_sales_chart_labels,
                "ops_sales_chart_default_items": ops_sales_chart_default_items,
                "ops_singlebar_chart_labels": ops_singlebar_chart_labels,
                "ops_singlebar_chart_default_items": ops_singlebar_chart_default_items,
        }
        return Response(data)


##################################################################################################
#                                      UI Views                                            #
##################################################################################################
class IndexView(TemplateView):
    template_name = 'ui/Focus/templates/ui/Focus/base.html'
    #    model = Products
    #    paginate_by = 50
    #    permissions_required = ('polls.view_choice', 'polls.change_choice')

class PrimaryView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/overview.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

##################################################################################################
#                                  UI Data Functions                                       #
##################################################################################################
class UIAPIView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = SystemSerializer


def docops(request):
#    if not request.user.is_authenticate:
#        return render(request, 'ui/Focus/login.html')
#    else:
        events = Event.objects.all()
        return render(request, 'ui/Focus/docops.html', {
            'event_list': events,
        }) #, context)

def ops(request):
#    if not request.user.is_authenticate:
#        return render(request, 'ui/Focus/login.html')
#    else:
        events = Event.objects.all()
        return render(request, 'ui/Focus/ops.html', {
            'event_list': events,
        }) #, context)

def mgmtops(request):
#    if not request.user.is_authenticate:
#        return render(request, 'ui/Focus/login.html')
#    else:
        events = Event.objects.all()
        return render(request, 'ui/Focus/mgmtops.html', {
            'event_list': events,
        }) #, context)


def events(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'ui/Focus/login.html')
    else:
        try:
            event_ids = []
            for System in System.objects.filter(event=request.event):
                for event in system.event_set.all():
                    event_ids.append(event.pk)
            system_events = Event.objects.filter(pk__in=event_ids)
            if filter_by == 'processed':
                system_events = system_events.filter(is_processed=True)
        except System.DoesNotExist:
            system_events = []
        return render(request, 'ui/Focus/galaxyops.html', {
            'event_list': system_events,
            'filter_by': filter_by,
        })

def celery(request):
    if not request.user.is_authenticated():
        return render(request, 'ui/Focus/login.html')
    else:
        return render(request, 'ui/Focus/base.html') #, context)

def celeryfeedback(request):
    if not request.user.is_authenticated():
       return render(request, 'ui/Focus/login.html')
    else:
        return render(request, 'ui/Focus/base.html') #, context)