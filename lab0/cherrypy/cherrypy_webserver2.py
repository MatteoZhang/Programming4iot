import random
import string
import cherrypy

class StringGeneratorWebService(object):
	mystring = "initial string"
	exposed = True
	
	def GET (self, *uri, **params):		
		return ("uri: %s; Parameters %s, uri length %s" % (str (uri), str(params), len(uri)))
		
	def POST (self, *uri, **params):
		my_string = "POST RESPONSE: "
		my_string += cherrypy.request.body.read()
		return my_string
			
	def PUT (self, *uri, **params):
		#cherrypy.session['mystring'] = str (uri) 
		cherrypy.session['mystring'] = str (StringGeneratorWebService.mystring)
		return cherrypy.session['mystring']
	
	def DELETE (self, *uri, **params):
		cherrypy.session.pop('mystring', None)
		
if __name__ == '__main__':
	conf = {
		'/': {
		'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
		'tools.sessions.on': True,
	}
}
cherrypy.tree.mount (StringGeneratorWebService(), '/string', conf)
cherrypy.config.update({'server.socket_host': '127.0.0.1'})
cherrypy.config.update({'server.socket_port': 9090})
cherrypy.engine.start()
cherrypy.engine.block()
