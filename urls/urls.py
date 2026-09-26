from django.urls import path
from .views import URLListCreateView,URLDetailView,URlRedirectView

urlpatterns = [
    path('urls/',URLListCreateView.as_view(),name = 'url-list-create'),
    path('urls/<int:pk>/',URLDetailView.as_view(), name = 'url-detail'),
]