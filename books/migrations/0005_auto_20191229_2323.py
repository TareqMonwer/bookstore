# Generated by Django 2.2.7 on 2019-12-29 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20191229_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('standard_pack', 'Can read all books')]},
        ),
    ]