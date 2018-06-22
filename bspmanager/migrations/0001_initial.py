# Generated by Django 2.0.6 on 2018-06-21 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('emailAddress', models.EmailField(blank=True, editable=False, max_length=50, null=True)),
                ('TaskDESC', models.TextField(blank=True, null=True)),
                ('EmployeeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskCategory', models.CharField(choices=[('PRE', 'Presales'), ('PJT', 'Project'), ('OTH', 'Others')], max_length=50)),
                ('TaskName', models.CharField(max_length=50)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('SalesDepartment', models.CharField(blank=True, choices=[('Azure', 'Azure'), ('AWS', 'Amazon Cloud Service'), ('PM', 'Project Manager'), ('PMO', 'Project Manager Operation'), ('CDP', 'Cloud Data ')], max_length=50, null=True)),
                ('SalesRepresentative', models.CharField(blank=True, max_length=50, null=True)),
                ('Remarks', models.TextField(blank=True, null=True)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('TaskID', models.EmailField(blank=True, editable=False, max_length=50, null=True, verbose_name='Task ID')),
                ('TaskOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='TaskName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bspmanager.TaskMaster'),
        ),
    ]