#!/usr/bin/env python3
"""
@author = Paolo Grasso
"""

import json
import cherrypy
import requests

OP = ' - add\n - sub\n - mul\n - div'
INP = '\n > '
OPTIONS = ['search', 'insert', 'print_all', 'exit', 'quit', 'delete']


class Application():

    def __init__(self):
        print('\n--- Welcome to your discography ---')

    def run(self):

        while True:
            inp = input('\nWhat do you want to do?\n - search < >\n'
            ' - insert <artist> <title> <year> <n.tracks>\n'
            ' - print_all\n - delete <title>\n - exit\n-> ')
            inp = inp.split()

            if inp[0] not in OPTIONS:
                print("Invalid command")

            if inp[0] == 'exit' or inp == 'quit':
                print("Quitting program...\a")
                break

            if inp[0] == 'print_all':
                r = requests.get('http://0.0.0.0:8080/print')
                print(json.dumps(r.json(), indent=4))

            if inp[0] == 'insert':
                chk = requests.get('http://0.0.0.0:8080/check?title='+inp[2])

                if int(chk.text) == 0:
                    r = requests.put('http://0.0.0.0:8080/insert?artist='+
                                      inp[1]+
                                     '&title='+inp[2]+
                                     '&year='+inp[3]+
                                     '&tracks='+inp[4])
                    print("\n-> New album inserted\a")

                else:
                    print("Disk %s is already present in the discography"
                           %inp[2])

                    while True:
                        up = input("Do you want to update data about %s? "
                        "(y/n)\n-> " % inp[2])

                        if up == 'y' or up == 'Y':
                            print('Updating data...')
                            r = requests.put('http://0.0.0.0:8080'+
                                             '/update?artist='+inp[1]+
                                             '&title='+inp[2]+
                                             '&year='+inp[3]+
                                             '&tracks='+inp[4])
                            break

                        elif up == 'n' or up == 'N':
                            break

            if inp[0] == 'search':
                par = inp[1]

                try:
                    for k in range(2,len(inp)):
                        par = par+' '+inp[k]
                except:
                    pass

                r = requests.get('http://0.0.0.0:8080/search?by='+par)
                print('\nResults for "%s"\n' % par)
                print(json.dumps(r.json(), indent=4))

            if inp[0] == 'delete':
                r = requests.delete('http://0.0.0.0:8080/'+
                                   '?title='+inp[1])
                print('\n-> Album deleted!\a')


if __name__ == '__main__':
    app = Application()
    app.run()
