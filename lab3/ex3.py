#!/usr/bin/env python3
"""
@author = Paolo Grasso
"""

import json
import cherrypy
import requests

LINK = 'https://www.bicing.cat/availability_map/getJsonObject'


class WebServer(object):
    exposed = True
    @cherrypy.tools.json_out()

    def GET(self, *uri, **params):
        data = requests.get(LINK)

        if uri[0] == 'slots':

            try:
                N = params['N']
                N = int(N)

                if N < 1:
                    raise exception

            except:
                N = 10

            try:
                ord = params['ord']

                if ord == 'ascend':
                    rev = False

                else:
                    rev = True

            except:
                rev = True

            j = json.loads(data.text)
            j = sorted(j, key = lambda i: int(i['slots']), reverse=rev)
            del j[N:len(j)]

        if uri[0] == 'bikes':
            try:
                N = params['N']
                N = int(N)

                if N < 1:
                    raise exception

            except:
                N = 10

            try:
                ord = params['ord']

                if ord == 'ascend':
                    rev = False

                else:
                    rev = True

            except:
                rev = True

            j = json.loads(data.text)
            j = sorted(j, key = lambda i: int(i['bikes']), reverse=rev)
            del j[N:len(j)]

        if uri[0] == 'zip':

            try:
                zipcode = params['zip-code']

            except:
                raise cherrypy.HTTPError('Zip-code must be specified')

            j = json.loads(data.text)
            j = [x for x in j if x['zip'] == zipcode]

        if uri[0] == 'electric':

            try:
                N = params['N']
                N = int(N)

                if N < 1:
                    raise exception

            except:
                N = 10

            j = json.loads(data.text)
            j = [x for x in j if x['stationType'] == 'ELECTRIC_BIKE']
            j = [x for x in j if int(x['bikes']) >= N]

        if uri[0] == 'count':

            try:
                district = params['district']
                j = json.loads(data.text)
                j = [x for x in j if x['district'] == district]
                bikes = sum([int(x['bikes']) for x in j])
                slots = sum([int(x['slots']) for x in j])
                j = {'district': district,
                     'bikes': str(bikes),
                     'slots': str(slots)}

            except:
                raise cherrypy.HTTPError(404, "Invalid district")

        try:
            return j

        except:
            raise cherrypy.HTTPError(404, "A problem occurred")


    def POST(self):
        pass

    def PUT(self):
        pass

    def DELETE(self):
        pass


if __name__ == '__main__':
    conf = {
        '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount (WebServer(), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()