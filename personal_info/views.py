from __future__ import unicode_literals

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import PersonalInfo
from .forms import PersonalInfoForm


# Create your views here.

class PersonalInfoList(ListView):
    model = PersonalInfo
    template_name = 'personal_info/personal_info_list.html'


class PersonalInfoCreate(CreateView):
    form_class = PersonalInfoForm
    template_name = 'personal_info/personal_info_form.html'
    success_url = reverse_lazy('personal_info_list')


class PersonalInfoUpdate(UpdateView):
    model = PersonalInfo
    form_class = PersonalInfoForm
    success_url = reverse_lazy('personal_info_list')
    template_name = 'personal_info/personal_info_form.html'


class PersonalInfoDelete(DeleteView):
    model = PersonalInfo
    success_url = reverse_lazy('personal_info_list')
    template_name = 'personal_info/personal_info_delete.html'
