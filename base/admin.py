from django.contrib import admin

# Register your models here.
from .models import Book, Customer

admin.site.register(Customer)
admin.site.register(Book)