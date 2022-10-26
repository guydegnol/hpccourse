__version__ = "1.1.0"

from .block import Block  # noqa
from .blockchain import BlockChain  # noqa
from .evaluation import *  # noqa


def load_extra_magics(ip):
    from .magics import NVCUDACPlugin, NVCUDACPluginBis

    nvcc_plugin1 = NVCUDACPlugin(ip)
    ip.register_magics(nvcc_plugin1)

    nvcc_plugin2 = NVCUDACPluginBis(ip)
    ip.register_magics(nvcc_plugin2)
