from django.urls import path
from .api.views import AddPost, ListPost, RetrieveUpdatePost
# from django.urls import re_path as url, include

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('new/', AddPost.as_view(), name='create'),
    path('', ListPost.as_view(), name='list'),
    path('<int:pk>', RetrieveUpdatePost.as_view(), name='post'),
    # path('edit/<int:pk>', UpdateNote.as_view(), name='edit'),
    # path('delete/<int:pk>', DeleteNote.as_view(), name='delete'),
]
app_name = 'posts'
