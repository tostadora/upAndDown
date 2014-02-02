import cherrypy
from cherrypy.process import wspbus, plugins
from jinja2 import Environment, FileSystemLoader

class JinjaPlugin(plugins.SimplePlugin):
    env = None

    def start(self):
        self.env = Environment(loader=FileSystemLoader('templates'))       
