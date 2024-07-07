from django.db import models


class Doctors(models.Model):
    FIRST_AID = 'lekarz rodziny'
    PEDIATRICIAN = 'pediatra'
    COMMUNITY_NURSE = 'pielęgniarka środowiskowa'
        
    SPECIALIZATION_CHOICES = [
            (FIRST_AID, 'Lekarz rodziny'),
            (PEDIATRICIAN, 'Pediatra'),
            (COMMUNITY_NURSE, 'Pielęgniarka środowiskowa'),
        ]

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField()
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Message(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    number_phone = models.CharField(max_length=15)
    email = models.CharField(max_length=64)
