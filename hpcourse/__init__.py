__version__ = "0.1.5"

# from .hpcourse import *
# from .hpcourse3 import *


def get_p():
    return "egzegaz"


def load_ipython_extension(ip):
    from .magics import NVCCPlugin3

    nvcc_plugin_v3 = NVCCPlugin3(ip)
    ip.register_magics(nvcc_plugin_v3)
