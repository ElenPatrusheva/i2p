# i2p
project_libarary
# Instructions
you will need installed python3 and pip3
* Download all files and unzip (if necessary)
* Instruction for windows:
* Open terminal (Win+R)
* write: pip install django
* write: pip install Pillow
* go to project directory
* write: python manage.py makemigrations
* write: python manage.py migrate
* write: python manage.py shell
* now you are ready to test.
* you shold import what you will need
* Example: from documents.models import Documents
* you may craete: library, all types of documents (books, a/v files, articles), copies, users and all required fields
* Example: library = Library.objects.create()
* you may create user (and all necessary objects) then search for documents and check out a copy of the document. 
* all the fields and functions are available in the code.
* after execution print exit()
