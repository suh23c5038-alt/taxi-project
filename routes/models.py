from django.db import models
from django.contrib.auth.models import User

# 1. تعريف المحطات (الرمادي، الفلوجة، إلخ)
class Station(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} ({self.code})"

# 2. تعريف الرحلات (تكسي الأنبار)
class Route(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    # Passengers - قمنا بتغيير الـ related_name لضمان عدم حدوث تضارب
    passengers = models.ManyToManyField(User, blank=True, related_name="booked_routes")
    
    # حقول معلومات السائق للتواصل المباشر
    driver_name = models.CharField(max_length=64, default="سائق تكسي")
    driver_phone = models.CharField(max_length=15, default="0770")

    def __str__(self):
        return f"{self.id}: {self.origin.name} to {self.destination.name}"