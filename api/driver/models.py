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
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return self.reg_number

# Поездка
class Drive(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True, related_name='drives')
    passengers = models.ManyToManyField(User, related_name='passenger_drives')
    passengers_available_count = models.IntegerField(null=True)
