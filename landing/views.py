from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class Landing(TemplateView):
    template_name = "landing.html"
