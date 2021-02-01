from xdg import xdg_config_home
from urllib3 import request

from os import path, makedirs

import xdg

APP_NAME = "com.github.gauthamkrishna9991.wire-me-in"

APP_CONFIG_PATH = xdg_config_home() + APP_NAME

# if path to the config directory does not exist,
# we create one to it.
# this, as far as I've seen, MUST conform to XDG specification
if not path.exists(APP_CONFIG_PATH):
    # create all dirs to that path
    makedirs(APP_CONFIG_PATH)
    # we need wgcf URLs before we can download one
    #TODO: Complete it