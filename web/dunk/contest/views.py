from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from contest.forms import ContestEntryForm


def entry(request):
    """
    Renders or processes a ContestEntryForm
    """
    if request.method == "POST":
        form = ContestEntryForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("contest_entry_done"))
    else:
        form = ContestEntryForm()

    return render_to_response("contest/entry.html", {
        "form": form,
    }, context_instance=RequestContext(request))
