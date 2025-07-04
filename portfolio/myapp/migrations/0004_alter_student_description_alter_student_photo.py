# Generated by Django 5.2.3 on 2025-06-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_student_contactno_student_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="description",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.ImageField(upload_to="student_photos/"),
        ),
    ]
