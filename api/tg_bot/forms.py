from django.utils.translation import gettext_lazy as _
from django import forms
from telegram_django_bot import forms as td_forms

from driver.models import Vehicle, Drive

class VehicleForm(td_forms.TelegramModelForm):
    form_name = _("Menu file")

    class Meta:
        model = Vehicle
        fields = ('reg_number', 'color', 'passengers_count', 'driver')

        labels = {
            'reg_number': _('Государственный регистрационный знак'),
            'passengers_count': _('Количетсов пассажиров'),
            'color': _('Цвет'),
        }

class DriveForm(td_forms.TelegramModelForm):
    form_name = _("Menu file")

    class Meta:
        model = Drive
        fields = ('passengers_available_count', 'vehicle')

        labels = {
            'passengers_available_count': _('Количетсво пассажиров, которых готов взять с собой'),
        }

