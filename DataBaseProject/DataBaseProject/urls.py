"""
Definition of urls for DataBaseProject.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DataBaseProject.views.home, name='home'),
    # url(r'^DataBaseProject/', include('DataBaseProject.DataBaseProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mascota/', include('apps.mascota.urls', namespace="mascota")),
    url(r'^adopcion/', include('apps.adopcion.urls', namespace="adopcion")),
]
