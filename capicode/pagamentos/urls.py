from django.urls import path

from .views import ExampleView

urlpatterns = [path('pagamentos/', ExampleView.as_view()), ]
