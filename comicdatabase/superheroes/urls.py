from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('edit/<int:superhero_id>', views.edit_get, name="edit_get"),
    path('edit/', views.edit_post, name="edit_post")
]