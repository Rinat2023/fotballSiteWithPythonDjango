from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "match/<int:match_id>/",
        views.match_detail,
        name="match_detail"
    ),

    path(
        "player/<int:player_id>/",
        views.player_detail,
        name="player_detail"
    ),
    path(
    "match/<int:match_id>/buy/",
    views.buy_ticket,
    name="buy_ticket"
    ),
    path(
    "register/",
    views.register_view,
    name="register"
),

path(
    "login/",
    views.login_view,
    name="login"
),

path(
    "logout/",
    views.logout_view,
    name="logout"
),
]