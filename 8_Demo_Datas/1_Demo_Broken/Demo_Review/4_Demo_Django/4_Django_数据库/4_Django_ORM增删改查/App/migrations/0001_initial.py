# Generated by Django 2.2.2 on 2019-08-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=32, verbose_name='学校名称')),
                ('system', models.CharField(max_length=32, verbose_name='院系')),
                ('major', models.CharField(max_length=32, verbose_name='专业')),
                ('teacher_name', models.CharField(max_length=32, verbose_name='老师的名字')),
            ],
        ),
    ]
