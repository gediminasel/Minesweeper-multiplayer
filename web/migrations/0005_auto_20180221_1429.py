# Generated by Django 2.0.2 on 2018-02-21 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_slidervalues'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SliderValues',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]