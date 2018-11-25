import cherrypy
import json
from datetime import datetime

class DiscoManager(object):
    def __init__(self, data):
        self.data = data

    def search_album(self, inst):
        try:
            dictionary = []
            for albums in self.data["album_list"]:
                if inst in [albums["title"], albums["artist"]]:
                    dictionary.append(albums)
        except Exception, e:
            print "not found the ", inst, " -- due to error: ", e
        return dictionary

    def search_album2(self, inst):
        try:
            dictionary = []
            for albums in self.data["album_list"]:
                if inst in [albums["publication_year"], albums["total_tracks"]]:
                    dictionary.append(albums)
        except Exception, e:
            print "not found the ", inst, " -- due to error: ", e
        return dictionary

class WebService(object):
    exposed = True

    def GET(self, *uri, **params):
        print "received uri: ", uri, "params: ", params
        try:
            with open("asset/discography.json", 'r') as disco:
                data = json.load(disco)
            if uri[0] == 'print_all':
                return json.dumps(data)
            elif uri[0] == 'search_by_artist' or 'search_by_title':
                operation = DiscoManager(data)
                dictionary = operation.search_album(uri[1])
                return json.dumps(dictionary)
            elif uri[0] == 'search_by_pub_year' or 'search_by_tot_tracks':
                operation = DiscoManager(data)
                dictionary = operation.search_album2(int(uri[1]))
                return json.dumps(dictionary)
        except Exception, e:
            print 'wrong get request: ', e
    def POST(self, *uri, **params):
        # create something
        pass
    def PUT(self, *uri, **params):
        # manipulate what u have already
        print "received uri: ", uri, "params: ", params
        try:
            if uri[0] == 'insert_new':
                with open("asset/discography.json", 'r') as disco:
                    data = json.load(disco)
                new_entry = {"total_tracks": int(params['tracks']), "artist": params['artist'],
                             "publication_year": int(params['year']), "title": params['album']}
                data['album_list'].append(new_entry)
                now = datetime.now().strftime("%Y-%B-%d ,%I:%M%p")
                data['last_update'] = now
                with open("asset/discography.json", 'w') as disco:
                    json.dump(data, disco, indent=2)
                return json.dumps(data)
        except Exception, e:
            print 'wrong put request ', e
    def DELETE(self, *uri, **params):
        try:
            print "received uri: ", uri, "params: ", params
            if uri[0] == 'delete':
                with open("asset/discography.json", 'r') as disco:
                    data = json.load(disco)
                op = DiscoManager(data)
                dictionary = op.search_album(params['album'])
                del data['album_list'][dictionary]
        except Exception, e:
            print "error: ", e, "\n"
        pass

if __name__=='__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(WebService(), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8085})
    cherrypy.engine.start()
    cherrypy.engine.block()

# netstat -ano | findstr :PORTA
# taskkill /PID PROCESSID /F

