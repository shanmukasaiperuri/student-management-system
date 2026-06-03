from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.result_list,
        name='result_list'
    ),

    path(
        'add/',
        views.add_result,
        name='add_result'
    ),

    path(
        'update/<int:pk>/',
        views.update_result,
        name='update_result'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_result,
        name='delete_result'
    ),
]