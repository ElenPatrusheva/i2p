from django.db import models

from library.models import Library


class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    library_card_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    library = models.ForeignKey(Library, on_delete=models.DO_NOTHING, related_name='users')

    class Meta:
        managed = False


class Patron(User):
    def search_doc(self):
        pass

    def check_out_doc(self):
        pass

    def return_doc(self):
        pass

    def is_overdue(self):  # bool
        pass


class Student(Patron):
    pass


class Faculty(Patron):
    pass


class Librarian(User):
    def manage_patron(self):
        pass

    def check_overdue_doc(self):
        pass

    def add_doc(self):
        pass

    def delete_doc(self):
        pass

    def modify_doc(self):
        pass
