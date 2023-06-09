# Generated by Django 4.2 on 2023-05-27 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, null=True)),
                ('last_name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, db_column='author', null=True,
                                             on_delete=django.db.models.deletion.DO_NOTHING, to='confApp.author')),
                ('category', models.ForeignKey(blank=True, db_column='category', null=True,
                                               on_delete=django.db.models.deletion.DO_NOTHING, to='confApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to='confApp/news_images')),
                ('epigraph', models.TextField()),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='confApp.new')),
            ],
        ),
    ]
