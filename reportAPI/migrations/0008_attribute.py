# Generated by Django 2.1.5 on 2019-02-09 06:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reportAPI', '0007_auto_20190209_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('column_title', models.CharField(max_length=255)),
                ('column_type', models.CharField(max_length=255)),
                ('column_format', models.CharField(max_length=255)),
                ('table_name', models.CharField(max_length=255)),
                ('tsid', models.DateTimeField(default=django.utils.timezone.now)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reportAPI.Category')),
            ],
        ),
    ]
