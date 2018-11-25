import json
import cherrypy
import requests

LINK = 'https://www.bicing.cat/availability_map/getJsonObject'

class MyOrder(object):
    def order_by_slots(self, dictionary, n=10, rev=True):
        dictionary_sorted = sorted(dictionary, key=lambda entry: int(entry['slots']), reverse=rev)
        return dictionary_sorted[1:n]

class WebServer(object):
    exposed = True

    def GET(self, *uri, **params):
        r = requests.get(LINK)
        print "received uri: ", uri, " ; params: ", params
        if uri[0] == 'slots':
            Order = MyOrder()
            try:
                N = int(params['N'])
                reversion = bool(params['reversion'])
                obj_ordered = Order.order_by_slots(r.json(), N, reversion)
                print "checkpoint"
                return json.dumps(obj_ordered)
            except Exception, e:
                print "error: ", e

if __name__=='__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(WebServer(), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()



