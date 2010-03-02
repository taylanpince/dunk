from django import template
from django.conf import settings

from contest.forms import ContestEntryForm


register = template.Library()


@register.inclusion_tag("contest/entry_form.html")
def contest_entry_form():
    return {
        "form": ContestEntryForm(),
        "MEDIA_URL": settings.MEDIA_URL,
    }
