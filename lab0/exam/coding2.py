import string
import cherrypy
import json
import time


class ChronometerWS(object):
    exposed = True

    def __init__(self):
        self.chronometer = Chronometer()

    def GET(self, *uri):
        responseJson = json.dumps(
            {"message": "error: wrong or number of web service. choose among /start, /stop and /print"})

        if len(uri) > 0:
            if (uri[0].lower() == "start"):
                self.chronometer.start()
                responseJson = json.dumps({"message": "chronometer is running"})
            elif (uri[0].lower() == "stop"):
                self.chronometer.stop()
                responseJson = json.dumps({"message": "chronometer is stopped"})
            elif (uri[0].lower() == "print"):
                timer = self.chronometer.getTimer()
                responseJson = json.dumps({"message": timer})

        return responseJson


class Chronometer(object):
    def __init__(self):
        self.beginning = None

    def start(self):
        self.beginning = time.time()

    def stop(self):
        self.beginning = None

    def getTimer(self):
        msg = ""
        if self.beginning is None:
            msg = "chronometer is not running"
        else:
            timer = int(time.time() - self.beginning)
            msg = timer

        return msg


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(ChronometerWS(), '/chronometer', conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
