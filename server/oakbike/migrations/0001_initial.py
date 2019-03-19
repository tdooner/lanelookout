# Generated by Django 2.1 on 2019-02-20 04:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('img_url', models.CharField(blank=True, max_length=256)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
