#===========================================================
#   BRWhisperPlugin
#   Author: FZFalzar of Brutus.SG Starbound
#   Version: v0.1
#   Description: A better whisper plugin with reply and SocialSpy
#===========================================================

from base_plugin import SimpleCommandPlugin
from plugins.core.player_manager import permissions, UserLevels
from utility_functions import extract_name

class BRWhisperPlugin(SimpleCommandPlugin):
    name = "brutus_whisper"
    depends = ['command_dispatcher', 'player_manager']
    commands = ["whisper", "w", "r", "socialspy"]
    auto_activate = True

    def activate(self):
        super(BRWhisperPlugin, self).activate()
        self.player_manager = self.plugins['player_manager'].player_manager
        self.reply_history = dict()
        self.sspy_enabled_dict = dict()

    @permissions(UserLevels.GUEST)
    def whisper(self, data):
        """Sends a message to target player. Syntax: /whisper [player name] [msg]"""
        if len(data) == 0:
            self.protocol.send_chat_message(self.whisper.__doc__)
            return
        try:
            targetName, message = extract_name(data)
            if not message:
                self.protocol.send_chat_message("Invalid message!")
                self.protocol.send_chat_message(self.whisper.__doc__)
                return           
            self.logger.info("Message to %s from %s: %s" % (targetName, self.protocol.player.name, " ".join(message)))
            self.sendWhisper(targetName, " ".join(message))
        except ValueError as e:
            self.protocol.send_chat_message(self.whisper.__doc__)
        except TypeError as e:
            self.protocol.send_chat_message(self.whisper.__doc__)

    def reply(self, data):
        """Replies to last player who whispered you. Syntax: /r [msg]"""
        if len(data) == 0:
            self.protocol.send_chat_message(self.reply.__doc__)
            return
 
        #retrieve your own history, using your name as key
        try:
            target = self.reply_history[self.protocol.player.name]
            self.sendWhisper(target, " ".join(data))
        except KeyError as e:
            self.protocol.send_chat_message("You have no one to reply to!")

    @permissions(UserLevels.GUEST)
    def w(self, data):
        self.whisper(data)

    @permissions(UserLevels.GUEST)
    def r(self, data):
        self.reply(data)

    def sendWhisper(self, target, message):
        targetPlayer = self.player_manager.get_logged_in_by_name(target)
        if targetPlayer is None:
            self.protocol.send_chat_message(("Couldn't send a message to %s") % target)
            return
        else:
            #show yourself the message
            strMsgTo = "[To: %s^#00FF00;] %s" % (targetPlayer.colored_name(self.config.colors), message)
            strTo = "To: %s" % targetPlayer.colored_name(self.config.colors)
            self.protocol.send_chat_message(strMsgTo)

            #show target the message            
            protocol = self.factory.protocols[targetPlayer.protocol]
            strMsgFrom = "[From: %s^#00FF00;] %s" % (self.protocol.player.colored_name(self.config.colors), message)
            strFrom = "From: %s" % self.protocol.player.colored_name(self.config.colors)
            protocol.send_chat_message(strMsgFrom)            

            #store your last sent history, so the other player can reply
            #store your name using your target's name as key, so he can use his name to find you
            self.reply_history[target] = self.protocol.player.name

            #send message to people with socialspy on
            for key, value in self.sspy_enabled_dict.iteritems():
                sspy_player = self.player_manager.get_logged_in_by_name(key)
                if sspy_player is not None:
                    if sspy_player.access_level >= UserLevels.ADMIN and value == True:
                        protocol = self.factory.protocols[sspy_player.protocol]
                        protocol.send_chat_message("^#00FFFF;[SS]^#00FF00;[%s %s^#00FF00;] %s" % (strFrom, strTo, message))           

    @permissions(UserLevels.ADMIN)
    def socialspy(self, data):
        """Enables the viewing of messages sent by other players. Syntax: /socialspy [on|off]"""
        if len(data) == 0:
            self.protocol.send_chat_message(self.socialspy.__doc__)
        val = " ".join(data)
        if val.lower() in ["on", "true"]:
            self.sspy_enabled_dict[self.protocol.player.name] = True
            self.protocol.send_chat_message("SocialSpy has been enabled!")
        elif val.lower() in ["off", "false"]:
            self.sspy_enabled_dict[self.protocol.player.name] = False
            self.protocol.send_chat_message("SocialSpy has been disabled!")
        else:
            self.protocol.send_chat_message("Invalid value! Permitted values are \"on\", \"true\", \"off\", \"false\"")