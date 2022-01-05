""" Basic Forms

"""
# Django
from django.urls import path
# View
from basic_forms.views import FileView, HomeView

urlpatterns = [
    path('', view=HomeView.as_view(), name='basic_home'),
    path('files/', view=FileView.as_view(), name='basic_home_files'),
]
