__version__ = "1.2.5"

from .block import Block  # noqa
from .blockchain import BlockChain  # noqa
from .evaluation import Evaluation, set_up_student  # noqa


def load_extra_magics(ip):
    from .magics import NVCUDACPlugin, NVCUDACPluginBis

    ip.register_magics(NVCUDACPlugin(ip))
    ip.register_magics(NVCUDACPluginBis(ip))
    ip.register_magics(Evaluation(ip))

    print(f"Load version hpccourse (version={__version__})")


def ipsa_login(student_name=None, ip=None):

    if student_name is None:
        raise IOError(
            f"""Register yourself for the course. Ex:
# John Doe, jdoe, ...
hpccourse.ipsa_login("jdoe", IPython.get_ipython())
"""
        )
    else:
        set_up_student(student_name)

    if ip is None:
        raise IOError(
            f"""Register yourself for the course using the line:
hpccourse.register("{student_name}", IPython.get_ipython())
"""
        )

    load_extra_magics(ip)
