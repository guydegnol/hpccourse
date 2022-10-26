import firebase_admin
from firebase_admin import credentials

from google.cloud import firestore


def evaluate(cell):

    # cred = credentials.Certificate(filename)
    # firebase_admin.initialize_app(cred)

    info = {"egzezehzrh": 0, "egzezehzrh2": "egzeze"}

    # print(f"Add instrument {info['id']} to firebase:{collection} {info}")
    firestore.Client().collection("Blah").document("Mathias").set(info)


import os
import subprocess
import tempfile
import uuid
import argparse

from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring


@magics_class
class Evaluation(Magics):
    def __init__(self, shell):
        super(Evaluation, self).__init__(shell)

        self.argparser = argparse.ArgumentParser(description="Evaluation params")
        self.argparser.add_argument(
            "-t", "--timeit", action="store_true", help="flag to return timeit result instead of stdout"
        )

    @cell_magic
    def evaluate_cell(self, line, cell):
        try:
            args = self.argparser.parse_args(line.split())
        except SystemExit as e:
            self.argparser.print_help()
            return

        print(cell)

        output = None
        return output
