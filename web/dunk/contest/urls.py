from django.conf.urls.defaults import *


urlpatterns = patterns('contest.views',
    url(r"^$", "entry", name="contest_entry"),
    url(r"^rules/$", "rules", name="contest_rules"),
)

urlpatterns += patterns('',
    url(r"^done/$", "django.views.generic.simple.direct_to_template", {
        "template": "contest/entry_done.html",
    }, name="contest_entry_done"),
)
