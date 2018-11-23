import requests
import json

ADDRESS = 'http://localhost:8085/'

if __name__ == "__main__":
    while True:
        print """Discography manager:
        search_by_artist
        search_by_title
        search_by_pub_year
        search_by_tot_tracks 
        insert_new
        print_all
        delete 
        exit"""
        try:
            s = []
            operation = raw_input("choose operation: ")
            if operation in ['search_by_artist', 'search_by_title', 'search_by_pub_year', 'search_by_tot_tracks']:
                par = raw_input("parameter: ")
                try:
                    r = requests.get(ADDRESS + operation + '/' + par)
                except Exception,e:
                    print "invalid parameter"
            elif operation == "print_all":
                r = requests.get(ADDRESS + operation)
            elif operation == "exit":
                break
            elif operation == "insert_new":
                artistName = raw_input("name of the artist: ")
                albumTitle = raw_input("album title: ")
                pubYear = raw_input("publication year: ")
                totalTracks = raw_input("total number of tracks: ")
                r = requests.put(ADDRESS + operation + '?artist=' + artistName + '&album=' +
                                 albumTitle + '&year=' + pubYear + '&tracks=' + totalTracks)
            elif operation == "delete":
                par = raw_input("what u want to delete?: ")
                r = requests.delete(ADDRESS + operation + '/' + par)
            s = r.json()
            print json.dumps(s, indent=2)
            print "\n"
        except Exception, e:
            print "error: ", e, " -- try again\n"
