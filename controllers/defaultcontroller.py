import cherrypy

from controllers.productscontroller import ProductsController

class DefaultController(object):


    def __init__(self):
        self.products = ProductsController()

    @cherrypy.expose
    def index(self):
        return cherrypy.engine.templates.env.get_template('default.html').render()
