# Generated by Django 5.0.2 on 2024-02-23 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_remove_csv_activated_csv_csv_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csv',
            old_name='csv_name',
            new_name='csv_file',
        ),
    ]
