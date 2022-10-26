import argparse
import datetime
import os

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
    def ipsa_evaluation(self, line, cell):
        if "STUDENT" not in os.environ:
            raise IOError(
                f"""Register yourself for the evaluation before. Ex:
    # John Doe, jdoe, ...
    hpcourse.ipsa_login("jdoe", IPython.get_ipython())
    """
            )

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hpcgpu_course/hpcourse/ipsastudents.json"
        firestore.Client().collection(line).document(os.environ["STUDENT"]).set(
            {"answer": cell, "update_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )

        output = f'Answer has been submited for {line}/{os.environ["STUDENT"]}. You can resubmit it several times'
        print(output)
        return None
