import os
import socket
import threading
from server.request import RequestObj
from server.response import ResponseObj

class WebServer:
	def __init__(self, host, port):
		#адрес сайта
		self.addr = (host, port)
		#максимальное количество ожидаемых подключений
		self.max_clients = 5
		self.make_sock()
		
	def make_sock(self):
		'''функция для создания сокета сервера'''
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(self.addr)
		self.sock.listen(self.max_clients)
		
	def main_loop(self):
		'''основной цикл обработки клиентских запросов'''
		while True:
			#ожидаем запрос
			conn, addr = self.sock.accept()
			conn.settimeout(60)
			#обрабатываем запрос
			thread = threading.Thread(target = self.handle_client_request, args = (conn,))
			thread.start()
			
			
	def handle_client_request(self, client_connection):
		'''функция для обработки клиентского запроса'''
		#принимаем сообщение от клиента
		try:
			request = client_connection.recv(1024)
		except:
			#в случае если сообщение не было получено за время установленного settimout, закрываем соединение
			client_connection.close()
			return None
		request = request.decode('utf-8')
		#объект запроса клиента
		self.request_obj = RequestObj(request)
		#объект ответа сервера
		self.response_obj = ResponseObj(self.request_obj)
		response = self.response_obj.make_response()
		#передача сообщения клиенту
		client_connection.sendall(response)
		client_connection.close()
