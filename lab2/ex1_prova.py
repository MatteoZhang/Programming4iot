import random
import string
import cherrypy
import json

class OP:
    def Add(self, a, b):
        try:
            c = a + b
        except Exception, e:
            print "invalid input"
        return c
    def Sub(self, a, b):
        try:
            c = a - b
        except Exception, e:
            print "invalid input"
        return c
    def Div(self, a, b):
        try:
            c = a/b
        except Exception, e:
            print "invalid input division by 0"
            c = "not valid"
        return c
    def Mul(self, a, b):
        try:
            c = a * b
        except Exception, e:
            print "invalid input"
        return c

class WebService(object):
    exposed = True

    def GET(self, *uri, **params):
        op = uri[0]
        a = int(params['op1'])
        b = int(params['op2'])
        result = OP()
        r = 0
        d = {}
        if uri[0] == 'add':
            r = result.Add(a, b)
        elif uri[0] == 'sub':
            r = result.Sub(a, b)
        elif uri[0] == 'div':
            r = result.Div(a, b)
        else:
            r = result.Mul(a, b)
            d["result"] = r
            d["operation"] = uri[0]
            d["op1"] = a
            d["op2"] = b
            c = json.dumps(d, indent=4)
        return c


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
cherrypy.tree.mount(WebService(), '/op', conf)
cherrypy.config.update({'server.socket_host': '127.0.0.1'})
cherrypy.config.update({'server.socket_port': 8080})
cherrypy.engine.start()
cherrypy.engine.block()
