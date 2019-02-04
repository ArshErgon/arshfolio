from django.db import models

class ServiceModel(models.Model):
    work_completed           =      models.CharField(max_length=50)
    years_of_experience      =       models.CharField(max_length=50)
    total_client             =       models.CharField(max_length=50)
    award_won                =       models.CharField(max_length=50)


    def __str__(self):
        return 'Work: %s, years : %s, total: %s, award : %s' % (self.work_completed, self.years_of_experience, self.total_client, self.award_won)
