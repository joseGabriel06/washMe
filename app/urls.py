from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from material.frontend import urls as frontend_urls
from registration.backends.default.views import RegistrationView
from django.contrib.auth import views as auth_views

from apps.homepage.views import (
    HomeView,
    create_service,
    ServiceListView,
 )

from apps.washer.views import (
     HomeDoneView,
    NewWasherView,
 )

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^washer/', NewWasherView.as_view(), name="new_washer"),
    url(r'^done/', HomeDoneView.as_view(), name="done"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^agendar', ServiceListView.as_view(), name='pay'),
    url(r'^service/create', create_service, name='newservice'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administración de WashMe'
