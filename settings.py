
class Settings():
	
	def __init__(self):
		
		#set screen
		self.screen_width = 1200
		self.screen_height = 750
		self.bg_color = (230,230,230)
		
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		
		self.bullet_speed_factor = 10
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 30
		
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 1
		# if fleet_direction equal to '1',then move right,or move left 
		self.fleet_direction = 1
		
		
