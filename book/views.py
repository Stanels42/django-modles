from django.views.generic import TemplateView, ListView, DetailView

from .models import Data

# Create your views here.
class HomeView(TemplateView):
  template_name = 'home.html'

class BookListView(ListView):
  template_name = 'list_view.html'
  model = Data

class BookDetailView(DetailView):
  template_name = 'detail_view.html'
  model = Data
  context_object_name = 'book'
