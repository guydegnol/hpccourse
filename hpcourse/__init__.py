__version__ = "1.1.3"

from .block import Block  # noqa
from .blockchain import BlockChain  # noqa
from .evaluation import evaluate, Evaluation  # noqa


def load_extra_magics(ip):
    from .magics import NVCUDACPlugin, NVCUDACPluginBis

    nvcc_plugin1 = NVCUDACPlugin(ip)
    ip.register_magics(nvcc_plugin1)

    nvcc_plugin2 = NVCUDACPluginBis(ip)
    ip.register_magics(nvcc_plugin2)
    print(f"Load version hpcourse (version={__version__})")
