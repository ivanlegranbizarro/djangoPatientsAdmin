# Generated by Django 4.1.3 on 2022-12-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('TM', 'TransMale'), ('TF', 'TransFemale'), ('GF', 'GenderFluid'), ('O', 'Other')], max_length=2)),
                ('notes', models.TextField(blank=True, null=True)),
                ('smoker', models.BooleanField(default=False)),
                ('alcohol', models.BooleanField(default=False)),
                ('drugs', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
