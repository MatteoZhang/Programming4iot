import cherrypy
import os.path

class FirstServer:
    def index(self):
        output = '''
        Hello Form <a href="hello">hi<a><br>
        <form action = "inputHere" method = "GET"> 
        Enter anything inp is my var
        <input type = "text" inp="inp">
        <input type = "submit">
        </form>
        '''
        return output
    index.exposed = True
    def hello(self):
        output = '''
        Hi there
        '''
    hello.exposed = True

    def inputHere(self, inp=None):
        output = '''
        ur input %s
        ''' % inp
        return output
    inputHere.exposed = True

configfile = os.path.join(os.path.dirname(__file__),'server.conf')
cherrypy.quickstart(FirstServer(), config=configfile)
