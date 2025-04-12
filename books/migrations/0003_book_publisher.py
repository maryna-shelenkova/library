# Generated by Django 5.1.7 on 2025-04-12 16:06

import books.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_discounted_price_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=books.models.user.get_first_admin, on_delete=django.db.models.deletion.PROTECT, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
