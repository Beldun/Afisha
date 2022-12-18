# Generated by Django 4.1.4 on 2022-12-18 10:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.SmallIntegerField(default=3, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(1)]),
        ),
    ]
