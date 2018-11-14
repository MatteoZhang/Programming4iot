
import cherrypy
from asset.calculatorV import OP
import json


class WebService(object):
    exposed = True

    class HelloWorld(object):
        @cherrypy.expose
        def index(self):
            return "Hello world!"

    def PUT(self, *uri, **params):
        data = json.loads(cherrypy.request.body.read())  # Read body data
        calculator = OP()
        if data["command"] == "add":
            result = calculator.Add(data["operands"])
        elif data["command"] == "sub":
            result = calculator.Sub(data["operands"])
        elif data["command"] == "div":
            result = calculator.Div(data["operands"])
        elif data["command"] == "mul":
            result = calculator.Mul(data["operands"])
        else:
            print "invalid input"

        dictionary = data
        dictionary["result"] = result
        return json.dump(dictionary)


if __name__=='__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(WebService(), '/operation', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.engine.start()
    cherrypy.engine.block()

"""
PUT request on Postman:
0.0.0.0:8080/operation
raw body in the body section
{"command": "add","operands": [10, 9, 8, 5, 3, 2, 1]}
"""