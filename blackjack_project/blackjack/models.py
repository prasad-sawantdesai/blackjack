# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GameModel(models.Model):
	player_id = models.CharField(max_length = 10)
	bet  = models.IntegerField(default=0)
	player_total_points = models.IntegerField(default=0)
	dealer_total_points = models.IntegerField(default=0)
	player_winning_status = models.BooleanField(default=False)
	dealer_winning_status = models.BooleanField(default=False)

class Card(models.Model):
	numeric_value = models.IntegerField(default=0)
	suit = models.CharField(max_length = 10)
	game = models.ForeignKey(GameModel)

