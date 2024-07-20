from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    def get(self,request):
        return render(request, template_name='website/home.html')