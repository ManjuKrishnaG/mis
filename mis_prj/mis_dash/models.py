from django.db import models
from django.utils import timezone
from django.db.models import JSONField

class Field_Creation(models.Model):
    field=models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.field

class Title_Creation(models.Model):
    
    title_creation = models.CharField(max_length=255, blank=True)
    field_name = models.ManyToManyField(Field_Creation)
    disable=models.BooleanField(default=False)
    def __str__(self):
        return f"Data for {self.title_creation}"
 
   
 
class Location(models.Model):
    Title_Creation_names = models.ManyToManyField(Title_Creation)
    location = models.CharField(max_length=255)
    Division=models.CharField(max_length=200)
    def __str__(self):
        return f"Settings for {self.location}"
    
class FormData(models.Model):
    empid=models.CharField(max_length=20)
    firstname= models.CharField(max_length=50, default='0')
    form_number= models.IntegerField(default=0)
    title_creation = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255)
    field_value = models.CharField(max_length=255)
    division = models.CharField( max_length=50)
    location= models.CharField(max_length=100)
    date= models.DateField(default=timezone.now)
    edit= models.BooleanField(default=True)
    

class Show(models.Model):
    list= models.ManyToManyField(Title_Creation)
    locations=models.CharField( max_length=50)
    divisions=models.CharField( max_length=50)

class ApprovalNotification(models.Model):
    refid = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class UserMas(models.Model):
    s_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    approval_request_raised_by = models.CharField(max_length=255)
    request_status = models.CharField(max_length=255)
    action = models.CharField(max_length=255)


class Attachment(models.Model):
    Plan_forthe_Next_Month = models.CharField(max_length=255, default='0')
    attachment = models.FileField(upload_to='attachments/',  null= True)
    remarks = models.TextField(blank=True,default='0')
    uploaded_time = models.DateTimeField(auto_now_add=True)
    empid=models.CharField(max_length=30)
     
    def __str__(self):
        return f"Attachment {self.empid}: {self.attachment.name}"