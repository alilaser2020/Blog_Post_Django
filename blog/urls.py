from django.urls import path
from .views import HomeView, NewPostView, DetailPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', NewPostView.as_view(), name='new_post'),
    path('post/<int:pk>', DetailPostView.as_view(), name='detail_post'),
]
