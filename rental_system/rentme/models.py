from django.db import models


# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=255)
    categories = [
        (None, 'Choose Category'),
        ('Buy', 'Property to buy'),
        ('Rent', 'Property to rent'),
        ('Sell', 'Property to sell'),
        ('Lease', 'Property to lease'),
    ]
    category = models.CharField(max_length=5, choices=categories, default=None)

    class Meta:
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.name()


class Person(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()

    class Meta:
        abstract = True


class Landlord(Person):

    def __str__(self):
        return self.name()


class Tenant(Person):

    def __str__(self):
        return self.name()


class Employee(Person):

    def __str__(self):
        return self.name()


class MaintenanceRequest(models.Model):
    # Possible issues
    issues = [
        (None, 'Issue'),
        ('A', 'Electrical'),
        ('B', 'Water'),
        ('C', 'Security'),
    ]
    category = models.CharField(max_length=1, choices=issues, default=None)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)


class MaintenanceTask(models.Model):
    description = models.TextField()


class Lease(models.Model):
    start_date = models.DateField(auto_now_add=False, blank=False, null=False)
    end_date = models.DateField(auto_now_add=False, blank=False, null=False)


class Payment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
