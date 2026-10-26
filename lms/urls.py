from django.urls import path
from . import views
app_name='lms'
urlpatterns=[path('submissions/',views.my_submissions,name='submissions')]
