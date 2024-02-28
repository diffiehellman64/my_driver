from telegram_django_bot import forms as td_forms
from telegram_django_bot.td_viewset import TelegramViewSet
from .models import Vehicle


class VehicleForm(td_forms.TelegramModelForm):
    class Meta:
        model = Vehicle
        fields = ['reg_number', 'color']


class VehicleViewSet(TelegramViewSet):
    model_form = VehicleForm
    queryset = Vehicle.objects.all()
    viewset_name = 'Vehicle'