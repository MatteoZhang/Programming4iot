import random
import string
import cherrypy
import json
from op import *


class StringGeneratorWebService(object):
	exposed = True
	
	def GET (self, *uri, **params):		
		return ("uri: %s; Parameters %s, uri length %s" % (str (uri), str(params), len(uri)))
		
if __name__ == '__main__':
	conf = {
		'/': {
		'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
		'tools.sessions.on': True,
	}
}
cherrypy.tree.mount (StringGeneratorWebService(), '/string', conf)
cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': 8080})
cherrypy.engine.start()
cherrypy.engine.block()