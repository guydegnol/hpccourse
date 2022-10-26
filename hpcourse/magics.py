import os
import subprocess
import tempfile
import uuid
import argparse

from IPython.core.magic import Magics, cell_magic, magics_class


@magics_class
class NVCCUDACPlugin(Magics):
    def __init__(self, shell):
        super(NVCCUDACPlugin, self).__init__(shell)

        self.parser = argparse.ArgumentParser(description="NVCCUDACPlugin params")
        self.parser.add_argument(
            "-t", "--timeit", action="store_true", help="flag to return timeit result instead of stdout"
        )

    @staticmethod
    def compile(file_path):
        compiler = "/usr/local/cuda/bin/nvcc"
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

        for l in output.split("\n"):
            print(l)

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
                for l in e.output.decode("utf8").split("\n"):
                    print(l)
                output = None
        return output
