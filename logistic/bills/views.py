from django.shortcuts import render
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import File
from .forms import FileForm
from django.http import HttpResponseRedirect



# Create your views here.


"""
class IndexView(View):
    context_object_name = 'index'
    template_name = 'index.html'
    def get(self, request):
        return render(request,self.template_name)
"""

class IndexView(ListView):
    context_object_name = 'Files'
    template_name = 'index.html'
    queryset = File.objects.all()
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['file_list'] = File.objects.order_by('file_name')
        #context['venue_list'] = Venue.objects.all()
        #context['festival_list'] = Festival.objects.all()
        # And so on for more models
        return context

#File Uploading
"""
def createFile(request):
    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        file=form.save(commit=False)
        file.save()
        context = {
            "form": form,
        }
        return render(request,'bills:index',context)
"""
#@method_decorator(user_passes_test(lambda u: u.is_admin), name='dispatch')
class createFile(CreateView):
    model = File
    #form_class = FileForm
    template_name = 'create-file.html'
    fields=['file_name','file_file']
    success_url = reverse_lazy('bills:index')

