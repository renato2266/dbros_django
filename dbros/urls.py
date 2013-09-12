from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^dbros/', 'dbrosbs.dbros.views.home'),
    #url(r'^dbros/', include('dbros.foo.urls')),
	(r'^helloworld/$', 'dbrosbs.views.hello_world'),
	(r'^soggetto/(\d+)/$', 'dbrosbs.views.scheda_soggetto'),
	(r'^index/$', "dbrosbs.views.index"),
	
	

	
	
    

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
