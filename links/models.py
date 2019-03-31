from django.db import models

# Create your models here.
class Link(models.Model):
	title = models.CharField(max_length=50, unique=True)
	clicks = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	def visit(self):
		self.clicks = self.clicks + 1
		self.save()

	def edit(self, new_title):
		self.title = new_title
		self.save()


