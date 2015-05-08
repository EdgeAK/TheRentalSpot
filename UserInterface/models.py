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

class GameGenre(models.Model):
    game_genre_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Game_Genre'
    
class MovieGenre(models.Model):
    movie_genre_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Movie_Genre'

class Star(models.Model):
    star_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'Star'


#class GameHasGenre(models.Model):
#    game_game_media = models.ForeignKey(Game, db_column='GAME_game_media_id')  # Field name made lowercase.
#    game_genre_game_genre = models.ForeignKey('GameGenre', db_column='Game_Genre_game_genre_id')  # Field name made lowercase.
#
#    class Meta:
#        managed = False
#        db_table = 'GAME_has_Genre'





class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    platform = models.CharField(max_length=10)
    cover_img = models.TextField()
    esrb = models.CharField(max_length=10)
    cust_rating = models.IntegerField(default=0)
    date_rented = models.DateField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'MEDIA'


class Movie(models.Model):
    movie_media = models.ForeignKey(Media, primary_key=True)
    director = models.ManyToManyField(Director)
    star = models.ManyToManyField(Star)
    genre = models.ManyToManyField(MovieGenre) 
    runtime = models.TimeField()

    class Meta:
        managed = False
        db_table = 'MOVIE'
    pass

class Game(models.Model):
    game_media = models.ForeignKey('Media', primary_key=True)
    genre = models.ManyToManyField(GameGenre)
    no_players = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'GAME'
    pass


#class MovieHasDirector(models.Model):
#    movie_movie_media = models.ForeignKey(Movie, db_column='MOVIE_movie_media_id')  # Field name made lowercase.
#    director_director = models.ForeignKey(Director, db_column='Director_director_id')  # Field name made lowercase.
#
#    class Meta:
#        managed = False
#        db_table = 'MOVIE_has_Director'


#class MovieHasGenre(models.Model):
#    movie_movie_media = models.ForeignKey(Movie, db_column='MOVIE_movie_media_id')  # Field name made lowercase.
#    movie_genre_movie_genre = models.ForeignKey('MovieGenre', db_column='Movie_Genre_movie_genre_id')  # Field name made lowercase.
#
#    class Meta:
#        managed = False
#        db_table = 'MOVIE_has_Genre'


#class MovieHasStar(models.Model):
#    movie_movie_media = models.ForeignKey(Movie, db_column='MOVIE_movie_media_id')  # Field name made lowercase.
#    star_star = models.ForeignKey('Star', db_column='Star_star_id')  # Field name made lowercase.
#
#    class Meta:
#        managed = False
#        db_table = 'MOVIE_has_Star'





class Renter(models.Model):
    renter_id = models.IntegerField(primary_key=True)
    media = models.ManyToManyField(Media)
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
    pass


#class RenterHasMedia(models.Model):
#    renter = models.ForeignKey(Renter, primary_key=True)
#    media = models.ForeignKey(Media)
#    date_rented = models.DateField()
#
#    class Meta:
#        managed = False
#        db_table = 'RENTER_has_MEDIA'



