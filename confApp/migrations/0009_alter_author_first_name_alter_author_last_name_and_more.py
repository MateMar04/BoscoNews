# Generated by Django 4.2 on 2023-06-01 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confApp', '0008_alter_image_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='epigraph',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='author',
            field=models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.DO_NOTHING, to='confApp.author'),
        ),
        migrations.AlterField(
            model_name='new',
            name='category',
            field=models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.DO_NOTHING, to='confApp.category'),
        ),
        migrations.AlterField(
            model_name='new',
            name='new_abstract',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='new',
            name='publish_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='new',
            name='subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.TextField(),
        ),
    ]
