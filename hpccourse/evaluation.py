import argparse
import datetime
import os

from google.cloud import firestore

from IPython.core.magic import Magics, cell_magic, magics_class


def set_up_student(student_name):
    # TODO: Fix that thing in the future
    # Ok till I have less-restrictive rules on the server side
    cred = "hpccourse/hpccourse/defzegzbzgh"
    c = (
        open("hpccourse/hpccourse/ipsastudents.json", "r")
        .read()
        .replace("eagezehrzqHHZHZ", "c77a63d9bde3c31b604df1585c8f1e6364f5cff7")
        .replace("egzezqh234ehzqh22", "109804974142774577736")
    )

    os.system(f"rm -rf {cred}")
    with open(cred, "w") as f:
        f.write(c)

    os.environ["STUDENT"] = student_name
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred


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
    hpccourse.ipsa_login("jdoe", IPython.get_ipython())
    """
            )

        firestore.Client().collection(line).document(os.environ["STUDENT"]).set(
            {"answer": cell, "update_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )

        output = f'Answer has been submited for {line}/{os.environ["STUDENT"]}. You can resubmit it several times'
        print(output)
        return None
