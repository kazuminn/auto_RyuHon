from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tosyokan.views.home', name='home'),
    # url(r'^tosyokan/', include('tosyokan.foo.urls')),
    (r'^register/$', 'login.views.register'),
    (r'^home/', 'home.views.home'),
    (r'^rule/$', 'home.views.rule'),
    (r'^deletion/$', 'login.views.delete'),
    (r'^deletion/delete$', 'login.views.deletion'),
    (r'^accounts/login/?next=/register/create_user/$', 'login.views.register'),
    (r'^accounts/login/?next=/delete/deletion/$', 'login.views.delete'),
    (r'^register/create_user/create_user/$', 'login.views.create_user'),
    (r'^register/create_user/$', 'login.views.create_user'),

    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
