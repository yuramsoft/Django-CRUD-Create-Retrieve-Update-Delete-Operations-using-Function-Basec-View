from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('<int:id>', views.view_info, name='view_info'),
path('update/<int:id>/', views.update_view, name='update'),
path('delete/<int:id>/', views.delete, name='delete'),
path('add/', views.add_form, name='add'),

]