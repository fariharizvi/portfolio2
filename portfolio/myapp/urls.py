from django.urls import path
from . import views

urlpatterns = [
    path('homepage/<int:id>', views.homepage), #http://127.0.0.1:8000/homepage/1
    path('aboutus', views.aboutUs), #http://127.0.0.1:8000/aboutus
    path('studentform', views.student_form, name='student_form'), #http://127.0.0.1:8000/studentform
    path('', views.index, name='index'),
    path('apply/', views.student_form, name='student_form'),
    path('success/', views.success, name='success'),
    path('students/', views.student_list, name='student_list'),
]

