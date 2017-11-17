#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alien_invasion.py
#  
#  Copyright 2017 admin <admin@DESKTOP-4OVNDA4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Alien import Alien
from game_stats import GameStats
def run_game():
	#initialize
	pygame.init()
	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	
	pygame.display.set_caption("Alien Invasion")
	
	#reate a example of game state
	stats = GameStats(ai_settings)
	
		
	#create a group of bullets,aliens and a ship
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		
		if stats.game_active:
			
			ship.update()
			
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
					
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		



run_game()


































