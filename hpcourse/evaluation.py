import argparse
from google.cloud import firestore

from IPython.core.magic import Magics, cell_magic, magics_class


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
        print("AAAAAAAAAAAAAA")
        print(line)
        print("AAAAAAAAAAAAAA 2")
        print(cell)

        info = {"egzezehzrh": 0, "egzezehzrh2": "egzeze"}

        # print(f"Add instrument {info['id']} to firebase:{collection} {info}")
        firestore.Client().collection("Blah").document("Mathias 2").set(info)

        output = "Done"
        return output
