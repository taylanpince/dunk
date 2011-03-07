from django.contrib import admin

from contests.actions import export_csv
from contest.models import ContestEntry


class ContestEntryAdmin(admin.ModelAdmin):
    actions = [export_csv]


admin.site.register(ContestEntry, ContestEntryAdmin)
