import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from bot.models import User


@method_decorator(csrf_exempt, name='dispatch')
class IndexWebAppView(generic.TemplateView):
    extra_context = {"title": "Web App Telegram"}
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        """Обработка POST-запроса от Telegram Web App"""
        try:
            # Читаем тело запроса
            data = json.loads(request.body.decode("utf-8"))
            telegram_id = data.get("telegram_id")
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            username = data.get("username")
            is_premium = data.get("is_premium", False)
            user_data = data.get("user_data", {})
            init_data = data.get("init_data", {})

            # Создаем или обновляем пользователя
            user, created = User.objects.get_or_create(telegram_id=telegram_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.is_premium = is_premium
            user.user_data = json.dumps(user_data)
            user.init_data = json.dumps(init_data)
            user.save()

            # Возвращаем успешный ответ
            return JsonResponse({"status": "success", "user_id": user.id})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
