from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_id",
        "first_name",
        "last_name",
        "username",
        "is_premium",
        "user_data",
        "init_data",
    )
    search_fields = ("telegram_id", "username")