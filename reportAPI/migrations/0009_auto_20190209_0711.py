# Generated by Django 2.1.5 on 2019-02-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportAPI', '0008_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='column_format',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
