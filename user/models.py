from django.db import models

from documents.models import Book, JournalArticles  #


class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    id = models.IntegerField(max_length=100)

    class Meta:
        managed = False


class Patron(models.Model, User):
    books = models.ManyToManyField(Book, related_name="user")  ## очень хочу матрицу
    audio_video = models.ManyToManyField(JournalArticles, related_name="audio_video")
    journal_articles = models.ManyToManyField(Book, related_name="journal_articles")

    def is_overdue(self):  # bool
        pass

    pass


class Student(models.Model, Patron):
    pass


class Teacher(models.Model, Patron):
    pass


class Librarian(models.Model, User):

    def add(self):
        pass

    pass
