# Generated by Django 4.1.4 on 2022-12-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_review_created_date_review_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3),
        ),
    ]