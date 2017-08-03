# # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.conf import settings
# modelos
from .models import Developer, Templates
# formularios
from .forms import DeveloperForm, TemplateForm, ContactForm

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from django.core.mail import send_mail
from django.views.generic.base import TemplateView


def DeveloperList(request):
    developer_list = Developer.objects.order_by('id')
    template = loader.get_template('developers/developer_list.html')
    context = {'developer_list': developer_list}
    return HttpResponse(template.render(context, request))


def DeveloperDetail(request, pk):
    developer = get_object_or_404(Developer, pk=pk)
    template = loader.get_template('developers/developer_detail.html')
    context = {'developer': developer}
    # if request.user.is_authenticated():
    return HttpResponse(template.render(context, request))
    # else:
    # return HttpResponseRedirect('/')


def principal(request):
    developer = Developer.objects.order_by('id')
    template_list = Templates.objects.all().order_by('id')[:3]
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_mensaje = form.cleaned_data.get('message')
        form_nombre = form.cleaned_data.get('name')
        asunto = 'formulario de contaco'
        email_from = settings.EMAIL_HOST_USER
        email_to = [form_email]
        email_mensaje = "%s: %s enviado por %s" %{form_nombre, form_mensaje, form_email}
        send_mail(asunto, email_mensaje, email_from, email_to, fail_silently = False, )
    template = loader.get_template('home.html')
    context = {'developer': developer,
                'template_list': template_list,
                'form': form,}
    return HttpResponse(template.render(context, request))


class DeveloperCreation(CreateView):
    model = Developer
    template_name = 'developers/new_developer.html'
    form_class = DeveloperForm
    success_url = reverse_lazy('developer:developer_list')

    def get_context_data(self, **kwargs):
        context = super(DeveloperCreation, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
            return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            developer = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class DeveloperUpdate(UpdateView):
    model = Developer
    template_name = 'developers/new_developer.html'
    form_class = DeveloperForm
    success_url = reverse_lazy('developer:developer_list')


class DeveloperDelete(DeleteView):
    model = Developer
    success_url = reverse_lazy('developer:developer_list')

# Clases y funciones del Modelo Template #


class TemplateCreation(CreateView):
    model = Templates
    template_name = 'template/new_template.html'
    form_class = TemplateForm
    success_url = reverse_lazy('developer:template_list')

    def get_context_data(self, **kwargs):
        context = super(TemplateCreation, self).get_context_data(**kwargs)
        if 'form2' not in context:
                context['form2'] = self.form_class(self.request.GET)
                return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form2 = self.form_class(request.POST)
        if form2.is_valid():
            template = form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form2=form2))


class TemplateUpdate(UpdateView):
    model = Templates
    template_name = 'template/new_template.html'
    form_class = TemplateForm
    success_url = reverse_lazy('developer:template_list')


class TemplateDelete(DeleteView):
    model = Templates
    success_url = reverse_lazy('developer:template_list')


def TemplateList(request):
    template_list = Templates.objects.order_by('id')
    template = loader.get_template('template/template_list.html')
    context = {
        'template_list': template_list
    }
    return HttpResponse(template.render(context, request))


def TemplateDetail(request, pk):
    template = get_object_or_404(Templates, pk=pk)
    template = loader.get_template('template/template_detail.html')
    context = {'template': template}
    return HttpResponse(template.render(context, request))


from django.core import serializers
import json


def ModalAjaxView(request):
    id_template = request.GET.get('id')
    temps = Templates.objects.filter(id=id_template)
    datos = serializers.serialize('json',temps, fields=('name', 'description', 'url', 'picture'))    

    return HttpResponse(datos, content_type='application/json')

def contact(request):
    form = ContactForm(request.POST or None)
    template = loader.get_template('contact.html')
    if form.is_valid():
        form_email =  form.cleaned_data.get("email")
        form_mensaje =  form.cleaned_data.get("message")
        form_nombre =  form.cleaned_data.get("name")
        asunto = 'ContacT.E.D.'
        email_from = settings.EMAIL_HOST_USER
        email_to = [form_email]
        email_mensaje = "%s: %s Sending successful by %s" %(form_nombre,form_mensaje,form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=True,
            )
    context = {
        "template":template,
        "form": form,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email =  form.cleaned_data.get("email")
        form_mensaje =  form.cleaned_data.get("message")
        form_nombre =  form.cleaned_data.get("name")
        asunto = 'Formulario de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [form_email]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre,form_mensaje,form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False,
            )
    context = {
        "form": form,
        "template":template,
    }
    return HttpResponse(template.render(context, request))