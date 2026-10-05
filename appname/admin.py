from django.contrib import admin
from .models import Team, Player, Match, TicketOrder


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "team",
        "position",
        "age",
        "goals",
        "assists",
        "rating",
    )

    list_filter = ("position", "team")


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "home_team",
        "away_team",
        "home_score",
        "away_score",
        "date",
        "status",
    )

    list_filter = ("status", "date")

@admin.register(TicketOrder)
class TicketOrderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "match",
        "quantity",
        "price",
        "created_at",
    )

    list_filter = ("created_at",)

    search_fields = (
        "name",
        "phone",
        "email",
    )