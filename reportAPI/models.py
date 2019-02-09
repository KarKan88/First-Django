"""
Model
"""
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class UILayout(models.Model):
    """
    Test Songs Class
    """
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    tsid = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {} - {}".format(self.pk, self.name, self.type)


class Category(models.Model):
    name = models.CharField(max_length=255)
    tsid = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{} - {}".format(self.pk, self.name)

class Association(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    table_name = models.CharField(max_length=255)
    association_table = models.CharField(max_length=255)
    join_type = models.CharField(max_length=255)
    table_column_name = models.CharField(max_length=255)
    association_column_name = models.CharField(max_length=255)
    tsid = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.pk, self.category_id, self.table_name, self.association_table, self.join_type, self.table_column_name, self.association_column_name)

class Attribute(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    column_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    column_title = models.CharField(max_length=255)
    column_type = models.CharField(max_length=255)
    column_format = models.CharField(max_length=255, null=True, blank=True)
    table_name = models.CharField(max_length=255)
    tsid = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.pk, self.category_id, self.column_name, self.description, self.column_title, self.column_type, self.column_format, self.table_name)

