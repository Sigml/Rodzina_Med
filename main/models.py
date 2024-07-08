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
    monday = models.CharField(max_length=20, null=True)
    tuesday = models.CharField(max_length=20, null=True)
    wednesday = models.CharField(max_length=20, null=True)
    thursday = models.CharField(max_length=20, null=True)
    friday = models.CharField(max_length=20, null=True)
    file_upload = models.FileField(upload_to='doctor_files/', null=True, blank=True)

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
    number_phone_1 = models.CharField(max_length=15)
    number_phone_2 = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=64)


class Rodo(models.Model):
    text = models.TextField()
    file_upload = models.FileField(upload_to='files/', null=True, blank=True)
    
    
class Reglamin(models.Model):
    text = models.TextField()
    file_upload = models.FileField(upload_to='files/', null=True, blank=True)
    
    
class File_to_download(models.Model):
    rodo = models.FileField(upload_to='files_to_download/', null=True, blank=True)
    reglamin = models.FileField(upload_to='files_to_download/', null=True, blank=True)
    doctor = models.FileField(upload_to='files_to_download/', null=True, blank=True)
    nurse = models.FileField(upload_to='files_to_download/', null=True, blank=True)
    instruction = models.FileField(upload_to='files_to_download/', null=True, blank=True)
    calendar = models.FileField(upload_to='files_to_download/', null=True, blank=True)
    application_for_authorisation = models.FileField(upload_to='files_to_download/', null=True, blank=True)
