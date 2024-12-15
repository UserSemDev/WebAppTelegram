from django.urls import path
from bot.apps import BotConfig
from bot.views import IndexWebAppView

app_name = BotConfig.name

urlpatterns = [
    path("", IndexWebAppView.as_view(), name="index"),
]