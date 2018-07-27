# Generated by Django 2.0.6 on 2018-06-15 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_post_urlvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('vote', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='urlvote',
        ),
    ]