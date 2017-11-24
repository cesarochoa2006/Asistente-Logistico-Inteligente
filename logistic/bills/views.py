from django.conf.global_settings import MEDIA_ROOT
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import File
from . import clasify as cla
import os

# Create your views here.

class IndexView(ListView):
    context_object_name = 'Files'
    template_name = 'bills/index.html'
    queryset = File.objects.all()
    file_path = os.path.join(MEDIA_ROOT,'DATOS.xlsx') or None


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['file_list'] = File.objects.all()
        context['count_rows'] = File.objects.count()
        context['clasification_table']=cla.data_clasification(self.file_path)
        context['content_table']=cla.list_of_list(self.file_path)
        context['table_header'] = cla.table_head(self.file_path)

            #context['content_table'] = None
            #context['table_header'] = None
        return context

#File Uploading

class UploadFile(CreateView):
    model = File
    template_name = 'bills/upload-file.html'
    fields=['file_file','thumbnail']
    success_url = reverse_lazy('bills:index')
#File Delete
class FileDelete(DeleteView):
    redirect_field_name = 'redirect_to'
    model = File
    success_url = reverse_lazy('bills:index')

class UpdateFile(UpdateView):
    redirect_file_name='redirect_to'
    model=File
    success_url = reverse_lazy('bills:index')
    fields=['file_file','thumbnail']
    template_name = 'bills/upload-file.html'

    # def form_valid(self, form):
    #     object = form.save(commit=False)
    #     object.user = self.request.user
    #     object.save()
    #     return super(UpdateFile, self).form_valid(form)