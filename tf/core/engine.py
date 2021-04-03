import socketserver
import threading


class TestFolderHandler(socketserver.BaseRequestHandler):
    """
    Framework handler
    """

    def handle(self) -> None:
        pass


class TestFolder(socketserver.ThreadingTCPServer):
    """
    Test Automation object
    """

    def __init__(self, server_address=("localhost", 8778), _handler=TestFolderHandler):
        super().__init__(server_address=server_address, RequestHandlerClass=_handler)
