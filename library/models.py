from django.db import models

from user.models import User


class UserCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='user_card')


class Library(models.Model):
    def calculate_items(self):
        pass

    def is_due(self):
        pass

    def overdue_fines(self):
        pass
