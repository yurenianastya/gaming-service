from django.db import models

class VideoGame(models.Model):

    RTS = 'RealTimeStrategy'
    MMORPG = 'OnlineMassiveMultiplayerRPG'
    ACTION_ADVENTURE = 'ActionAdventure'
    SANDBOX = 'Sandbox'
    SHOOTER = 'Shooter'
    UNKNOWN = 'unknown'
    XBOX = 'Xbox'
    PS = 'PS'
    PC = 'PC'
    MOBILE = 'MobilePhone'
    SWITCH = 'NintendoSwitch'

    GENRE_CHOICES = [
    (RTS, 'RealTimeStrategy'),
    (MMORPG, 'OnlineMassiveMultiplayerRPG'),
    (ACTION_ADVENTURE, 'ActionAdventure'),
    (SANDBOX, 'Sandbox'),
    (SHOOTER, 'Shooter'),
    (UNKNOWN, 'unknown'),
    ]

    INPUT_CHOICES = [
    (XBOX, 'Xbox'),
    (PS, 'PS'),
    (PC, 'PC'),
    (MOBILE, 'MobilePhone'),
    (SWITCH, 'NintendoSwitch'),
    (UNKNOWN, 'unknown'),
    ]

    title_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default=UNKNOWN)
    rating = models.IntegerField()
    platform = models.CharField(max_length=100, choices=INPUT_CHOICES, default=UNKNOWN)
    release_date = models.DateTimeField(auto_now_add=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    class Meta:
        ordering = ['title_name']
