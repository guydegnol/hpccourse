__version__ = "1.0.1"

# from .hpcourse import *
# from .hpcourse3 import *
from .block import Block
from .blockchain import BlockChain


def get_p():
    return "egzegaz"


def load_extra_magics(ip):
    from .magics import NVCCUDACPlugin, NVCUDACPluginBis

    ip.register_magics(NVCCUDACPlugin(ip))
    ip.register_magics(NVCUDACPluginBis(ip))
