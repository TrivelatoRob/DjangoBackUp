# Generated by Django 5.1.3 on 2024-11-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0003_courses_alter_student_courses'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='courses.courses'),
        ),
    ]