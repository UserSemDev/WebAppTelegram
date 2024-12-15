from django.db import models


class User(models.Model):
    telegram_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    user_data = models.TextField(null=True, blank=True)  # TextField to store JSON user data
    init_data = models.TextField(null=True, blank=True)  # TextField to store JSON init data

    def __str__(self):
        return self.username or self.telegram_id