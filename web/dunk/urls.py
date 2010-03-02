from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin
    (r'^admin/', include(admin.site.urls)),
    
    # Contest
    (r'^contest/', include('contest.urls')),
    
    # Home
    url(r"^$", "django.views.generic.simple.direct_to_template", {
        "template": "home.html",
    }, name="home"),
)
