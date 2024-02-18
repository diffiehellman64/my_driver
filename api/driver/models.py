from django.db import models
# from telegram_django_bot.models import TelegramUser


class Vehicle(models.Model):
    reg_number = models.CharField(max_length=15)
    color = models.CharField(max_length=100)


# class Driver(models.Model):
#     reg_number = models.TextField()
    # importance_level = models.PositiveSmallIntegerField()  # for example it will be integer field
    # project = models.ForeignKey('Project', on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tags')