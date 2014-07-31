from django.db import models
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import datetime
from django.utils import timezone

# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	birth = models.DateField()
	number = models.IntegerField()
	group = models.ForeignKey('Group')

	def __str__(self):
		return self.last_name+ ' ' + self.first_name

	def get_absolute_url(self):
		return '/student_view/' + self.id.__str__() + '/'

class Group(models.Model):
	title = models.CharField(max_length=50)
	cheif = models.ForeignKey(to='Student',unique=True, blank=True, null=True, related_name='cheif')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/group_view/' + self.id.__str__() + '/'

class Signal(models.Model):
	type_signal = models.CharField(max_length=50)
	sender = models.CharField(max_length=50)
	date = models.DateTimeField('date signal')

	def __str__(self):
		return self.sender + ' ' + self.type_signal


@receiver(post_save, sender=Group)
@receiver(post_save, sender=Student)
@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def write_action(instance, **kwargs):
	type_signal = ''
	if 'created' in kwargs:
		if kwargs['created'] == True:
			type_signal = 'created'
		else:
			type_signal = 'updated'
	else:
		type_signal = 'deleted'
	signal = Signal(type_signal=type_signal, sender=(instance.__class__).__qualname__,date=timezone.now())
	signal.save()


