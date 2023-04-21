from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('edit/<task_id>', views.edit, name="edit"),
    path('delete/<task_id>', views.delete, name="delete"),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('sort_tasks_by_title_asc', views.sort_tasks_by_title_asc, name='sort_tasks_by_title_asc'),
    path('sort_tasks_by_title_desc', views.sort_tasks_by_title_desc, name='sort_tasks_by_title_desc'),
    path('sort_tasks_by_status_asc', views.sort_tasks_by_status_asc, name='sort_tasks_by_status_asc'),
    path('sort_tasks_by_status_desc', views.sort_tasks_by_status_desc, name='sort_tasks_by_status_desc'),
    path('sort_tasks_by_due_date_asc', views.sort_tasks_by_due_date_asc, name='sort_tasks_by_due_date_asc'),
    path('sort_tasks_by_due_date_desc', views.sort_tasks_by_due_date_desc, name='sort_tasks_by_due_date_desc')
]