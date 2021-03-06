from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Player(models.Model):
    GENDER_OPTIONS = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    ident = models.CharField(max_length=15, primary_key=True, verbose_name='Identificacion')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    date_joined = models.DateField(default=datetime.now, verbose_name='Sign Date')
    birth_day = models.DateTimeField(verbose_name='Birth Date')
    address = models.CharField(max_length=150, verbose_name='Address', null=True) 
    description = models.TextField( null=True, verbose_name='Description')
    image = models.ImageField(upload_to='avatars/%Y/%m/%d', null=True, verbose_name='Avatar')
    compet_certificate = models.FileField(upload_to='certifications/%Y/%m/%d', null=True, verbose_name='Competition Certificates')
    active = models.BooleanField(default=True, verbose_name='Active Player')

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        db_table = 'player'
        ordering = ['ident']

    def __str__(self):
        return self.ident


class Telephone(models.Model):
    country_code = models.CharField(max_length=3, verbose_name='Country Code ')
    telephone = models.CharField(max_length=10, verbose_name='Telephone')
    user_id = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Telehone'
        verbose_name_plural = 'Telephones'
        db_table = 'telephone'
        ordering = ['user_id']

    def __str__(self):
        return self.telephone


class Cube(models.Model):
    cube_id = models.AutoField(primary_key=True)
    cube_name = models.CharField(max_length=150, verbose_name='Cube Name')
    cube_image = models.ImageField(null=True, verbose_name='Cube Image', upload_to='cubes/%Y/%m/%d')
    cube_description = models.TextField(null=True, verbose_name='Description')
    users = models.ManyToManyField(Player)

    class Meta:
        verbose_name = 'Cube'
        verbose_name_plural = 'Cubes'
        db_table = 'cube'
        ordering = ['cube_name']

        def __str__(self):
            return self.cube_id

class PlayerReview(Player, Cube):
    """ Create model than containing aal info from other models,
    in DB is a break table from other models"""
    headline = models.CharField(max_length=200)
    date_publication = models.DateField(default=datetime.now)
    abstract = models.TextField(null=True)
    url = models.TextField()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        db_table = 'review'
        ordering = ['headline']

    def __str__(self):
        return self.headline
