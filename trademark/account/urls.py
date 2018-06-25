from django.conf.urls import url

from . import views

app_name = 'account'
urlpatterns = [
    url(r'^log/',views.Log_in,name="log_in"),
]
