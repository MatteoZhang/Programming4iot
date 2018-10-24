from sys import argv
import json

class DiscoManager(object):
    def __init__(self):
        self.data = data
    def search_by_artist(self, artist_name):
        try:
            for artist_name in data["album_list"]["artist"]:
                print "the artist's disc:  ", data["album_list"]
        except Exception, e:
            print "not found the ", artist_name , " artist"

if __name__ == "__main__":
    script, filename = argv
    print "this is ur script and file: ", script , filename
    # loading file
    with open(filename) as fp:
        data = json.load(fp)

    while True:
        operation = raw_input('''
        choose a command by typing it:
        1)search_by_artist
        2)search_by_title
        3)
        ''')
        op = DiscoManager()
        if operation == "search_by_artist":
            artist=raw_input("give me artist name: ")
            op.search_by_artist(artist)
        else:
            break
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=2)
