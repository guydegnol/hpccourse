import argparse
from google.cloud import firestore
import os

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
    def ipsa_evaluate(self, line, cell):
        if "STUDENT" not in os.environ:
            raise IOError(
                f"""Register yourself for the evaluation before. Ex:
    # Guillaume Therin, gtherin, ...
    hpcourse.ipsa_login("gtherin", IPython.get_ipython())
    """
            )

        firestore.Client().collection(line).document(os.environ["STUDENT"]).set({"answer": cell})

        output = f'Answer has been submited for {line}/{os.environ["STUDENT"]}. You can resubmit it several times'
        print(output)
        return cell
