from django.conf import settings
from django.views.generic import TemplateView
from django.urls import path, include
from UI import views
from UI.views import IndexView, TemplateView




###Django Framework

from rest_framework import routers


router = routers.DefaultRouter()
router.register('UI', views.UIAPIView)

### Chart Data ###

from .views import ChartData
from .views import ChartData2

urlpatterns = [

    # API Call for Chart View for ChartData
    path('api/chart/data/', ChartData.as_view()),

    # API Call for Chart View for Overview Dashboard
    path('api/chart/data2/', ChartData2.as_view()),

    # /ui/

    # Indexes
    path('', TemplateView.as_view(template_name='ui/Focus/base.html'), name='index1'),  # this one is OK with '' it means end of the string

    # Dashboards
    path('ops/', views.ops, name='ops'),

    # Tables
    path('ui-tables-basic/', TemplateView.as_view(template_name='ui/Focus/table-basic.html'), name='tablebasic'),
    path('ui-tables-datatableexport/', TemplateView.as_view(template_name='ui/Focus/table-export.html'), name='tableexport'),
    path('ui-tables-datatablerowselect/', TemplateView.as_view(template_name='ui/Focus/table-row-select.html'), name='tablerow'),
    path('ui-tables-datatablejsgrid/', TemplateView.as_view(template_name='ui/Focus/table-jsgrid.html'), name='tablejsgrid'),

    # Django Rest Framework API path
    path('api/', include(router.urls)),

    # Misc
    path('profile/', TemplateView.as_view(template_name='ui/Focus/app-profile.html'), name='appprofile'),
    path('widgets/', TemplateView.as_view(template_name='ui/Focus/app-widget-card.html'), name='appwidget'),

    # Celery Testing
#   path('cel/', PhotoView.as_view(), name="celeryhome"),
#   path('feedback/', FeedbackView.as_view(), name="celeryfeedback"),
]