from django.urls import path
from .views import introduction, water

app_name = 'water'

urlpatterns = [
    path('', introduction, name='introduction'),
    #path('<int:introduction_pk/>', water, name='water'),
    path('introduction/<int:pk>', water, name='water')

]