__version__ = "1.0.1"

from .block import Block
from .blockchain import BlockChain


def get_p():
    return "egzegaz"


def load_extra_magics(ip):
    # from .magics import NVCCUDACPlugin, NVCUDACPluginBis
    from .magics import NVCUDACPlugin, NVCUDACPluginBis

    nvcc_plugin1 = NVCUDACPlugin(ip)
    ip.register_magics(nvcc_plugin1)

    nvcc_plugin2 = NVCUDACPluginBis(ip)
    ip.register_magics(nvcc_plugin2)
