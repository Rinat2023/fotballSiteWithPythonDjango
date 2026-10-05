from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_CHOICES = [
        ("GK", "Вратарь"),
        ("DEF", "Защитник"),
        ("MID", "Полузащитник"),
        ("ATT", "Нападающий"),
    ]

    name = models.CharField(max_length=100)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players"
    )

    country = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES
    )

    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    matches = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)

    rating = models.FloatField(default=0)

    photo = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    STATUS_CHOICES = [
        ("UPCOMING", "Предстоящий"),
        ("LIVE", "Идёт"),
        ("FINISHED", "Завершён"),
    ]

    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="home_matches"
    )

    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="away_matches"
    )

    date = models.DateTimeField()

    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    # Статистика матча

    possession_home = models.PositiveIntegerField(default=50)
    possession_away = models.PositiveIntegerField(default=50)

    shots_home = models.PositiveIntegerField(default=0)
    shots_away = models.PositiveIntegerField(default=0)

    shots_on_target_home = models.PositiveIntegerField(default=0)
    shots_on_target_away = models.PositiveIntegerField(default=0)

    corners_home = models.PositiveIntegerField(default=0)
    corners_away = models.PositiveIntegerField(default=0)

    fouls_home = models.PositiveIntegerField(default=0)
    fouls_away = models.PositiveIntegerField(default=0)

    yellow_home = models.PositiveIntegerField(default=0)
    yellow_away = models.PositiveIntegerField(default=0)

    red_home = models.PositiveIntegerField(default=0)
    red_away = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.home_team} — {self.away_team}"

class TicketOrder(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="ticket_orders"
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name} — {self.match}"