# Generated by Django 4.1.6 on 2023-02-19 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('type', models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='NW', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.category')),
                ('newsThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.news')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='newsCategory',
            field=models.ManyToManyField(through='news_app.NewsCategory', to='news_app.category'),
        ),
    ]
