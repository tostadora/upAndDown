#!/usr/bin/python

import sqlite3
import cherrypy
from jinja2 import Environment, FileSystemLoader

from helpers import uadatabase
from controllers.defaultcontroller import DefaultController
from plugins.db import UADbPlugin
from plugins.jinja import JinjaPlugin

jinjaenv = Environment(loader=FileSystemLoader('templates/'))

def main():
    cherrypy.engine.db = UADbPlugin(cherrypy.engine)
    cherrypy.engine.templates = JinjaPlugin(cherrypy.engine)

    cherrypy.engine.db.subscribe()
    cherrypy.engine.templates.subscribe()

    cherrypy.quickstart(DefaultController())

if __name__ == "__main__":
    main()
