#-*- coding: UTF-8 -*-

import requests
from xml.dom import minidom
from base_plugin import BasePlugin


class NotifyMyAndroid(BasePlugin):
    """
    Sends a NotifyMyAndroid (notifymyandroid.com) notification whenever a player joins. It's based on mdeneen's
    Pushover plugin (https://github.com/mdeneen)
    """
    name = "nma_plugin"
    auto_activate = False

    def activate(self):
        super(NotifyMyAndroid, self).activate()
        self.verify_api_key()

    def send_notification(self, msg, api_key, api_application, api_event, api_priority):
        payload = {'apikey': api_key, 'application': api_application, 'event': api_event,
                   'description': msg, 'priority': api_priority}
        req = requests.post('https://www.notifymyandroid.com/publicapi/notify', data=payload)
        errors = minidom.parseString(req.text).getElementsByTagName('error')
        if len(errors) > 0:
            errortext = errors[0].childNodes[0].data
            self.logger.error("NotifyMyAndroid Notification could not be sent. Error: {e}".format(e=errortext))
        else:
            self.logger.info("NotifyMyAndroid Notification was sent.")

    def verify_api_key(self):
        api_key = self.config.plugin_config["api_key"]
        payload = {'apikey': api_key}
        req = requests.post('https://www.notifymyandroid.com/publicapi/verify', data=payload)
        errors = minidom.parseString(req.text).getElementsByTagName('error')
        if len(errors) > 0:
            errortext = errors[0].childNodes[0].data
            self.logger.error("NotifyMyAndroid API-Key could not be verified. Error: {e}".format(e=errortext))
        else:
            self.logger.info("NotifyMyAndroid API-Key was successfully verified.")

    def after_connect_response(self, data):
        if self.protocol.player.name not in self.config.plugin_config["ignored_players"]:
            message = "Player {p} has joined the server".format(p=self.protocol.player.name)
            api_key = self.config.plugin_config["api_key"]
            api_application = self.config.plugin_config["api_application"]
            api_event = self.config.plugin_config["api_event"]
            api_priority = self.config.plugin_config["api_priority"]
            self.send_notification(message, api_key, api_application, api_event, api_priority)
