from django.conf.urls.defaults import *
from leikur.views import *


urlpatterns = patterns('',
    # Example:
    (r'^$', index),
    (r'^(?P<question>\d+)/(?P<answer>\w+)$', check_answer, {}),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
