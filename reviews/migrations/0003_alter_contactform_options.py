# Generated by Django 4.0.4 on 2023-02-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_review_contactform'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': 'Контактная форма', 'verbose_name_plural': 'Формы обратной связи'},
        ),
    ]
