__version__ = "1.1.6"

import os

from .block import Block  # noqa
from .blockchain import BlockChain  # noqa
from .evaluation import evaluate, Evaluation  # noqa


def load_extra_magics(ip):
    from .magics import NVCUDACPlugin, NVCUDACPluginBis

    nvcc_plugin1 = NVCUDACPlugin(ip)
    ip.register_magics(nvcc_plugin1)

    nvcc_plugin2 = NVCUDACPluginBis(ip)
    ip.register_magics(nvcc_plugin2)
    ip.register_magics(Evaluation(ip))

    print(f"Load version hpcourse (version={__version__})")


def register(student_name=None, ip=None):

    if student_name is None:
        raise IOError(
            f"""Register your self for the course. Ex:
# Guillaume Therin => gtherin
hpcourse.register("gtherin", IPython.get_ipython())
"""
        )
    os.env["STUDENT"] = student_name

    if ip is None:
        raise IOError(
            f"""Register your self for the course using the line:
hpcourse.register("{student_name}", IPython.get_ipython())
"""
        )

    load_extra_magics(ip)
