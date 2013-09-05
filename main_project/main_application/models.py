#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=150, verbose_name='Title')
	first_author = models.CharField(max_length=150, verbose_name='First author')
	quality = models.PositiveSmallIntegerField(verbose_name='Quality', help_text='Quality value')
	already_read = models.BooleanField(verbose_name='Was already read', help_text='Already read or not')
	
	IMAGE_PROCESSING = 'IMAGE_PROCESSING'
	INFORMATICS = 'INFORMATICS'
	MEDICINE = 'MEDICINE'
	PARAMETER_TYPE_CHOICES = (
        (IMAGE_PROCESSING, 'IMAGE PROCESSING'),
        (INFORMATICS, 'INFORMATICS'),
        (MEDICINE, 'MEDICINE'),
    )
	subject = models.CharField(max_length=25,choices=PARAMETER_TYPE_CHOICES, default=INFORMATICS, verbose_name='Main article subject', help_text='Main article subject')
	
	user = models.ManyToManyField(User)
	
	def __str__(self):
		return self.title

class Profile(models.Model):
	user = models.ForeignKey(User, unique=True)
	country = models.CharField(max_length=15,verbose_name='Country')

	def __str__(self):
		return self.user.username

# class Parameter(models.Model):
	# id = models.AutoField(primary_key=True)
	# #order = models.PositiveSmallIntegerField(null=False)
	# label = models.CharField(max_length=50, verbose_name='Param label', unique=True)
	# description = models.CharField(max_length=200, verbose_name='Param description')

	# NUMBER = 'NUM'
	# BOOLEAN = 'BOOL'
	# TEXT = 'TEXT'
	# CHOICES = 'CHOICES'
	# PARAMETER_TYPE_CHOICES = (
        # (NUMBER, 'Numeric value'),
        # (BOOLEAN, 'Boolean value'),
        # (TEXT, 'String value'),
        # (CHOICES, 'Selection value'),
    # )
	# type = models.CharField(max_length=15,choices=PARAMETER_TYPE_CHOICES, default=TEXT,null=False)
	
	# min_value = models.CharField(max_length=15, verbose_name='Min value for numerical values', default='NULL')
	# max_value = models.CharField(max_length=15, verbose_name='Max value for numerical values', default='NULL')
	# choices = models.CharField(max_length=200, verbose_name='Choices to be selected', default='NULL')

class Field(models.Model):
	id = models.AutoField(primary_key=True)
	label = models.CharField(max_length=50, verbose_name='Param label', unique=True)
	description = models.CharField(max_length=200, verbose_name='Param description')

	NUMBER = 'NUM'
	BOOLEAN = 'BOOL'
	TEXT = 'TEXT'
	CHOICES = 'CHOICES'
	FIELD_TYPE_CHOICES = (
        (NUMBER, 'Numeric value'),
        (BOOLEAN, 'Boolean value'),
        (TEXT, 'String value'),
        (CHOICES, 'Selection value'),
    )
	field_type = models.CharField(max_length=15,choices=FIELD_TYPE_CHOICES, default=TEXT,null=False)
	
	min_value = models.CharField(max_length=15, verbose_name='Min value for numerical values', default='NULL')
	max_value = models.CharField(max_length=15, verbose_name='Max value for numerical values', default='NULL')
	choices = models.CharField(max_length=200, verbose_name='Choices to be selected', default='NULL')
	basic_info = models.BooleanField(verbose_name='Is basic info?', help_text='Is basic info?')
	
	EVENT = 'EVNT'
	AUTHOR = 'AUTH'
	PARENTFORM_TYPE_CHOICES = (
        (EVENT, 'Event info'),
        (AUTHOR, 'Author info'),
	)
	parentform_type = models.CharField(max_length=15, choices=PARENTFORM_TYPE_CHOICES, default=TEXT, null=False)

	def __unicode__(self):
		return self.label

class Person(models.Model):
	user = models.ForeignKey(User, unique=True)
	country = models.CharField(max_length=15,verbose_name='Country')
	fields = models.ManyToManyField(Field, through='PersonFieldValues')

	def __str__(self):
		return self.user.username

class PersonFieldValues(models.Model):
	person = models.ForeignKey(Person)
	field = models.ForeignKey(Field)
	value = models.CharField(max_length=50, verbose_name='Field value', null=False)