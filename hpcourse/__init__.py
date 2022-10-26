__version__ = "1.2.0"

import os

from .block import Block  # noqa
from .blockchain import BlockChain  # noqa
from .evaluation import Evaluation  # noqa


def load_extra_magics(ip):
    from .magics import NVCUDACPlugin, NVCUDACPluginBis

    ip.register_magics(NVCUDACPlugin(ip))
    ip.register_magics(NVCUDACPluginBis(ip))
    ip.register_magics(Evaluation(ip))

    print(f"Load version hpcourse (version={__version__})")


def ipsa_login(student_name=None, ip=None):

    if student_name is None:
        raise IOError(
            f"""Register yourself for the course. Ex:
# Guillaume Therin, gtherin, ...
hpcourse.ipsa_login("gtherin", IPython.get_ipython())
"""
        )
    else:
        os.environ["STUDENT"] = student_name
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hpcgpu_course/hpcourse/ipsastudents.json"

    if ip is None:
        raise IOError(
            f"""Register yourself for the course using the line:
hpcourse.register("{student_name}", IPython.get_ipython())
"""
        )

    load_extra_magics(ip)
