import os
from settings.urls import urls
from settings.settings import TEMPLATES, STATIC

class ResponseObj:
	''' Объект для создания ответа сервера'''
	def __init__(self, request_obj):
		self.request = request_obj
		self.validate_path()
		
	def validate_path(self):
		'''функция проверки существования запрошенного url'''	
		if (self.request.message_correct) and (self.request.path in urls):
			#если запрошенный путь находится в url
			self.path_to_file = os.path.join(TEMPLATES, urls[self.request.path])
			self.ext_file = 'html'
			self.headers = "Content-Type: text/html; charset=utf-8\n"
			self.status = True
			return True
		else:	
			try:	
				#определяем путь к директории, название файла и его разширение, если был запрошен файл					
				dir_path, request_file, ext_file = self.parse_path(self.request.path)
				if ext_file in ['css', 'js', 'png', 'jpeg', 'jpg', 'gif']:
					#определяем полный путь к директории и извлекаем список файлов
					full_static_path = os.path.join(STATIC, dir_path)
					list_files = os.listdir(full_static_path)					
					if request_file in list_files:
						#если файл присутствует в директории, определяем его полный путь
						self.path_to_file = os.path.join(STATIC, dir_path, request_file)						
						self.content_type(ext_file)
						self.status = True
						return True
				self.status = False
				return False
			except:
				#если запрошенный путь не является файлом
				self.status = False
				return False
				
	def parse_path(self, path_to_file):
		''' Функция для парсинга запрошенного пути'''
		dir_path = '/'.join(path_to_file.split('/')[1:-1])
		file_name = path_to_file.split('/')[-1]
		ext_file = file_name.split('.')[-1]
		self.ext_file = ext_file
		return dir_path, file_name, ext_file
		
	def content_type(self, ext_file):
		''' Функция для определения в заголовках типа возвращаемого значения файла'''
		if ext_file in ['css', 'js']:
			self.headers = "Content-Type: text/{0}; charset=utf-8\n".format(ext_file)
		elif ext_file in ['png', 'jpeg', 'jpg', 'gif']:
			self.headers = "Content-Type: image/{0}\n".format(ext_file)
	
	def built_headers(self):
		'''функция для первоначального заполнения заголовка ответа'''
		if self.status:
			self.headers = "HTTP/1.1 200 OK\n"
			return True
		else:
			if not self.request.message_correct:
				self.headers = "HTTP/1.1 400 Bad Request\n"
			else:
				self.headers = "HTTP/1.1 404 Not Found\n"
			return False
	
	def make_response(self):
		'''функция для создания http-ответа'''
		if self.built_headers():
			with open(self.path_to_file, 'rb') as main_page:
				data = main_page.read()						
			self.headers += "Content-Length: {0}\n\n".format(len(data))			
			http_response = bytes(self.headers, 'utf-8')+data
		else:
			if self.request.message_correct:
				data = "<html><body>Page not found</body></html>"
			else:
				data = "<html><body>Check the correctness of the request</body></html>"
			self.headers += "Content-Type: text/html; charset=utf-8\nContent-Length: {0}\n\n".format(len(data))
			http_response = self.headers + data
			http_response = bytes(http_response, 'utf-8')
		return http_response
