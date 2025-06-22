from django.db import models

class ClassBooking(models.Model):
    CLASS_TYPES = [
        ('CBSE', 'CBSE'),
        ('JEE', 'JEE'),
        ('NEET', 'NEET'),
        ('One-to-One', 'One-to-One')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    class_type = models.CharField(max_length=10, choices=CLASS_TYPES)
    preferred_subject = models.CharField(max_length=100, blank=True, null=True)  # Only for one-to-one class booking
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.class_type}'
