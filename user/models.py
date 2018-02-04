import datetime

from django.db import models


class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)


class Patron(User):
    def search_doc(self):
        pass

    def check_out_doc(self, document):
        for copy in document.copies.all():
            if not copy.is_checked_out:
                copy.is_checked_out = True
                self.user_card.copies.add(copy)
                copy.booking_date = datetime.date.today()
                copy.save()
                return True
        return False

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

    def check_overdue_copy(self):
        pass

    def add_doc(self):
        pass

    def delete_doc(self):
        pass

    def modify_doc(self):
        pass
