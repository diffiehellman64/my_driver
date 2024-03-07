from django.db import models
from telegram_django_bot.models import TelegramUser

class User(TelegramUser):
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Folder.objects.get_or_create(
        #     user=self,
        #     parent=None,
        #     defaults={'name': ''}
        # )

# Транспорт
class Vehicle(models.Model):
    reg_number = models.CharField(max_length=15)
    color = models.CharField(max_length=100)
    passengers_count = models.IntegerField()

# Водитель
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

# Поездка
class Drive(models.Model):
    drive = models.ForeignKey(Driver, on_delete=models.CASCADE)
    passengers = models.ManyToManyField(User)
    passengers_available_count = models.IntegerField()
