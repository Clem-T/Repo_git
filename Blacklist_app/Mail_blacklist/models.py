# -*- coding: utf-8 -*-
from django.db import models

class EnumField(models.Field):
    """
    A field class that maps to MySQL's ENUM type.

    Usage:

    class Card(models.Model):
        suit = EnumField(values=('Clubs', 'Diamonds', 'Spades', 'Hearts'))

    c = Card()
    c.suit = 'Clubs'
    c.save()
    """
    def __init__(self, *args, **kwargs):
        if "values" in kwargs:
            self.values = kwargs.pop('values')
            kwargs['choices'] = [(v, v) for v in self.values]
            kwargs['default'] = self.values[0]
        super(EnumField, self).__init__(*args, **kwargs)

    def db_type(self, connection=None):
        return "enum({0})".format( ','.join("'%s'" % k for (k, _) in self.choices) )
    #EnumField class adapted from
    #http://stackoverflow.com/questions/21454/specifying-a-mysql-enum-in-a-django-model

class Email(models.Model):
    email = models.CharField(max_length=128, null=True)
    user_id = models.IntegerField(default=0, null=False)
    type = EnumField(values=('Bounce','Blacklist'))
    class Meta:
        db_table = 'blacklist' #if not specified the table name is appname_classname
        unique_together = (("email","user_id"),)
        