# Generated by Django 3.2 on 2021-04-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=2048)),
                ('author_name', models.CharField(max_length=255)),
                ('upvoted', models.IntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
