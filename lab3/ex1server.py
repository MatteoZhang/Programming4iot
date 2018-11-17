import cherrypy
import json
from asset.calculator import OP


class WebService(object):
    exposed = True


    def GET(self, *uri, **params):
        a = float(params['op1'])
        b = float(params['op2'])
        operation = str(uri[0])
        dictionary = {}
        result = OP()
        if operation == 'add':
            r = result.Add(a, b)
        elif operation == 'sub':
            r = result.Sub(a, b)
        elif operation == 'mul':
            r = result.Mul(a, b)
        elif operation == 'div':
            r = result.Div(a, b)
        else:
            print "wrong url"
        dictionary['result'] = r
        dictionary['op1'] = a
        dictionary['op2'] = b
        dictionary['operation'] = operation
        print dictionary
        print "uri: %s; Parameters %s, uri length %s" % (str(uri), str(params), len(uri))
        return json.dumps(dictionary)

if __name__=='__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(WebService(), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8081})
    cherrypy.engine.start()
    cherrypy.engine.block()

## usare r = requests.get('http://localhost:8081/add?op1=0&op2=1')
## r.txt
