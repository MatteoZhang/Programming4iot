import string
import cherrypy
import json


class PalindromeWS(object):
    exposed = True

    def __init__(self):
        self.palindrome = Palindrome()

    def GET(self, *uri):
        if len(uri) > 0:
            isPalindrome = self.palindrome.isPalindrome(uri[0])
            response = {"string": uri[0], "isPalindrome": isPalindrome}
            responseJson = json.dumps(response)
        else:
            responseJson = json.dumps({"error": "wrong number of parameters"})
        return responseJson


class Palindrome(object):
    def __init__(self):
        # nothing to do
        pass

    def isPalindrome(self, myString):
        length = len(myString)
        for i in range(0, length / 2):
            print i
            if (myString[i] != myString[length - i - 1]):
                return False
        return True


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(PalindromeWS(), '/palindrome', conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
