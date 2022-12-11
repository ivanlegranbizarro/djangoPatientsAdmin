from django.db.models import Q
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Patient
from .forms import PatientForm
from django.contrib.messages.views import SuccessMessageMixin


class FrontEnd(generic.TemplateView):
    template_name = 'index.html'


class CreatePatient(LoginRequiredMixin, generic.CreateView):
    model = Patient
    template_name = 'create_patient.html'
    form_class = PatientForm
    success_url = 'backend'


class DetailPatient(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Patient
    template_name = 'detail_patient.html'
    form_class = PatientForm
    login_url = 'login'
    success_message = 'Patient updated successfully'


def delete_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.delete()
    return redirect('patients:backend')


# Backend Section


class Login(generic.TemplateView):
    template_name = 'registration/login.html'


class Backend(LoginRequiredMixin, generic.ListView):
    login_url = 'patients:login'
    template_name = 'backend.html'
    context_object_name = 'patients'

    def get_queryset(self):
        if self.request.GET.get('q'):
            search_term = self.request.GET.get('q')
            return Patient.objects.filter(
                Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term) | Q(
                    age__icontains=search_term) | Q(gender__icontains=search_term))
        else:
            return Patient.objects.all()
