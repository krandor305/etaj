# Generated by Django 2.0.6 on 2018-11-09 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=200)),
                ('Image', models.ImageField(default='default.png', upload_to='')),
            ],
        ),
    ]
