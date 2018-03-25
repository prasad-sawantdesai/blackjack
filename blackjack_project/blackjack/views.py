# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blackjack.models import GameModel
from blackjack.business import Player, Dealer
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
# Create your views here.

def games(request):
	args = {}
	args.update(csrf(request))
	args['games'] = GameModel.objects.all()
	return render_to_response('game_statistics.html', args)

def start_game(request):
	return render_to_response('start_game.html')

def pick_card(request):
	player = request.session['player'] 
	dealer = request.session['dealer']
	if player.player_status == "blackjack":
	    print "Player won!!"
	elif player.player_status == "bust":
	    print "Player loose!!"
	else:
	    #Player deal
		player.get_another_card()
		if player.player_status == "blackjack":
			print "Player won!!"

		elif player.player_status == "bust":
			print "Player loose!!"

	args = {}
	args.update(csrf(request))
	args['player'] = player
	args['dealer'] = dealer
	del request.session['player']
	del request.session['dealer']
	request.session['player'] = player
	request.session['dealer'] = dealer
	player_win_stat = False
	dealer_win_stat = False
	if player.player_status == "blackjack" or dealer.player_status == "bust" or player.player_status == "won" :
		player_win_stat = True
	if player.player_status == "bust" or dealer.player_status == "blackjack" or dealer.player_status == "won":
		dealer_win_stat = True

	if player_win_stat == True or dealer_win_stat == True:
		obj = GameModel(player_id=player.player_id, 
						bet=player.bet,
						player_total_points=player.total_points,
						dealer_total_points=dealer.total_points,
						player_winning_status=player_win_stat,
						dealer_winning_status=dealer_win_stat)
		obj.save()
	return render_to_response('game_play.html', args)

def skip(request):
	player = request.session['player'] 
	dealer = request.session['dealer']
	player.player_status = "stand"

	print "django " + player.player_status
	if player.player_status == "stand":
		while dealer.total_points <= 16:
			dealer.get_another_card()
			if dealer.player_status == "blackjack":
				print "Dealer won!!"   
			elif dealer.player_status == "bust":
				print "Player won!!" 

	if player.player_status == "stand" and dealer.player_status == "playing":
		if player.total_points > dealer.total_points:
			player.player_status = "won"
			print "Player won"
		elif  player.total_points < dealer.total_points:  
			dealer.player_status = "won" 
			print "Dealer won"
		else:
			print "Tie"

	args = {}
	args.update(csrf(request))
	args['player'] = player
	args['dealer'] = dealer
	del request.session['player']
	del request.session['dealer']
	request.session['player'] = player
	request.session['dealer'] = dealer

	player_win_stat = False
	dealer_win_stat = False
	if player.player_status == "blackjack" or dealer.player_status == "bust" or player.player_status == "won" :
		player_win_stat = True
	if player.player_status == "bust" or dealer.player_status == "blackjack" or dealer.player_status == "won":
		dealer_win_stat = True
	if player_win_stat == True or dealer_win_stat == True:
		obj = GameModel(player_id=player.player_id, 
						bet=player.bet,
						player_total_points=player.total_points,
						dealer_total_points=dealer.total_points,
						player_winning_status=player_win_stat,
						dealer_winning_status=dealer_win_stat)
		obj.save()

	return render_to_response('game_play.html', args)

def play_game(request):
	player = Player(1, 1000)
	dealer = Dealer(0, 1000)
	args = {}
	args.update(csrf(request))
	args['player'] = player
	args['dealer'] = dealer
	request.session['player'] = player
	request.session['dealer'] = dealer
	return render_to_response('game_play.html', args)

