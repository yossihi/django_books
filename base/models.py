from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    pub_year = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
              return self.name + "  by " + self.author

class Customer(models.Model):
        name = models.CharField(max_length=50, null=False)
        age = models.IntegerField()
        birth_date = models.DateField()
        email = models.EmailField()

        def __str__(self) -> str:
              return self.name + "   " + str(self.age)
