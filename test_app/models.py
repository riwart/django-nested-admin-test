from django.db import models

class Parent(models.Model):
	name = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Child1(models.Model):
	name = models.CharField(max_length=10)
	parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, blank=True, null=True)
	def __str__(self):
		return self.name

class Child2(models.Model):
	name = models.CharField(max_length=10)
	child1 = models.ForeignKey(Child1, on_delete=models.SET_NULL, blank=True, null=True)
	def __str__(self):
		return self.name