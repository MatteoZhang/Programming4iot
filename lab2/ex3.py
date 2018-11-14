import cherrypy

class WebService(object):
    exposed = True

    def GET(self, *uri, **param):
        with open("freeboard\index.html") as fp:
            index = fp
        return fp

if __name__=='__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(WebService(), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8082})
    cherrypy.engine.start()
    cherrypy.engine.block()