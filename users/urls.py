from django.urls import path
from .api.views import UsersListView, UserAddView
# from django.urls import re_path as url, include

urlpatterns = [
    path('', UsersListView.as_view(), name='home'),
    path('new/', UserAddView.as_view(), name='new' ),
    # path('home/', views.home, name='home'),
    # path('new/', CreateNote.as_view(), name='create'),
    # path('', ListNote.as_view(), name='list'),
    # path('notes/<int:pk>', RetrieveNote.as_view(), name='note'),
    # path('edit/<int:pk>', UpdateNote.as_view(), name='edit'),
    # path('delete/<int:pk>', DeleteNote.as_view(), name='delete'),
]
app_name = 'users'