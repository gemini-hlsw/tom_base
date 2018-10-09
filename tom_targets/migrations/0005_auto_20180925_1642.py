# Generated by Django 2.0.6 on 2018-09-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_targets', '0004_target_parallax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='parallax',
            field=models.FloatField(blank=True, help_text='Parallax, in milliarcseconds.', null=True, verbose_name='Parallax'),
        ),
    ]