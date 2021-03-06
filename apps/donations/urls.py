from django.urls import path

from apps.donations.views import SingleDonationView, ContactMailView
from . import views
from .views import ArchiveDonation

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='index'),
    path('add_donation/', views.AddDonationView.as_view(), name='add-donation'),
    path('archive_donation/<int:donation_id>/', ArchiveDonation.as_view(), name='archive_donation'),
    path('donation/<int:pk>/', SingleDonationView.as_view(), name='donation'),
    path('contact_mail/sent/', ContactMailView.as_view(), name='contact_mail'),
]
