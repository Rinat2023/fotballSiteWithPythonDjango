from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Match, Player, TicketOrder

def home(request):
    matches = Match.objects.select_related(
        "home_team",
        "away_team"
    ).order_by("-date")

    players = Player.objects.select_related(
        "team"
    ).order_by("-rating")

    return render(
        request,
        "appname/home.html",
        {
            "matches": matches,
            "players": players,
        }
    )


def match_detail(request, match_id):
    match = get_object_or_404(
        Match.objects.select_related(
            "home_team",
            "away_team"
        ),
        id=match_id
    )

    return render(
        request,
        "appname/match_detail.html",
        {
            "match": match
        }
    )


def player_detail(request, player_id):
    player = get_object_or_404(
        Player.objects.select_related("team"),
        id=player_id
    )

    return render(
        request,
        "appname/player_detail.html",
        {
            "player": player
        }
    )

@login_required(login_url="/login/")
def buy_ticket(request, match_id):
    match = get_object_or_404(Match, id=match_id)

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        quantity = int(request.POST.get("quantity", 1))

        order = TicketOrder.objects.create(
            match=match,
            name=name,
            phone=phone,
            email=email,
            quantity=quantity,
            price=1000,
        )

        return render(
            request,
            "appname/ticket_success.html",
            {
                "order": order
            }
        )

    return render(
        request,
        "appname/buy_ticket.html",
        {
            "match": match
        }
        
    )

def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = UserCreationForm()

    return render(
        request,
        "appname/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("home")

    else:

        form = AuthenticationForm()

    return render(
        request,
        "appname/login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    return redirect("home")