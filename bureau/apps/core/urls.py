from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    path('kitchensink', TemplateView.as_view(template_name='core/kitchensink.html'), name='kitchensink'),
]
