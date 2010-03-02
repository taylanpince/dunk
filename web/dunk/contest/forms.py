from datetime import date

from django import forms
from django.contrib.localflavor.us.forms import USStateSelect
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

from contest.models import ContestEntry


class ContestEntryForm(forms.ModelForm):
    """
    A contest entry form, generated from ContestEntry model
    """
    def __init__(self, *args, **kwargs):
        super(ContestEntryForm, self).__init__(*args, **kwargs)

        now = date.today()
        years = range(now.year - 100, now.year - 18)
        years.reverse()

        self.fields["birth_date"].widget = SelectDateWidget(years=years)
        self.fields["state"].widget = USStateSelect()

    class Meta:
        model = ContestEntry
        exclude = ("timestamp",)
