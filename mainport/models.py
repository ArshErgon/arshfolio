from django.db import models

class Project(models.Model):
	PROJECT_CATEGORY = (
			('WEB-DEVELOPMENT-DJANGO', 'DJANGO'),
			('ANDROID', 'ANDROID'),
	)
	project_name = models.CharField(max_length=50)
	project_image = models.ImageField(upload_to='proImg', blank=True)
	project_url = models.URLField(max_length=200)
	project_url_name = models.CharField(max_length=50)
	project_source_code = models.URLField(max_length=200, null=True)
	project_date = models.DateTimeField(null=True, blank=True)
	project_category = models.CharField(max_length=30, choices=PROJECT_CATEGORY)

	def __str__(self):
		return self.project_name


class Quote(models.Model):
	name = models.CharField(max_length=50)
	quote = models.TextField()

	def __str__(self):
		return "%s by %s" % (self.quote[:10], self.name)
