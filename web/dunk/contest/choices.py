from django.contrib.localflavor.ca.ca_provinces import PROVINCE_CHOICES as CANADIAN_PROVINCES
from django.contrib.localflavor.us.us_states import STATE_CHOICES as US_STATES
from django.utils.translation import ugettext_lazy as _


PROVINCE_CHOICES = (
    (_("Canada"), CANADIAN_PROVINCES),
    (_("United States"), US_STATES),
)
