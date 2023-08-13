# Generated by Django 4.2.2 on 2023-07-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre', models.CharField(max_length=255)),
                ('centreid', models.CharField(max_length=255)),
                ('cluster', models.CharField(max_length=255)),
                ('centrepostalcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='elder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elder', models.CharField(max_length=255)),
                ('eldergender', models.CharField(max_length=255)),
                ('elderid', models.CharField(max_length=255)),
                ('nricorfin', models.CharField(max_length=255)),
                ('postalcode1', models.CharField(max_length=255)),
                ('postalcode2', models.CharField(max_length=255)),
                ('centre', models.CharField(max_length=255)),
                ('tofromcentre', models.CharField(max_length=255)),
                ('weekday', models.CharField(max_length=255)),
                ('etaetd', models.CharField(max_length=255)),
                ('timepickupdeliver', models.CharField(max_length=255)),
                ('eldertype', models.CharField(max_length=255)),
                ('elderservicetype', models.CharField(max_length=255)),
                ('caregiver', models.CharField(max_length=255)),
                ('loadingtime', models.CharField(max_length=255)),
                ('rowid', models.IntegerField(null=True)),
                ('fromtopostal', models.IntegerField(null=True)),
                ('distancekm', models.IntegerField(null=True)),
                ('minn', models.IntegerField(null=True)),
                ('min', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre', models.CharField(max_length=255)),
                ('tripid', models.CharField(max_length=255)),
                ('seqid', models.CharField(max_length=255)),
                ('vehicleplate', models.CharField(max_length=255)),
                ('vehicletype', models.CharField(max_length=255)),
                ('vehicleid', models.CharField(max_length=255)),
                ('vehiclecapacity', models.CharField(max_length=255)),
                ('maxwheelchairelder', models.CharField(max_length=255)),
                ('maxambulantelder', models.CharField(max_length=255)),
                ('maxcaregiver', models.CharField(max_length=255)),
            ],
        ),
    ]