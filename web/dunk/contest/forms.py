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
    email_confirm = forms.EmailField(label=_("Email Confirm"))

    def clean_email(self):
        if self.cleaned_data.get("email", None):
            try:
                ContestEntry.objects.get(email__iexact=self.cleaned_data.get("email"))
            except ContestEntry.DoesNotExist:
                return self.cleaned_data.get("email")

            raise forms.ValidationError(_("A contest entry with this email has already been made."))

        return self.cleaned_data.get("email", None)

    def clean(self):
        if self.cleaned_data.get("email") != self.cleaned_data.get("email_confirm"):
            raise forms.ValidationError(_("Please make sure that your email is entered correctly."))

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(ContestEntryForm, self).__init__(*args, **kwargs)

        now = date.today()
        years = range(now.year - 100, now.year - 17)
        years.reverse()

        self.fields["birth_date"].widget = SelectDateWidget(years=years)
        #self.fields["state"].widget = USStateSelect()
        self.fields.keyOrder.insert(1, self.fields.keyOrder.pop())

    class Meta:
        model = ContestEntry
        exclude = ("timestamp",)
