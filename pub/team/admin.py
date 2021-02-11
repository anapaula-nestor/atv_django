from django.contrib import admin
from team.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Team, TeamAdmin)