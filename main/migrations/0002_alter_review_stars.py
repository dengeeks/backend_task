# Generated by Django 5.0.4 on 2024-04-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(choices=[('*', '*'), ('**', '**'), ('***', '***'), ('****', '****'), ('*****', '*****')], max_length=100),
        ),
    ]
