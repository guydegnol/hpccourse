__version__ = "1.0.0"

# from .hpcourse import *
# from .hpcourse3 import *
from .block import Block
from .blockchain import BlockChain


def get_p():
    return "egzegaz"


def load_magic(ip):
    from .magics import NVCCUDACPlugin

    nvcc_plugin_v3 = NVCCUDACPlugin(ip)
    ip.register_magics(nvcc_plugin_v3)
