# Generated by Django 4.2.1 on 2023-05-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brojSjedala', models.IntegerField()),
                ('idKorisnik', models.IntegerField()),
                ('idProjekcija', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projekcija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imeFilma', models.CharField(max_length=40)),
                ('vrijemeFilma', models.DateField()),
                ('kapacitetDvorane', models.IntegerField()),
            ],
        ),
    ]
