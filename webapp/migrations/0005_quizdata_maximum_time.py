# Generated by Django 3.1.1 on 2020-10-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_quizdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizdata',
            name='Maximum_Time',
            field=models.CharField(default='10', max_length=20),
        ),
    ]