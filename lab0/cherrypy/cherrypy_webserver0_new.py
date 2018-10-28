import random
import cherrypy
import string

class StringGenerator(object):
	@cherrypy.expose
	def index(self):
		return "Hello world!"

	@cherrypy.expose
	def generate(self):
		return ''.join(random.sample(string.hexdigits, 8))
	
if __name__ == '__main__':
	cherrypy.tree.mount (StringGenerator())
	cherrypy.config.update({'server.socket_port': 9090})
	cherrypy.engine.start()
	cherrypy.engine.block()
