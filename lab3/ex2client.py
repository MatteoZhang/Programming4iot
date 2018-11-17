import requests

if __name__=="__main__":
    list = ["search_by_artist",
        "search_by_title",
        "search_by_pub_year",
        "search_by_tot_tracks",
        "insert_new",
        "print_all",
        "exit"]
    while True:
        print """\nDiscography manager:
        --search_by_artist
        --search_by_title
        --search_by_pub_year
        --search_by_tot_tracks
        --insert_new
        --print_all 
        --exit"""
        operation = raw_input("choose operation: ")
        while operation not in list:
            operation = raw_input("choose operation (this time choose it right): ")