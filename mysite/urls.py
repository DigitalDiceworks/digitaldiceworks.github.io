from django.urls import path
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView
from mysite import views

urlpatterns = [
    # path('favicon.ico', RedirectView.as_view(
    #         url=staticfiles_storage.url('favicon.ico'),
    #         permanent=False
    #     ),
    #     name='favicon'),
    # path('browserconfig.xml', RedirectView.as_view(
    #         url=staticfiles_storage.url('browserconfig.xml'),
    #         permanent=False
    #     ),
    #     name='broswerconfig'),
    path('', views.HomeView.as_view(), name='home'),
]
