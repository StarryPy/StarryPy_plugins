# -*- coding: UTF-8 -*-

from base_plugin import SimpleCommandPlugin
from plugins.core.player_manager import permissions, UserLevels


class EmotesPlugin(SimpleCommandPlugin):
    """
    Very simple plugin that adds /me <emote> command to StarryPy.
    """
    name = "emotes_plugin"
    depends = ["command_dispatcher", "player_manager"]
    commands = ["me"]
    auto_activate = True

    def activate(self):
        super(EmotesPlugin, self).activate()
        self.player_manager = self.plugins['player_manager'].player_manager

    @permissions(UserLevels.GUEST)
    def me(self, data):
        """Creates a player emote message. Syntax: /me <emote>"""
        if len(data) == 0:
            self.protocol.send_chat_message(self.me.__doc__)
            return
        if self.protocol.player.muted:
            self.protocol.send_chat_message(
                "You are currently muted and cannot emote. You are limited to commands and admin chat (prefix your lines with %s for admin chat." % (self.config.chat_prefix*2))
            return False
        emote = " ".join(data)
        self.factory.broadcast_planet("^#F49413;%s %s" % (self.protocol.player.name, emote), planet=self.protocol.player.planet)
        return False
