import SimpleHTTPServer
import SocketServer
import os
import urllib2

PORT = int(os.getenv('PORT', 8080))
SERVICE = os.getenv('SERVICE', None)
PARAMETER = os.getenv('PARAMETER', None)

class my_handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      result  = "<b>HOSTNAME:</b> " + os.environ.get('HOSTNAME') + " - " + PARAMETER
      if SERVICE is not None:
        result += "<br/><b>Consumindo servico:</b> "+SERVICE+"<br/>" + urllib2.urlopen(SERVICE).read()
      self.wfile.write(result)
      return

try:
   httpd = SocketServer.ThreadingTCPServer(('', PORT), my_handler)
   print "servidor web rodando na porta ", PORT
   httpd.serve_forever()

except KeyboardInterrupt:
   print "Voce pressionou ^C, encerrando..."
   httpd.socket.close()
