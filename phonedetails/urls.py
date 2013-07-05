from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'phonedetails.views.home', name='home'),
    # url(r'^phonedetails/', include('phonedetails.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/$', 'phonebook.views.contacts'),  
    url(r'^contact_add/$', 'phonebook.views.contact_add'),
    url(r'^contact_edit/(?P<contact_id>\d+)/$',
    'phonebook.views.contact_edit'),
    url(r'^contact_delete/(?P<contact_id>\d+)/$',
    'phonebook.views.contact_delete'),
)
