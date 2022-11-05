__version__ = "1.5.0"

from .block import Block  # noqa
from .blockchain import BlockChain  # noqa
from .evaluation import Evaluation, set_up_student  # noqa
from .flops import *  # noqa
from .languages import get_languages_perf  # noqa
from .pycker import *  # noqa


def load_extra_magics(ip, verbose=True):
    from .magics import NVCUDACPlugin, NVCUDACPluginBis

    ip.register_magics(NVCUDACPlugin(ip))
    ip.register_magics(NVCUDACPluginBis(ip))
    ip.register_magics(Evaluation(ip))

    if verbose:
        print(f"Load version hpccourse (version={__version__})")


def ipsa_login(student_name=None, ip=None):

    student_login = set_up_student(student_name)

    if ip is None:
        raise Exception.DefaultCredentialsError(
            f"""Register yourself for the course using the line:
hpccourse.register("{student_name}", IPython.get_ipython())
"""
        )

    load_extra_magics(ip, verbose=False)
    print(f"Load version hpccourse (version={__version__}, connected as {student_login})")
