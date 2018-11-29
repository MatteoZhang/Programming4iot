import json
import cherrypy
import requests

LINK = 'https://www.bicing.cat/availability_map/getJsonObject'

class MyOrder(object):
    def order_by_par(self, dictionary, n=10, rev=True, par):
        dictionary_sorted = sorted(dictionary, key=lambda entry: int(entry[par]), reverse=rev)
        return dictionary_sorted[1:n]

class WebServer(object):
    exposed = True

    def GET(self, *uri, **params):
        r = requests.get(LINK)
        print "received uri: ", uri, " ; params: ", params
        if uri[0] == 'slots':
            try:
                par = uri[0]
                N = int(params['N'])
                reversion = bool(params['reversion'])
                Order = MyOrder()
                obj_ordered = Order.order_by_par(r.json(), N, reversion, par)
                return json.dumps(obj_ordered)
            except Exception, e:
                print "error: ", e
        if uri[0] == 'bikes':
            try:
                par = uri[0]
                N = int(params['N'])
                reversion = bool(params['reversion'])
                Order = MyOrder()
                obj_ordered = Order.order_by_par(r.json(), N, reversion, par)
                return json.dumps(obj_ordered)
            except Exception, e:
                print "error: ", e
        # matches = [x for x in lst if fulfills_some_condition(x)] 
        # https://stackoverflow.com/questions/9542738/python-find-in-list
		if uri[0] == 'zip':
            try:
                zipcode = params['zipcode']
            except Exception, e:
                print "error: ", e
                print "zipcode must be specified try /zip?zipcode=08025"
            matches = r.json()
            matches = [x for x in lst if x['zip'] == zipcode]
            return json.dumps(matches)
        if uri[0] == 'ELECTRIC_BIKE':
            try:
                N = int(params['N'])
            except Exception, e:
                print "optional parameter not found"
                N = 10
            matches = r.json()
            matches = [x for x in matches if x['stationType'] == uri[0]] 
            matches = [x for x in matches if int(x['bikes']) >= N]
            return json.dumps(matches)

        if uri[0] == 'count':
            try:
                district = params['district']
                matches = r.json()
                matches = [x for x in matches if x['district'] == district]
                bikes = sum([int(x['bikes']) for x in matches])
                slots = sum([int(x['slots']) for x in matches])
                matches = {'district': district, 'bikes': str(bikes), 'slots': str(slots)}
            except:
                raise cherrypy.HTTPError(404, "Invalid district")
            return json.dump(matches)

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
