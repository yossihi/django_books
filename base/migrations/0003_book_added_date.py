# Generated by Django 5.0.1 on 2024-01-21 10:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_books_book_rename_customers_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
