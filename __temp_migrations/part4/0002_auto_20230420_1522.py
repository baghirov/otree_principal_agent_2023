# Generated by Django 2.2.12 on 2023-04-20 12:22

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=14, null=True),
        ),
    ]
