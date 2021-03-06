# Generated by Django 3.2.9 on 2021-12-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_blog', '0005_auto_20211208_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais_origem',
            field=models.CharField(max_length=20),
        ),
    ]
