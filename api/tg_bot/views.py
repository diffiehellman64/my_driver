import copy
from uuid import uuid4

from django.conf import settings

from telegram_django_bot.models import MESSAGE_FORMAT
from telegram_django_bot.routing import telegram_reverse
from telegram_django_bot.telegram_lib_redefinition import InlineKeyboardButtonDJ, InlineKeyboardMarkupDJ
from telegram_django_bot.td_viewset import TelegramViewSet
from telegram_django_bot.utils import handler_decor
from telegram_django_bot.tg_dj_bot import TG_DJ_Bot

from django.utils import timezone
from django.utils.translation import gettext as _, gettext_lazy
from django.db.models import Count, F

from telegram import Update

# from .models import MountInstance, ShareLink, User, File, Folder
from driver.models import User, Vehicle, Drive
from .forms import VehicleForm, DriveForm
# from .permissions import CheckFolderPermission, CheckFilePermission


@handler_decor()
def start(bot: TG_DJ_Bot, update: Update, user: User):
    user.clear_status()

    message = _(
        'Привет! 🤖\n\n'
        'Я создан для того чтобы помочь тебе добраться куда нужно!\n'
    )

    buttons = []

    drive_views = DriveViews(telegram_reverse('drive_path'))
    vehicle_views = VehicleViews(telegram_reverse('vehicle_path'))

    if user.vehicles.count() == 0:
        # Если пользователь выбрал, что он водитель и у него нет ТС, то надо добавить
        driver_button = InlineKeyboardButtonDJ(
            text = _('Я водитель'),
            callback_data = vehicle_views.gm_callback_data('create')
        )
    else:
        driver_button = InlineKeyboardButtonDJ(
            text = _('Я водитель'),
            callback_data = drive_views.gm_callback_data('create', i_driver=True)
        )

    buttons.append([
        InlineKeyboardButtonDJ(
            text = _('Я пассажир'),
            callback_data=drive_views.gm_callback_data('show_list')
        ),
        driver_button
    ])

    return bot.edit_or_send(update, message, buttons)


class DriveViews(TelegramViewSet):
    model_form = DriveForm
    queryset = Drive.objects.all()
    viewset_name = gettext_lazy('Drive')
    # updating_fields = ['color']

    def create(self, field=None, value=None, initial_data=None):
        vehicles = self.user.vehicles
        if vehicles.count() == 1:
            vehicle = vehicles.first()
            initial_data = {
                'vehicle': vehicle
            }
        return super().create(field, value, initial_data)

    def show_list(self, page=0, per_page=10, columns=1):
        buttons = []
        buttons.append([
            InlineKeyboardButtonDJ(
                text=_('Назад'),
                callback_data='/start'
            )
        ])
        msg = 'ok!'
        return self.CHAT_ACTION_MESSAGE, (msg, buttons)

class VehicleViews(TelegramViewSet):
    viewset_name = 'VehicleViews'
    model_form = VehicleForm
    queryset = Vehicle.objects.all()
    viewset_name = gettext_lazy('Vehicle')
    updating_fields = ['color', 'reg_number', 'passengers_count']

    def create(self, field=None, value=None, initial_data=None):
        initial_data = {
            'driver': self.user,
        }
        return super().create(field, value, initial_data)

    def show_list(self, page=0, per_page=10, columns=1):
        buttons = []
        buttons.append([
            InlineKeyboardButtonDJ(
                text=_('Назад'),
                callback_data='/start'
            )
        ])
        msg = 'ok!'
        return self.CHAT_ACTION_MESSAGE, (msg, buttons)
