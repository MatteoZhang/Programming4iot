from sys import argv
import json
import pprint
from datetime import datetime

class DiscoManager(object):
    def __init__(self, data):
        self.data = data
        self.feature = data.keys()
        self.fnested = data["album_list"]  # array
        self.subfeature = self.fnested[0].keys() #one of the album keys
        self.len = len(self.feature)
        self.lensub = len(self.fnested)
    def search_by_artist(self, artist_name):
        try:
            for i in range(self.lensub):
                for field in self.subfeature:
                    value = self.fnested[i][field]
                    if value == artist_name:
                        print "for the given artist :"
                        print "\n----"
                        for entry in self.subfeature:
                            print entry, " : ", data["album_list"][i][entry]
                        print "----\n"
        except Exception, e:
            print "not found the ", artist_name, " artist"
    def search_by_title(self, title):
        try:
            for i in range(self.lensub):
                for field in self.subfeature:
                    value = data["album_list"][i][field]
                    if value == title:
                        print "for the given title :"
                        print "\n----"
                        for entry in self.subfeature:
                            print entry, " : ", data["album_list"][i][entry]
                        print "----\n"
        except Exception, e:
            print "not found the ", title, " title"
    def search_by_pub_year(self, pub_year):
        try:
            for i in range(self.lensub):
                for field in self.subfeature:
                    value = data["album_list"][i][field]
                    if value == int(pub_year):
                        print "for the given pub year :"
                        print "\n----"
                        for entry in self.subfeature:
                            print entry, " : ", data["album_list"][i][entry]
                        print "----\n"
        except Exception, e:
            print "not found the ", pub_year, " year"
    def search_by_tot(self, tot_tracks):
        try:
            for i in range(self.lensub):
                for field in self.subfeature:
                    value = self.fnested[i][field]
                    if value == int(tot_tracks):
                        print "for the given artist :"
                        print "\n----"
                        for entry in self.subfeature:
                            print entry, " : ", data["album_list"][i][entry]
                        print "----\n"
        except Exception, e:
            print "not found the ", tot_tracks, " total tracks"
    def insert_new(self, artist, title, pub_year, tot_tracks):
        try:
            self.fnested.append({"total_tracks": int(tot_tracks), "artist": artist, "pubblication_year": int(pub_year), "title": title})
            now = datetime.now().strftime("%Y-%B-%d ,%I:%M%p")
            data["last_update"] = now
        except Exception, e:
            print "not possible to insert"
    def print_all(self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(data)

if __name__ == "__main__":
    filename = "discography.json"
    print "this is ur file: ", filename
    with open(filename) as fp:
        data = json.load(fp)

    # menu
    while True:
        operation = raw_input('''
choose a command by typing it:
--search_by_artist
--search_by_title
--search_by_pub_year
--search_by_tot_tracks
--insert_new
--print_all 
--exit
''')
        op = DiscoManager(data)
        # we can also write DiscoManager(op,data)
        if operation == "search_by_artist":
            artist = raw_input("give me artist name: ")
            op.search_by_artist(artist)
        elif operation == "search_by_title":
            title = raw_input("give me the title of the album: ")
            op.search_by_title(title)
        elif operation == "search_by_pub_year":
            pub_year = raw_input("give me the pub year of the album: ")
            op.search_by_pub_year(pub_year)
        elif operation == "search_by_tot_tracks":
            tot_tracks = raw_input("give me the tot tracks of the album: ")
            op.search_by_tot(tot_tracks)
        elif operation == "insert_new":
            artist = raw_input("give me artist name: ")
            title = raw_input("give me the title of the album: ")
            pub_year = raw_input("give me the pub year of the album: ")
            tot_tracks = raw_input("give me the tot tracks of the album: ")
            op.insert_new(artist, title, pub_year, tot_tracks)
        elif operation == "print_all":
            op.print_all()
        else:
            if operation == "exit":
                print "you exited with the ", operation, " command"
                break
            else:
                print "wrong command but I will forgive you and exit for u"
            break

    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=2)
