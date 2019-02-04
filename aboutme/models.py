from django.db import models

class AboutModel(models.Model):
    reason      =    models.CharField(max_length=50, default='ok')
    image       =    models.ImageField(upload_to='upImg', null=True)
    message     =    models.TextField()
    email       =    models.EmailField(null=True)

    def __str__(self):
        return self.message[:30]
