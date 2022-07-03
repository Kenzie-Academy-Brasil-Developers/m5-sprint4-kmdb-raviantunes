# Generated by Django 4.0.5 on 2022-07-03 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('review', models.TextField()),
                ('spoilers', models.BooleanField(default=False)),
                ('recomendation', models.CharField(choices=[('MW', 'Must Watch'), ('SW', 'Should Watch'), ('AW', 'Avoid Watch'), ('NO', 'No Opinion')], default='NO', max_length=50)),
            ],
        ),
    ]
