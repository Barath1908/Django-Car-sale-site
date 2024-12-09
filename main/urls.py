from django.urls import path
from .views import *

urlpatterns = [
  path('', main_view, name='main'),
  path('home/', home_view, name='home'),
  path('list/', list_view, name='list'),
  path('listing/<str:id>/', listing_view, name='listing'),
  path('listing/<str:id>/edit/', edit_view, name='edit'),
  path('listing/<str:id>/like/', like_listing_view, name='like_listing'),

]