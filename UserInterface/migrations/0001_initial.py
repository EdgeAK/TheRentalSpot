# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('director_id', models.AutoField(serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Director',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('game_genre_id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Game_Genre',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('media_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('platform', models.CharField(max_length=10)),
                ('cover_img', models.TextField()),
                ('esrb', models.CharField(max_length=10)),
                ('cust_rating', models.IntegerField(default=0)),
                ('date_rented', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'MEDIA',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_media', models.ForeignKey(primary_key=True, serialize=False, to='UserInterface.Media')),
                ('no_players', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'GAME',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_media', models.ForeignKey(primary_key=True, serialize=False, to='UserInterface.Media')),
                ('runtime', models.TimeField()),
            ],
            options={
                'db_table': 'MOVIE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('movie_genre_id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Movie_Genre',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('renter_id', models.IntegerField(serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('credit_card_num', models.CharField(unique=True, max_length=16)),
                ('street_add', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'RENTER',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('star_id', models.AutoField(serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Star',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
