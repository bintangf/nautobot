# Generated by Django 3.2.18 on 2023-03-17 20:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0074_job__unique_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gitrepository",
            name="_token",
        ),
        migrations.RemoveField(
            model_name="gitrepository",
            name="username",
        ),
    ]