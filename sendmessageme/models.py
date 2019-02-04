from django.db import models

from django.db import models

class MessageMe(models.Model):
    your_name        =      models.CharField(max_length=50)
    your_email       =      models.EmailField()
    your_subject     =      models.CharField(max_length=50)
    your_message     =      models.TextField()

    def __str__(self):
        return self.your_subject[:30]

class CoderModel(models.Model):
    title            =       models.CharField(max_length=50)
    coder_message    =       models.TextField()

    def __str__(self):
        return self.title

class GetInTouch(models.Model):
    message = models.TextField(blank=True, default='I love hearing things form you')

    def __str__(self):
        return self.message[:30]

class SocialMediaModel(models.Model):
    GITHUB           =       models.URLField(max_length=200, blank=True)
    LINKEDIN         =       models.URLField(max_length=200, blank=True)
    TWITTER          =       models.URLField(max_length=200, blank=True)
    PINTEREST        =       models.URLField(max_length=200, blank=True)


    def __str__(self):
        return '%s,   %s,   %s,   %s' % (self.GITHUB[8:], self.LINKEDIN[8:], self.TWITTER[8:], self.PINTEREST[8:])
