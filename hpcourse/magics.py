import os
import subprocess
import tempfile
import uuid
import argparse

from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring


@magics_class
class NVCUDACPlugin(Magics):
    def __init__(self, shell):
        super(NVCUDACPlugin, self).__init__(shell)

        self.argparser = argparse.ArgumentParser(description="NVCCUDACPlugin params")
        self.argparser.add_argument(
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


@magics_class
class NVCUDACPluginBis(Magics):
    def __init__(self, shell):
        super(NVCUDACPluginBis, self).__init__(shell)

        self.argparser = argparse.ArgumentParser(description="NVCCUDACPlugin params")
        self.argparser.add_argument(
            "-t", "--timeit", action="store_true", help="flag to return timeit result instead of stdout"
        )
        current_dir = os.getcwd()
        self.output_dir = os.path.join(current_dir, "src")
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
            print(f"created output directory at {self.output_dir}")
        else:
            print(f"directory {self.output_dir} already exists")

        self.out = os.path.join(current_dir, "result.out")
        print(f"Out bin {self.out}")

    @staticmethod
    def compile(output_dir, file_paths, out):
        compiler = "/usr/local/cuda/bin/nvcc"
        res = subprocess.check_output(
            [compiler, "-I" + output_dir, file_paths, "-o", out, "-Wno-deprecated-gpu-targets"],
            stderr=subprocess.STDOUT,
        )
        for l in res.split("\n"):
            print(l)

    def run(self, timeit=False):
        if timeit:
            stmt = f"subprocess.check_output(['{self.out}'], stderr=subprocess.STDOUT)"
            output = self.shell.run_cell_magic(magic_name="timeit", line="-q -o import subprocess", cell=stmt)
        else:
            output = subprocess.check_output([self.out], stderr=subprocess.STDOUT)
            output = output.decode("utf8")

        for l in output.split("\n"):
            print(l)
        return None

    @magic_arguments()
    @argument(
        "-n", "--name", type=str, help="file name that will be produced by the cell. must end with .cu extension"
    )
    @argument("-c", "--compile", type=bool, help="Should be compiled?")
    @cell_magic
    def nvcudac(self, line="", cell=None):
        args = parse_argstring(self.cuda, line)
        ex = args.name.split(".")[-1]
        if ex not in ["cu", "h"]:
            raise Exception("name must end with .cu or .h")

        if not os.path.exists(self.output_dir):
            print(f"Output directory does not exist, creating")
            try:
                os.mkdir(self.output_dir)
            except OSError:
                print(f"Creation of the directory {self.output_dir} failed")
            else:
                print(f"Successfully created the directory {self.output_dir}")

        file_path = os.path.join(self.output_dir, args.name)
        with open(file_path, "w") as f:
            f.write(cell)

        if args.compile:
            try:
                self.compile(self.output_dir, file_path, self.out)
                output = self.run(timeit=args.timeit)
            except subprocess.CalledProcessError as e:
                for l in e.output.decode("utf8").split("\n"):
                    print(l)

                output = None
        else:
            output = f"File written in {file_path}"

        return output

    @cell_magic
    def cuda_run(self, line="", cell=None):
        try:
            args = self.argparser.parse_args(line.split())
        except SystemExit:
            self.argparser.print_help()
            return

        try:
            cuda_src = os.listdir(self.output_dir)
            cuda_src = [os.path.join(self.output_dir, x) for x in cuda_src if x[-3:] == ".cu"]
            print(f"found sources: {cuda_src}")
            self.compile(self.output_dir, " ".join(cuda_src), self.out)
            output = self.run(timeit=args.timeit)
        except subprocess.CalledProcessError as e:
            for l in e.output.decode("utf8").split("\n"):
                print(l)
            output = None

        return output
