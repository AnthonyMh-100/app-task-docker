from django.urls import path
from . import views

app_name = 'Task'
urlpatterns = [
    path('',views.view_login,name="login_task"),
    path('register/',views.view_register,name="register_task"),
    path('logout/',views.view_logout,name="logout_task"),
    path('home/',views.view_home,name="home_task"),
    path('home/dashboard',views.view_index,name="view_index"),
    path('home/new/task',views.view_form,name="new_task"),
    path('home/task/<int:task_id>',views.one_task,name="one_task"),
    path('home/change/doing/<int:task_id>',views.change_doing,name="change_doing"),
    path('home/change/done/<int:task_id>',views.change_done,name="change_done"),
    path('home/delete/task/<int:task_id>',views.delete_task,name="delete_task"),

]

