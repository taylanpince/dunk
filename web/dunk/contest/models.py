from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from contest.choices import PROVINCE_CHOICES


class ContestEntry(models.Model):
    """
    A contest entry with a unique email
    """
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    address = models.CharField(_("Address Line 1"), max_length=255)
    address_second = models.CharField(_("Address Line 2"), blank=True, max_length=255)
    city = models.CharField(_("City"), max_length=255)
    zip_code = models.CharField(_("Zip/Postal Code"), max_length=10)
    state = models.CharField(_("State/Province"), choices=PROVINCE_CHOICES, max_length=2)
    phone_number = PhoneNumberField(_("Phone Number"))
    birth_date = models.DateField(_("Birthday"))

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Contest Entry")
        verbose_name_plural = _("Contest Entries")

    def __unicode__(self):
        return u"%(first_name)s %(last_name)s (%(email)s)" % {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
