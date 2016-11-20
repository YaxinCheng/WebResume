class Manager:
	def __init__(self):
		self.is_authenticated = True
		self.is_active = True
		self.is_anonymous = False
	
	def get_id(self):
		return 'ycheng'

	@staticmethod
	def get(user_id):
		return Manager()
	

