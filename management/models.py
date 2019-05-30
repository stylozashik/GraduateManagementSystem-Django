from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Management(models.Model):
	student_id = models.CharField(max_length=100)
	image = models.FileField(blank=True,null=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	father_name = models.CharField(max_length=200)
	mother_name = models.CharField(max_length=200)
	Present_address = models.TextField(max_length=400)
	Permanent_address = models.TextField(max_length=400)
	contact = models.CharField(max_length=11)
	# avg_cgpa = models.DecimalField(max_digits=5,decimal_places=2)
	avg_cgpa = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(4)],)

	def __str__(self):
		return self.student_id

	def passed(self):
		return self.avg_cgpa > 2

	def grade1(self):
		return self.avg_cgpa == 4

	def grade2(self):
		return self.avg_cgpa > 3.74

	def grade3(self):
		return self.avg_cgpa > 3.49

	def grade4(self):
		return self.avg_cgpa > 3.24

	def grade5(self):
		return self.avg_cgpa > 2.99

	def grade6(self):
		return self.avg_cgpa > 2.74

	def grade7(self):
		return self.avg_cgpa > 2.49

	def grade8(self):
		return self.avg_cgpa > 2.24

	def grade9(self):
		return self.avg_cgpa > 1.99












