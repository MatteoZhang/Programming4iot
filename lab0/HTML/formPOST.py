import cherrypy

class Generator(object):
	@cherrypy.expose

	def hello (self, *uri, ** params):
		return open('./hello/hello_form.html','r').read()
		
	#hello.exposed = True
				
	def reply (self, *uri, ** params):
		return open('./hello/page.html','r').read()
		
	reply.exposed = True

if __name__	== '__main__':
	cherrypy.quickstart(Generator(), '/')
