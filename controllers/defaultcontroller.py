import cherrypy

class DefaultController(object):

    @cherrypy.expose
    def index(self):
        return cherrypy.engine.templates.env.get_template('default.html').render()
