from django.conf.urls import patterns, include, url
from django.contrib import admin
import grappelli

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheRentalSpot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
