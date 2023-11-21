from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PotfolioPageView(TemplateView):
    template_name = 'potfolio.html'


class ConnectionPageView(TemplateView):
    template_name = 'connection.html'

# Create your views here.
