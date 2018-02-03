from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)


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
    document = models.ForeignKey(Document)
    hash_number = models.IntegerField(max_length=100)
    pass


class JournalArticles(models.Model, Document):
    pass


class Book(models.Model, Document):
    edition = models.IntegerField(max_length=100)
    pass


class AudioVideo(models.Model, Document):
    pass
