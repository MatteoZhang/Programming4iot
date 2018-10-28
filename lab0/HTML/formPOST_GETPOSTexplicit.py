import cherrypy

class Generator(object):

	def index (self, *uri, ** params):
		return '''<form action="reply" method="POST">
		Enter some text:<br />
		<textarea name="seq" rows="10" cols="80" /></textarea><br />
		<input type="submit" />
		</form>
        '''
	index.exposed = True

						
	def reply (self, *uri, ** params):
		return open('./hello/page.html','r').read()

	reply.exposed = True
		
if __name__	== '__main__':
	#cherrypy.quickstart(Generator(), '/')
	cherrypy.tree.mount (Generator(),	'/')
	cherrypy.engine.start()
	cherrypy.engine.block()
