# Generated by Django 4.0.2 on 2022-04-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0035_alter_submittedtask_task_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='about',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
