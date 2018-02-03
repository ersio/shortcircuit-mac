# crestprocessor.py

import threading
from PyQt5 import QtCore
from .crest.crest import Crest


class CrestProcessor(QtCore.QObject):
    """
    CREST Middle-ware
    """
    login_response = QtCore.pyqtSignal(str)
    logout_response = QtCore.pyqtSignal()
    location_response = QtCore.pyqtSignal(str)
    destination_response = QtCore.pyqtSignal(bool)

    def __init__(self, implicit, client_id, client_secret, parent=None):
        super(CrestProcessor, self).__init__(parent)
        self.crest = Crest(implicit, client_id, client_secret, self._login_callback, self._logout_callback)

    def login(self):
        return self.crest.start_server()

    def logout(self):
        self.crest.logout()

    def get_location(self):
        server_thread = threading.Thread(target=self._get_location)
        server_thread.setDaemon(True)
        server_thread.start()

    def _get_location(self):
        location = self.crest.get_char_location()
        self.location_response.emit(location)

    def set_destination(self, sys_id):
        server_thread = threading.Thread(target=self._set_destination, args=(sys_id, ))
        server_thread.setDaemon(True)
        server_thread.start()

    def _set_destination(self, sys_id):
        response = self.crest.set_char_destination(sys_id)
        self.destination_response.emit(response)

    def _login_callback(self, char_name):
        self.login_response.emit(char_name)

    def _logout_callback(self):
        self.logout_response.emit()
