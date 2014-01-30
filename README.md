StarryPy_plugins
================

##A collection of plugins for the [StarryPy](https://github.com/CarrotsAreMediocre/StarryPy) starbound game server proxy
Please note:

* These plugins are free to use, free as in free and open source software.
* The developers of [StarryPy](https://github.com/CarrotsAreMediocre/StarryPy) have very little influence on these plugins, they shall not be blamed if something goes wrong. Precaution is advised before downloading an running any code from the internet.


# Plugins:

## [Planet Warps for StarryPy](https://github.com/MrMarvin/StarryPy_plugins/blob/master/plugins/planet_warps_for_starrypy.py)

> Currently it conflicts with /warp from warpy because really that should be called /tp due to what it does. If you want to use this with warpy at the same time, you'll have to change one of them to work around the other.
>
>This plugin allows admins to create and delete 'warps' to any planet. They just go on a planet and "/set_warp <name>" to make a warp. It correctly blocks doing so if that name or planet have been used in another warp.
>Similarly, admins can use "/del_warp <name>" to remove warps, and they don't have to be on a planet to do so.
>
>All users can do "/warp" to view a list of set warps, and "/warp <name>" to go to one of the planets free of charge. Currently it starts moving your ship to that planet and instantly warps you down, but I'm looking for a way to keep a player's ship where it is. The plugin has been tested and definitely works the way it should. Also, I suggest protecting a planet before making a warp to it.

## [StarryPy Server Status](https://bitbucket.org/zvorgan/starrypy-server-status/)
>Server status plugin available here. You can send query on specified port (specified in server_status.py) and plugin return status (online/offline) and number of players.
>Also include small php script for embed this in your website.