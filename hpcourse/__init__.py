__version__ = "1.0.1"

# from .hpcourse import *
# from .hpcourse3 import *
from .block import Block
from .blockchain import BlockChain


def get_p():
    return "egzegaz"


def load_extra_magics(ip):
    from .magics import NVCCUDACPlugin

    nvcc_plugin_v3 = NVCCUDACPlugin(ip)
    ip.register_magics(nvcc_plugin_v3)

    nvccudac_plugin2 = NVCCPlugin3(ip)
    ip.register_magics(nvccudac_plugin2)
