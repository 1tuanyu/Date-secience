from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^log_in/',views.Log_in,name="log_in"),
]
