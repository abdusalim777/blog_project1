from django.urls import path
from .views import HomePageView, AboutPageView, PotfolioPageView, ConnectionPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('portfolio/', PotfolioPageView.as_view(), name='potfolio'),
    path('connection/', ConnectionPageView.as_view(), name='connection')
]
