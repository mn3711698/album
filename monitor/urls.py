
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^repost/', views.repost),
    url(r'^indexs/', views.monitor),
    url(r'^monitors/', views.monitorlist),
]
