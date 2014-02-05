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
        emote = " ".join(data)
        self.factory.broadcast_planet("^#CCCCCC;%s %s" % (self.protocol.player.name, emote), planet=self.protocol.player.planet)
        return False
