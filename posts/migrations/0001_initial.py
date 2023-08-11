# Generated by Django 4.1.4 on 2023-08-07 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userinstance')),
            ],
        ),
    ]