from django.conf.urls import url
from blblogger.views import BlogCreateView

from . import views

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserRegisterView.as_view(), name='register'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^$', views.CreateUser.as_view(), name='create-blog'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]