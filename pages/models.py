from django.db import models

# Create your models her
class FormContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Form Contact"
        verbose_name_plural = "Form Contacts"