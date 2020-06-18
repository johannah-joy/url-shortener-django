from django.urls import path

from . import views

app_name = 'url_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('submission/', views.submission, name='submission'),
  path('resulting/<str:id_short>/', views.resulting, name='resulting'),
  path('<str:short_url>/', views.redirection, name='redirection')
]