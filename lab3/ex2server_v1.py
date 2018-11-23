#!/usr/bin/env python3
"""
@author = Paolo Grasso
"""
import json
import datetime
import cherrypy


class WebServer():  # RESTful web server
    exposed = True

    def GET(self, *uri, **params):
        disco = Discography()

        if uri[0] == 'print':
            return disco.print_data()
        else:
            pass

        if uri[0] == 'search':
            return disco.search(params['by'])
        else:
            pass

        if uri[0] == 'check':
            return str(disco.check_disk(params['title']))  # str(boolean)
        else:
            pass

    def POST(self):
        pass

    def PUT(self, *uri, **params):
        disco = Discography()

        if uri[0] == 'insert':
            disco.insert_data(params['artist'],
                              params['title'],
                              params['year'],
                              params['tracks'])

        elif uri[0] == 'update':
            disco.check_disk(params['title'])  # Find disk index
            disco.update_data(params['artist'],
                              params['title'],
                              params['year'],
                              params['tracks'])

        disco.save_data()

    def DELETE(self, *uri, **params):
        disco = Discography()
        if (disco.check_disk(params['title'])):  # Find disk index
            raise cherrypy.HTTPError('Album not present in the database')
        else:
            disco.delete_data()
            disco.save_data()


class Discography(object):

    def __init__(self, filename='asset/discography.json'):
        self.filename = filename
        self.data = {}

        with open(self.filename, 'r') as infile:
            self.data = json.load(infile)

        self.options = ['search', 'insert', 'print_all', 'exit', 'quit']

    def search(self, arg):
        self.arg = arg
        k = 0
        search_results = {'albums':[]}
        for d in self.data['album_list']:

            if (d['artist'] == self.arg or d['title'] == self.arg):
                search_results['albums'].append(self.data['album_list'][k])

            k += 1

        try:
            self.arg=int(self.arg)
            k = 0

            for d in self.data['album_list']:

                if (d['publication_year'] == self.arg or
                    d['total_tracks'] == self.arg):
                    search_results['albums'].append(self.data['album_list'][k])

                k += 1

        except:
            pass
        return json.dumps(search_results['albums'])

    def print_data(self):
        return json.dumps(self.data)

    def save_data(self):
        with open(self.filename, 'w') as outfile:
            json.dump(self.data, outfile, ensure_ascii=False)

    def check_disk(self, disk):
        self.disk = disk
        k = 0

        for d in self.data['album_list']:

            if d['title'] == self.disk:
                self.list_n = k
                return 1

            k += 1

        return 0

    def update_data(self, artist, title, year, tracks):
        self.artist = artist
        self.title = title

        try:
            self.publication_year = int(year)
            self.total_tracks = int(tracks)
            self.data['album_list'][self.list_n].update({"artist": self.artist,
                "title": self.title, "publication_year": self.publication_year,
                "total_tracks": self.total_tracks})
            self.update_time()

        except:
            pass

    def insert_data(self, artist, title, year, tracks):

        self.artist = artist
        self.title = title

        try:
            self.publication_year = int(year)
            self.total_tracks = int(tracks)
            self.data['album_list'].append({"artist": self.artist,
                "title": self.title, "publication_year": self.publication_year,
                "total_tracks": self.total_tracks})
            self.update_time()

        except:
            pass

    def update_time(self):
        self.data.update({"last_update":
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})

    def delete_data(self):
        del self.data['album_list'][self.list_n]
        self.update_time()


if __name__ == '__main__':

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