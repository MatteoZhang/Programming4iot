import cherrypy
import json
from datetime import datetime

class DiscoManager(object):
    def __init__(self, data):
        self.data = data
        self.feature = data.keys()
        self.fnested = data["album_list"]  # array
        self.subfeature = self.fnested[0].keys()  # one of the album keys
        self.len = len(self.feature)
        self.lensub = len(self.fnested)
    def searchAlbum(self, inst):
        try:
            dictionary = {}
            for i in range(self.lensub):
                for field in self.subfeature:
                    value = self.fnested[i][field]
                    if value == inst:
                        print "printing %s related things:" % inst
                        print "\n----"
                        for entry in self.subfeature:
                            dictionary[entry] = self.data["album_list"][i][entry]
                        print "----\n"
            return dictionary
        except Exception, e:
            print "not found the ", inst

class WebService(object):
    exposed = True

    def GET(self, *uri, **params):
        list = ["search_by_artist",
                "search_by_title",
                "search_by_pub_year",
                "search_by_tot_tracks",
                "insert_new",
                "print_all",
                "exit"]
        outp={}
        with open("asset/discography.json") as disco:
            data = json.load(disco)
        if uri[0] == "print_all":
            return data
        elif uri[0] == list[0]:
            op = DiscoManager(data)
            outp=op.searchAlbum(uri[1])
        elif uri[0] == list[1]:
            op = DiscoManager(data)
            outp=op.searchAlbum(uri[1])
        elif uri[0] == list[2]:
            op = DiscoManager(data)
            outp=op.searchAlbum(uri[1])
        elif uri[0] == list[3]:
            op = DiscoManager(data)
            outp=op.searchAlbum(uri[1])
        else:
            print "not valid input"
        return outp

    def POST(self, *uri, **params):
        if uri[0] == 'insert_new':
            with open("asset/discography.json") as disco:
                data = json.load(disco)
            new_entry = {"total_tracks": int(params['tracks']), "artist": params['artist'],
                         "publication_year": int(params['year']), "title": params['album']}
            data['album_list'].append(new_entry)
            now = datetime.now().strftime("%Y-%B-%d ,%I:%M%p")
            data['last_update'] = now
            return data
    def PUT(self, *uri, **params):
        pass
    def DELETE(self, *uri, **params):
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
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()