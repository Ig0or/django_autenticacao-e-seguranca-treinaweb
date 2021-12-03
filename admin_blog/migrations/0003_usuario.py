# Generated by Django 3.2.9 on 2021-12-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_blog', '0002_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pais_origem', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
