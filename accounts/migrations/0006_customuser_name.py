# Generated by Django 4.2.16 on 2024-12-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_age_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
