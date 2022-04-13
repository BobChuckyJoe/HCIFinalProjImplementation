# Generated by Django 3.1.5 on 2022-04-13 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coloring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coloring.point')),
            ],
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('paths', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coloring.path')),
            ],
        ),
    ]
