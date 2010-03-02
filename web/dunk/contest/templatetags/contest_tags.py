from django import template

from contest.forms import ContestEntryForm


register = template.Library()


@register.inclusion_tag("contest/entry_form.html")
def contest_entry_form():
    return {
        "form": ContestEntryForm(),
    }
