import os
import sys
import site

site.addsitedir('/home/taylan/sites/dunk/lib/python2.5/site-packages')

sys.path.append("/home/taylan/sites/dunk/src")
sys.path.append("/home/taylan/sites/dunk/src/dunk")

os.environ["DJANGO_SETTINGS_MODULE"] = "dunk.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
