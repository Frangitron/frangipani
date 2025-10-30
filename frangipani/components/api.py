import logging

from frangipani.components.components import Components
from frangipani.web_server import WebServer


_logger = logging.getLogger("Components")


def init_components():
    _logger.info("Initializing web server")
    Components().web_server = WebServer()
    _logger.info("Web server initialized")
