from django.db import models

from library.models import UserCard
from user.models import Patron


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)


class Keyword(models.Model):
    word = models.CharField(max_length=255)


class Document(models.Model):
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField(Author, related_name='documents')
    price_value = models.IntegerField(max_length=100)
    keywords = models.ManyToManyField(Keyword, related_name='documents')  # i do not know

    class Meta:
        managed = False


class Copy(models.Model):
    document = models.ForeignKey(Document, on_delete=models.DO_NOTHING, related_name='copies')
    user_card = models.ForeignKey(UserCard, on_delete=models.DO_NOTHING, related_name='user_card')
    hash_number = models.IntegerField(max_length=100)
    is_checked_out = models.BooleanField(max_length=10)


class JournalArticles(Document):
    pass


class Book(Document):
    is_best_seller = models.BooleanField(max_length=10)
    edition = models.IntegerField(max_length=100)
    pass


class AudioVideo(Document):
    pass
