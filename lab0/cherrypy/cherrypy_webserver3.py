import random
import string
import cherrypy

class StringGeneratorWebService(object):
	exposed = True
	
	def GET (self, *uri, **params):		
		return ("uri: %s; Parameters %s, uri length %s" % (str (uri), str(params), len(uri)))
		
	def POST (self, *uri, **params):
		
		if uri[0] == "add":
			operation = "+"
			result = int(params['first']) + int(params['second'])
		else:
			operation  = "-"
			result = int(params['first']) - int(params['second'])
		return ("performed %s %s %s = %s" % (params['first'], operation, params['second'], result)) 
		
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