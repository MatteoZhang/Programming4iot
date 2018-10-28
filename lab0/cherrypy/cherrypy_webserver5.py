import random
import string
import cherrypy

class StringGeneratorWebService(object):
	exposed = True
	
	def GET (self, *uri, **params):		
		return ("uri: %s; Parameters %s, uri length %s" % (str (uri), str(params), len(uri)))
		
	def POST (self, *uri, **params):
		vector1 = Vector(params)
		#return ("vector: %s" % str (vector1.pick()))
		result = vector1.add_v()
		return ("result: %s elements: %s" % ( result, vector1.count_element() ) )
	
class Vector:
	def __init__(self, params):
		self.vector1 = []
		for key in params:
			self.vector1.append(int(params[key]))
		
	def pick(self):
		return self.vector1[0]
		
	def add_v (self):		
		result = 0
		for i in range(len(self.vector1)):
			result += (self.vector1)[i]
		return result
		
	def count_element (self):
		return len(self.vector1)
		
if __name__ == '__main__':
	conf = {
		'/': {
		'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
		'tools.sessions.on': True,
	}
}
cherrypy.tree.mount (StringGeneratorWebService(), '/string', conf)
cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': 9090})
cherrypy.engine.start()
cherrypy.engine.block()