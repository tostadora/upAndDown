import cherrypy
from cherrypy.process import plugins

import helpers.uadatabase

class UADbPlugin(plugins.SimplePlugin):

    def __init__(self, bus):
        plugins.SimplePlugin.__init__(self, bus)
        if (not helpers.uadatabase.check_database()):
            helpers.uadatabase.create_database()

    def query(self, query):
        conn = helpers.uadatabase.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
