# catalog
import json
import paho.mqtt.client as PahoMQTT
import cherrypy
import time


FILE = "main_catalog.json"


class MyCatalog(object):
    exposed = True

    def __init__(self, filename):
        self.filename = filename

    @cherrypy.tools.json_out()  # substitute json.dumps
    def GET(self, *uri, **params):
        with open(self.filename, 'r') as fp:
            obj = json.loads(fp.read())

        if uri[0] == 'broker':
            # retrive broker
            return obj['broker']
        if uri[0] == 'devices':
            if uri[1] == 'all':
                return obj['devices']
            else:
                try:
                    id = uri[1]
                    print id
                    data = [d for d in obj['devices'] if d['ID'] == id]
                    return data
                except Exception, e:
                    print e
                    raise cherrypy.HTTPError(404, "not found")
        if uri[0] == 'user' and params['id'] == '':
            # retrive broker
            return obj['user']
        else:
            try:
                id = params['id']
                print id
                data = [d for d in obj['user'] if d['id'] == id]
                return data
            except Exception, e:
                print e
                raise cherrypy.HTTPError(404, "not found")

    def POST(self):
        return

    @cherrypy.tools.json_in()
    def PUT(self, *uri, **params):
        with open(self.filename, 'r') as fp_in:
            obj_in = json.loads(fp_in.read())
        try:
            if uri[0] == 'add':
                body = cherrypy.request.json
                obj_add = body

                if uri[1] == 'devices':
                    obj_in['devices'].append(obj_add)
                if uri[1] == 'user':
                    obj_in['user'].append(obj_add)

            with open(self.filename, 'w') as fp_out:
                json.dump(obj_in, fp_out, indent=2)
            cherrypy.response.status(200)
            return "ok"
        except Exception, e:
            print e

    def DELETE(self):
        return


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(MyCatalog(FILE), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8081})
    cherrypy.engine.start()
    cherrypy.engine.block()

    # netstat -ano | findstr :PORTA
    # taskkill /PID PROCESSID /F
    # http://127.0.0.1:8081/user?id=stampantefax
    # http://127.0.0.1:8081/user