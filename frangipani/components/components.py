from pythonhelpers.singleton_metaclass import SingletonMetaclass

from frangipani.web_server import WebServer


class Components(metaclass=SingletonMetaclass):
    def __init__(self):
        self.web_server: WebServer | None = None
