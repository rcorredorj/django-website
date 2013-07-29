from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main_application.views.home', name='home'),
    # url(r'^main_application/', include('main_application.foo.urls')),
	url(r'^$','main_application.views.home'),
	url(r'^home/$','main_application.views.home'),
    url(r'^private/about/$','main_application.views.about'),
    url(r'^private/contact/$','main_application.views.contact'),
    url(r'^private/$','main_application.views.private'),
    url(r'^private/article$','main_application.views.new_article'),
	url(r'^private/article/(?P<id_article>\d+)$','main_application.views.detail_article'),
    url(r'^log_out/$', 'main_application.views.log_out'),

    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
