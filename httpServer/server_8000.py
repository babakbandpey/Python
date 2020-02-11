#!/usr/bin/python3

import http.server
import socketserver
import glob
import random
import sys

class Server(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		print(self.headers)
		referer = self.headers.get('Referer')
		print("The referer is", referer)
		if referer == None:
			self.protocol_version='HTTP/1.1'
			self.send_response(200, 'OK')
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes("", 'UTF-8'))
			images = glob.glob('*.jpg')
			rand = random.randint(0,len(images)-1)
			filepath = images[rand]
#			imagestring = "<img src = \"" + images[rand] + "\" height = 1028 width = 786 align = \"right\"/> </body> </html>"
#			self.wfile.write(bytes(imagestring, 'UTF-8'))
		else:
			imgname = self.path
			print ("Image requested is: ", imgname[1:])
			imgfile = open(imgname[1:], 'rb').read()
			self.send_header('Content-type', 'image/jpeg')
			self.send_header('Content-length', sys.getsizeof(imgfile))
			self.end_headers()
			self.wfile.write(imgfile)

	def serve_forever(port):
		socketserver.TCPServer(('', port), Server).serve_forever()

if __name__ == "__main__":
	Server.serve_forever(8000)
