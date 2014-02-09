StarryPy_plugins
================

##A collection of plugins for the [StarryPy](https://github.com/CarrotsAreMediocre/StarryPy) starbound game server proxy
Please note:

* These plugins are free to use, free as in free and open source software.
* The developers of [StarryPy](https://github.com/CarrotsAreMediocre/StarryPy) have very little influence on these plugins, they shall not be blamed if something goes wrong. Precaution is advised before downloading an running any code from the internet.


# Plugins:

## [SloanReynolds /who on login](https://github.com/MrMarvin/StarryPy_plugins/blob/master/plugins/loginwho_plugin)
> Displays a /who upon login

## [Maffi's uptime plugin](https://github.com/MrMarvin/StarryPy_plugins/blob/master/plugins/uptime)
> Very simple plugin that responds to /uptime with the time StarryPy is running.

## [teihoo's /me emote plugin](https://github.com/StarryPy/StarryPy_plugins/tree/master/plugins/emotes)
> Very simple plugin that adds /me <emote> command to StarryPy.

## [teihoo's /starteritems plugin](https://github.com/StarryPy/StarryPy_plugins/tree/master/plugins/starteritems)
> Adds /starteritems command which can be used once per player and will give player a set of predefined starter items
> It is ment to work along with new_player_greeter_plugin, and will give a different set, that's why:

### Add the following block to your config file:

>```
"starteritems_plugin": {
    "auto_activate": true,
    "items": [
    [ "coalore", 100 ],
    [ "money", 1000 ]
    ],
    "message": "You were given a set of starter items ;)"
  }
>```


## [mdeneen's Pushover plugin](https://github.com/StarryPy/StarryPy_plugins/tree/master/plugins/pushover_plugin)
> This adds basic support for [Pushover](https://pushover.net) messages. Right now it can:

> - Send a pushover message to a mobile device whenever a player joins
> - Avoid sending notifications for ignored players.
> Pushover supports delivery groups, so one could send messages to multiple users. This can be useful when running a private server so that you know when other players are online.

### Add the following block to your config file:

> ```
"pushover_plugin": {
    "api_key": "MY_API_KEY",
    "ignored_players": 
        "Player1",
    ],
    "user_key": "MY_USER_KEY"
}
>```

## [Hexicube's Planet Warps for StarryPy](https://github.com/MrMarvin/StarryPy_plugins/blob/master/plugins/hexicube_planet_warps_for_starrypy.py)

> Currently it conflicts with /warp from warpy because really that should be called /tp due to what it does. If you want to use this with warpy at the same time, you'll have to change one of them to work around the other.
>
>This plugin allows admins to create and delete 'warps' to any planet. They just go on a planet and "/set_warp <name>" to make a warp. It correctly blocks doing so if that name or planet have been used in another warp.
>Similarly, admins can use "/del_warp <name>" to remove warps, and they don't have to be on a planet to do so.
>
>All users can do "/warp" to view a list of set warps, and "/warp <name>" to go to one of the planets free of charge. Currently it starts moving your ship to that planet and instantly warps you down, but I'm looking for a way to keep a player's ship where it is. The plugin has been tested and definitely works the way it should. Also, I suggest protecting a planet before making a warp to it.

## [StarryPy Server Status](https://bitbucket.org/zvorgan/starrypy-server-status/)
>Server status plugin available here. You can send query on specified port (specified in server_status.py) and plugin return status (online/offline) and number of players.
>Also include small php script for embed this in your website.
