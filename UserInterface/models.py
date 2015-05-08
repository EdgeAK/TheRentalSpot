# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Director(models.Model):
    director_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'Director'


class Game(models.Model):
    media = models.ForeignKey('Media', primary_key=True)
    no_players = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'GAME'


class GameHasGenre(models.Model):
    media = models.ForeignKey(Game)
    game_genre = models.ForeignKey('GameGenre')

    class Meta:
        managed = False
        db_table = 'GAME_has_Genre'


class GameGenre(models.Model):
    game_genre_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Game_Genre'


class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    platform = models.CharField(max_length=10)
    cover_img = models.TextField()
    esrb = models.CharField(max_length=10)
    cust_rating = models.IntegerField()
    date_rented = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MEDIA'


class Movie(models.Model):
    media = models.ForeignKey(Media, primary_key=True)
    runtime = models.TimeField()

    class Meta:
        managed = False
        db_table = 'MOVIE'


class MovieHasDirector(models.Model):
    media = models.ForeignKey(Movie, primary_key=True)
    director = models.ForeignKey(Director)

    class Meta:
        managed = False
        db_table = 'MOVIE_has_Director'


class MovieHasGenre(models.Model):
    media = models.ForeignKey(Movie)
    movie_genre = models.ForeignKey('MovieGenre')

    class Meta:
        managed = False
        db_table = 'MOVIE_has_Genre'


class MovieHasStar(models.Model):
    media = models.ForeignKey(Movie)
    star = models.ForeignKey('Star')

    class Meta:
        managed = False
        db_table = 'MOVIE_has_Star'


class MovieGenre(models.Model):
    movie_genre_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Movie_Genre'


class Renter(models.Model):
    renter_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    dob = models.DateField()
    email = models.CharField(max_length=30)
    credit_card_num = models.CharField(unique=True, max_length=16)
    street_add = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'RENTER'


class RenterHasMedia(models.Model):
    renter = models.ForeignKey(Renter)
    media = models.ForeignKey(Media)

    class Meta:
        managed = False
        db_table = 'RENTER_has_MEDIA'


class Star(models.Model):
    star_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'Star'
