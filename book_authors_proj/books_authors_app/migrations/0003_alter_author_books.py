# Generated by Django 3.2.6 on 2021-08-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='author', to='books_authors_app.Book'),
        ),
    ]
