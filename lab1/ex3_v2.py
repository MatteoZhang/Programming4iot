from sys import argv
import json

class DiscoManager(object):
    def __init__(self, data):
        self.data = data
        self.feature = data.keys()
        self.fnested = data["album_list"]
        self.subfeature = self.fnested[0].keys()
        self.len = len(self.feature)
        self.lensub = len(self.subfeature)
    def search_by_artist(self, artist_name):
        try:
            for i in range(self.lensub):
                for field in self.subfeature:
                    value = data["album_list"][i][field]
                    print value
                    if value == artist_name:
                        print "for the given artist :\n"
                        for j in range(len.sub):
                            print self.subfeature[j], ": ", data["album_list"][i][self.subfeature[j]]
        except Exception, e:
            print "not found the ", artist_name, " artist"
    def search_by_title(self, title):
        pass
    def search_by_pub_year(self, pub_year):
        pass
    def search_by_tot(self, tot_tracks):
        pass
    def insert_new(self, artist, title, pub_year, tot_tracks):
        pass
    def print_all(self):
        print data

if __name__ == "__main__":
    # script, filename = argv
    filename = "discography.json"
    print "this is ur file: ", filename
    # loading file
    with open(filename) as fp:
        data = json.load(fp)

    # debug
    '''fields = data.keys()  # notice it's an array
    fnested = data["album_list"]
    print "these are the main fields of the ", filename, "file :\n", fields
    print "these are the keys in the nested one:\n", fnested
    feature = fnested[0].keys()
    print "feature in the sub dictionary\n", feature'''

    # menu
    while True:
        operation = raw_input('''
choose a command by typing it:
1)search_by_artist
2)search_by_title
3)search_by_pub_year
4)search_by_tot_tracks
5)insert_new
6)print_all 
7)exit
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
            op.search_by_tot(tracks)
        elif operation == "insert_new":
            artist = raw_input("give me artist name: ")
            title = raw_input("give me the title of the album: ")
            pub_year = raw_input("give me the pub year of the album: ")
            tot_tracks = raw_input("give me the tot tracks of the album: ")
            op.insert_new(artist,title,pub_year,tot_tracks)
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
    fp.close()