# Generated by Django 3.1.13 on 2021-12-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=20)),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=200, unique=True)),
                ('Phone', models.CharField(max_length=30)),
                ('Married', models.BooleanField(default=False)),
                ('Dependents', models.IntegerField()),
                ('Education', models.CharField(choices=[('GRADUTE', 'GRADUTE'), ('NOTGRADUATE', 'NOTGRADUATE')], max_length=20)),
                ('Self_Employed', models.BooleanField(default=False)),
                ('ApplicantIncome', models.IntegerField()),
                ('CoapplicantIncome', models.IntegerField()),
                ('LoanAmount', models.IntegerField()),
                ('Loan_Amount_Term', models.IntegerField()),
                ('Credit_History', models.BooleanField(default=False)),
                ('Property_Area', models.CharField(choices=[('URBAN', 'URBAN'), ('RURAL', 'RURAL'), ('SEMIURBAN', 'SEMIURBAN')], max_length=20)),
            ],
        ),
    ]
