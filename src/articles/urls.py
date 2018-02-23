from django.urls import include, path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<slug>/edit/', views.article_edit, name='edit'),
    path('<slug>/', views.article_details, name='details'),
    #path('<slug>/delete/', views.article_delete, name='create'),
]
