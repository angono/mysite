from django.urls import path
from .views import * #import all functions from views

urlpatterns = [
    path('', post_list_view, name='post_list'), #To display all information
    path('detail/<str:ids>/', post_detail_view, name='post_detail'), #Display details
]




