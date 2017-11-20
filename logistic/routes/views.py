from django.shortcuts import render
from django.views.generic import ListView,View

# Create your views here.
"""class IndexView(ListView):
    context_object_name = 'index'
    template_name = 'index.html'
"""
class IndexView(View):
    context_object_name = 'index'
    template_name = 'index.html'
    def get(self, request):
        return render(request,self.template_name)