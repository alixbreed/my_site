from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Expense(models.Model):
    date = models.DateField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    comment = models.CharField(max_length=32, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1}'.format(self.date, self.cost)