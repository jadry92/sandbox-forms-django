# Django
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
# Forms
from basic_forms.forms import FileForm
# Model
from basic_forms.models import File


class FileView(FormView):
    template_name = 'basic_forms/files.html'
    form_class = FileForm
    success_url = reverse_lazy('basic_home_files')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super(FileView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """adding List"""
        new_kwargs = super(FileView, self).get_context_data(**kwargs)
        new_kwargs['files'] = File.objects.all()
        return new_kwargs


class HomeView(TemplateView):
    template_name = 'basic_forms/home.html'
