import cherrypy
import json

class WebService(object):
    exposed = True

    def GET(self, *uri, **param):
        with open("freeboard/index.html") as fp:
            index = fp.read()
        print uri, param
        return index

    def POST(self, *uri, **params):
        dash = json.loads(params["json_string"])  # Load json object
        with open("./freeboard/dashboard/dashboard.json", "w") as f:
            json.dump(dash, f, indent=2)  # Write json to file
        print uri, params

if __name__=='__main__':
    cherrypy.tree.mount(WebService(), '/', config='server.conf')
    cherrypy.config.update('server.conf')
    cherrypy.engine.start()
    cherrypy.engine.block()

##C:/Users/Ninja/PycharmProjects/Programming4iot/lab2/freeboard a casa
##C:/Users/matte/Documents/PycharmProjects/Programming4iot/lab2/freeboard laptop
