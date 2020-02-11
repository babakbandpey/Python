#!/usr/bin/python3

import http.server
import socketserver
import glob
import random
import sys

from pathlib import Path

class Server(http.server.SimpleHTTPRequestHandler):

	def log_message(self, format, *args):
		file_object = open("log.txt", "a+")
		file_object.write("%s - - [%s] %s\n"%(self.client_address[0], self.log_date_time_string(), format%args))
		file_object.close()

	def do_GET(self):
		print(self.headers)
		file_path = Path(self.path).name
		if file_path == "":
			file_path = "index.html"
		try:
			file_object = open(file_path)
			contents = file_object.read()

			self.protocol_version='HTTP/1.1'
			self.send_response(200, 'OK')
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes(contents, 'UTF-8'))
			file_object.close()
		except IOError:
			self.protocol_version='HTTP/1.1'
			self.send_response(404, 'Not Found')
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes("Not found", 'UTF-8'))

		print("Path: ", Path(self.path).name)

	def serve_forever(port):
		socketserver.TCPServer(('', port), Server).serve_forever()

if __name__ == "__main__":
	Server.serve_forever(8000)
