from django.db import models
from django_enumfield import enum

#Create class for brand status
class OrderStatus(enum.Enum):
    PENDING = 0
    PROCESSING = 1
    COMPLETED = 2
    CANCELED = 3

    __labels__ = {
        PENDING: "Pending",
        PROCESSING: "Processing",
        COMPLETED: "Completed",
        CANCELED: "Canceled"
    }

class Project(models.Model):

    brand = models.CharField(max_length=200) # Brand name
    holder = models.TextField() # Holder
    registration_number = models.CharField(max_length=50, unique=True, null=True, blank=True)  # Registration number
    country = models.CharField(max_length=100, null=True, blank=True)  # Country of registration
    status = enum.EnumField(OrderStatus, default = OrderStatus.PENDING) # Registration status
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} - {self.holder}"