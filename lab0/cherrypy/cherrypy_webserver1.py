import random
import string
import cherrypy

class StringGeneratorWebService(object):
	exposed = True
	
	def GET (self, some_string = "the user did not pass any string"):
		cherrypy.session['mystring'] = some_string
		return cherrypy.session['mystring']
	
	def POST (self, length=8):
		some_string = ''.join(random.sample(string.hexdigits, int(length)))
		cherrypy.session['mystring'] = some_string
		return some_string
	
	def PUT (self, another_string):
		cherrypy.session['mystring'] = another_string
		return cherrypy.session['mystring']
	
	def DELETE (self):
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
