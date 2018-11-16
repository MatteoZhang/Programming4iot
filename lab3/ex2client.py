import requests

if __name__ == "__main__":
    while True:
        operation = raw_input('''
choose a command by typing it:
-search_by_artist
-search_by_title
-search_by_pub_year
-search_by_tot_tracks
-insert_new
-print_all 
-exit
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