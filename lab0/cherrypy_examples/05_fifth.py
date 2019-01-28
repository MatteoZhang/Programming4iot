import random
import string
import cherrypy


class StringGeneratorWebService(object):
    exposed = True

    def GET(self, *uri, **params):
        return ("URI: %s; Parameters %s" % (str(uri), str(params)))

    def POST(self, *uri, **params):
        mystring = "POST RESPONSE\n"
        mystring += ("URI: %s; Parameters %s\n" % (str(uri), str(params)))
        mystring += ("BODY: %s" % cherrypy.request.body.read())
        return mystring

    def PUT(self, *uri, **params):
        mystring = "PUT RESPONSE\n"
        mystring += ("URI: %s; Parameters %s\n" % (str(uri), str(params)))
        mystring += ("BODY: %s" % cherrypy.request.body.read())
        return mystring

    def DELETE(self):
        pass


class OtherWebService(object):
    exposed = True

    def GET(self):
        return "this is the other web service!"

    def POST(self, length=8):
        # do something
        pass

    def PUT(self, another_string):
        # do something
        pass

    def DELETE(self):
        # do something
        pass


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(StringGeneratorWebService(), '/string', conf)
    cherrypy.tree.mount(OtherWebService(), '/other', conf)

    cherrypy.config.update({'server.socket_host': '127.0.0.1'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
