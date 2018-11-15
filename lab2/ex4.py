import cherrypy

class WebService(object):
    exposed = True

    def GET(self, *uri, **param):
        with open("./freeboard/index.html") as fp:
            index = fp.read()
        return index

if __name__=='__main__':
    cherrypy.tree.mount(WebService(), '/', config='server.conf')
    cherrypy.config.update('server.conf')
    cherrypy.engine.start()
    cherrypy.engine.block()
