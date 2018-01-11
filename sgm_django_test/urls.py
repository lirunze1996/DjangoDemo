from django.conf.urls import patterns, include, url
from tastypie.api import Api
from webservice.testResource import MyTestResource
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(MyTestResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls))
    # Examples:
    # url(r'^$', 'sgm_django_test.views.home', name='home'),
    # url(r'^sgm_django_test/', include('sgm_django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
