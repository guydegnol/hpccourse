from v1.v1 import NVCCPlugin as NVCC_V1
from v2.v2 import NVCCPluginV2 as NVCC_V2


import os
import subprocess
import tempfile
import uuid

from IPython.core.magic import Magics, cell_magic, magics_class
from common import helper

compiler = "/usr/local/cuda/bin/nvcc"


@magics_class
class NVCCPlugin3(Magics):
    def __init__(self, shell):
        super(NVCCPlugin3, self).__init__(shell)

        self.argparser = helper.get_argparser()

    @staticmethod
    def compile(file_path):
        subprocess.check_output(
            [compiler, file_path + ".cu", "-o", file_path + ".out", "-Wno-deprecated-gpu-targets"],
            stderr=subprocess.STDOUT,
        )

    def run(self, file_path, timeit=False):
        if timeit:
            stmt = f"subprocess.check_output(['{file_path}.out'], stderr=subprocess.STDOUT)"
            output = self.shell.run_cell_magic(magic_name="timeit", line="-q -o import subprocess", cell=stmt)
        else:
            output = subprocess.check_output([file_path + ".out"], stderr=subprocess.STDOUT)
            output = output.decode("utf8")

        helper.print_out(output)
        return None

    @cell_magic
    def nvcudac_and_exec(self, line, cell):
        try:
            args = self.argparser.parse_args(line.split())
        except SystemExit as e:
            self.argparser.print_help()
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
            with open(file_path + ".cu", "w") as f:
                f.write(cell)
            try:
                self.compile(file_path)
                output = self.run(file_path, timeit=args.timeit)
            except subprocess.CalledProcessError as e:
                helper.print_out(e.output.decode("utf8"))
                output = None
        return output


def load_ipython_extension(ip):
    nvccudac_plugin = NVCC_V1(ip)
    ip.register_magics(nvccudac_plugin)

    nvccudac_plugin2 = NVCCPlugin3(ip)
    ip.register_magics(nvccudac_plugin2)
