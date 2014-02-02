import cherrypy
from cherrypy.process import plugins

import helpers.uadatabase

class UADbPlugin(plugins.SimplePlugin):

    conn = None

    def __init__(self, bus):
        plugins.SimplePlugin.__init__(self, bus)
        if (not helpers.uadatabase.check_database()):
            helpers.uadatabase.create_database()

    def start(self):
        self.conn = helpers.uadatabase.connect()

    def stop(self):
        self.conn.close()
