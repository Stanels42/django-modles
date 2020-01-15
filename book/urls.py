from django.urls import path
from .views import HomeView, BookListView, BookDetailView

urlpatterns = [
  path('', HomeView.as_view(), name = 'home'),
  path('list/', BookListView.as_view(), name = 'list'),
  path('detail/<int:pk>/', BookDetailView.as_view(), name = 'detail'),
]
