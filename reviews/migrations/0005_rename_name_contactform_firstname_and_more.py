# Generated by Django 4.0.4 on 2023-05-14 16:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_contactform_name_alter_contactform_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='review',
        ),
        migrations.AddField(
            model_name='contactform',
            name='lastname',
            field=models.CharField(blank=True, max_length=50, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='телефон'),
        ),
    ]
