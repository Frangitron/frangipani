from frangipani.web_server import WebServer
from pythonhelpers.singleton_metaclass import SingletonMetaclass


class Components(metaclass=SingletonMetaclass):
    def __init__(self):
        self.web_server: WebServer | None = None
