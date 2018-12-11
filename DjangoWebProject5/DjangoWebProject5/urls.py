"""
Definition of urls for DjangoWebProject5.
"""

from django.conf.urls import include, url
from home.views import home_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebProject5.views.home, name='home'),
    # url(r'^DjangoWebProject5/', include('DjangoWebProject5.DjangoWebProject5.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^$',home_view, name='home'),
      url(r'^post/', include('post.urls')),
      url(r'^accounts/', include('accounts.urls')),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)