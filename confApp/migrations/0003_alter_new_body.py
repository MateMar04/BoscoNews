# Generated by Django 4.2 on 2023-05-29 15:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('confApp', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
