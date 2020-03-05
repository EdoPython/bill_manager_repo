from django.conf.urls import url
from . import views


# SET THE NAMESPACE
app_name = 'bills'


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^general/$', views.general, name='general'),
    url(r'^add_bill/$', views.add_bill, name='add_bill'),
    url(r'^add_bill/([0-9]+)/$', views.edit_bill, name='edit_bill'),
    url(r'^delete_bill/([0-9]+)/$', views.delete_bill, name='delete_bill'),
]
