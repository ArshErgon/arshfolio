from django.db import models

class SkillModel(models.Model):
    HTML5        =      models.CharField(max_length=50)
    CSS3         =      models.CharField(max_length=50)
    DJANGO       =      models.CharField(max_length=50)
    PYTHON       =      models.CharField(max_length=50)
    ANDROID      =      models.CharField(max_length=50)


    def __str__(self):
        return "HTML5 : %s, CSS3 : %s, DJANGO : %s, PTYHON : %s, ANDROID : %s" % (self.HTML5, self.CSS3, self.DJANGO, self.PYTHON, self.ANDROID)
