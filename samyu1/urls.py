from django.contrib import admin
from django.urls import path
from samyuapp import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^samyu$', views.home),
    url(r'regi', views.regi),
    url(r'login', views.login),
    url(r'sanjeev', views.sanjeev),
    url(r'saroja', views.saroja),
    url(r'input',views.input),
    url(r'grand',views.grand),
    url(r'gra1',views.gra1),
    url(r'parent',views.parent),
    url(r'praveen', views.praveen),
    url(r'sibling',views.sibling),
    url(r'naveen', views.naveen),
    url(r'nick',views.nick),
    url(r'apple',views.apple),
    url(r'edu',views.edu),
    url(r'psn',views.psn),
]
