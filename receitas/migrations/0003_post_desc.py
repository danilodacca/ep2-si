# Generated by Django 4.2.7 on 2023-11-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_post_alter_review_movie_delete_receita'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.CharField(default='valor temporário', max_length=1000),
        ),
    ]
