

class GameStats():
	def __init__(self,ai_settings):
		
		"initialize the state information"
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = True
		
	def reset_stats(self):
		self.ship_left = self.ai_settings.ship_limit
		