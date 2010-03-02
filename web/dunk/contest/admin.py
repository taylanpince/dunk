from django.contrib import admin

from contest.models import ContestEntry


class ContestEntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContestEntry, ContestEntryAdmin)
