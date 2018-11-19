import requests
import json

if __name__=="__main__":
    lista = ["search_by_artist",
        "search_by_title",
        "search_by_pub_year",
        "search_by_tot_tracks",
        "insert_new",
        "print_all",
        "exit"]
    while True:
        print """\nDiscography manager:
        search_by_artist
        search_by_title
        search_by_pub_year
        search_by_tot_tracks 
        insert_new
        print_all 
        exit"""
        try:
            operation = raw_input("choose operation: ")
            s = {}
            if operation in lista[0:4]:
                par = raw_input("parameter: ")
                try:
                    r = requests.get('http://localhost:8080/' + operation + '/' + par)
                except Exception,e:
                    print "invalid parameter"
            elif operation == "print_all":
                r = requests.get('http://localhost:8080/' + operation)
            elif operation == "exit":
                break
            else:
                artistName = raw_input("name of the artist: ")
                albumTitle = raw_input("album title: ")
                pubYear = raw_input("publication year: ")
                totalTracks = raw_input("total number of tracks: ")
                r = requests.post('http://localhost:8080/' + operation + '?' + 'artist=' + artistName + '&' +
                                  'album=' + albumTitle + '&' + 'year=' + pubYear + '&' + 'tracks=' + totalTracks)
            s = r.json()
            print json.dumps(s)
        except Exception,e:
            print "invalid operation"
            operation = raw_input("choose operation again: ")

