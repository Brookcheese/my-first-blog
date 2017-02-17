from django.conf.urls import include, url
from . import views

urlpartterns =[
 url(r'ˆ$', views.post_list),

]
