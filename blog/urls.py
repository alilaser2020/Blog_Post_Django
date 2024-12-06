from django.urls import path
from .views import (HomeView, NewPostView, DetailPostView,
                    UpdatePostView, DeletePostView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', NewPostView.as_view(), name='new_post'),
    path('post/<int:pk>', DetailPostView.as_view(), name='detail_post'),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]
