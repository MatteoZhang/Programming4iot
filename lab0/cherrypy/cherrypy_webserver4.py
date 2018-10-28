import random
import string
import cherrypy

class StringGeneratorWebService(object):
	exposed = True
	
	def GET (self, *uri, **params):		
		return ("uri: %s; Parameters %s, uri length %s" % (str (uri), str(params), len(uri)))
		
	def POST (self, *uri, **params):
		vector = []
		i = 0
		result = 0
		for key in params:
			vector.append(int(params[key]))
			result += vector[i]
			i += 1
		
		return ("result: %s" % (result))
	
#class Vector():
#	def add_vector ():		
#		return
		
#	def count_element ():
#		return 
		
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