from django.urls import path
from todo_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add_task,name='addtask'),
]