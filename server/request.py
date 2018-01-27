class RequestObj:
	'''Объект пользовательского запроса'''
	def __init__(self, client_message):
		#текстовое сообщение клиента
		self.message = client_message
		self.message_correct = False
		self.parse_request()
		
		
	def parse_request(self):
		#парсим первую строку сообщения
		if self.message:
			#определяем метод, путь и версию http
			try:
				self.method, self.path, self.http_version = self.message.split('\n')[0].split(' ')
				self.message_correct = True
			except:
				self.message_correct = False
