from django.shortcuts import render
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.



class IndexView(View):
    context_object_name = 'index'
    template_name = 'index.html'
    def get(self, request):
        return render(request,self.template_name)




