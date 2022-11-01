# Generated by Django 3.1.2 on 2022-11-01 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(verbose_name='Главная тема')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.theme')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='theme',
            field=models.ManyToManyField(through='articles.Relations', to='articles.Theme'),
        ),
    ]
