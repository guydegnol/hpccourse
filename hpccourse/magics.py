import os
import subprocess
import tempfile
import uuid
import argparse

from IPython.core.magic import Magics, cell_magic, magics_class


@magics_class
class NVCUDACPlugin(Magics):
    def __init__(self, shell):
        super(NVCUDACPlugin, self).__init__(shell)
        self.argparser = argparse.ArgumentParser(description="NVCCUDACPlugin params")
        self.argparser.add_argument(
            "-t", "--timeit", action="store_true", help="flag to return timeit result instead of stdout"
        )

    def run(self, exec_file, timeit=False):
        if timeit:
            stmt = f"subprocess.check_output(['{exec_file}'], stderr=subprocess.STDOUT)"
            output = self.shell.run_cell_magic(magic_name="timeit", line="-q -o import subprocess", cell=stmt)
        else:
            output = subprocess.check_output([exec_file], stderr=subprocess.STDOUT)
            output = output.decode("utf8")

        for l in output.split("\n"):
            print(l)

    @cell_magic
    def ipsa_nvcudac_and_exec(self, line, cell):
        try:
            args = self.argparser.parse_args(line.split())
        except SystemExit as e:
            self.argparser.print_help()
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            try:
                # Write code file in a temp file
                file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
                with open(file_path + ".c", "w") as f:
                    f.write(cell)

                # Compile file
                # cmd = f"/usr/local/cuda/bin/nvcc {file_path}.cu -o {file_path}.out -Wno-deprecated-gpu-targets"
                cmd = f"/usr/bin/g++ {file_path}.c -o {file_path}.out"
                subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT)

                # Run executable file
                return self.run(file_path + ".out", timeit=args.timeit)
            except subprocess.CalledProcessError as e:
                for l in e.output.decode("utf8").split("\n"):
                    print(l)
