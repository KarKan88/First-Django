# Generated by Django 2.1.5 on 2019-02-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportAPI', '0003_auto_20190209_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='dummy', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uilayout',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
