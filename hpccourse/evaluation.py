import argparse
import datetime
import os
import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from IPython.core.magic import Magics, cell_magic, magics_class, line_cell_magic, needs_local_scope


def get_cred(k="pi.pyc", d=None, pass_code=None):
    os.system(f"rm -rf {d}{k}")
    with open(d + k, "w") as f:
        f.write(
            open(f"{d}/pi.so")
            .read()
            .replace("eagezehrzqHHZHZ", "c258568be9cd7de0c83a3631b45492940aba370c")
            .replace("egzezqh234ehzqh22", pass_code)
        )
    return d + k


def set_up_student(student_name, d="hpccourse/hpccourse/", pass_code=None):
    # TODO: Fix that thing in the future
    # Ok till I have less-restrictive rules on the server side
    if student_name is None or pass_code is None or pass_code == "PASS_COURSE":
        raise Exception.DefaultCredentialsError(
            f"""Register yourself please. Ex:
# John Doe => jdoe, ...
# Don't forget to take the password in class
hpccourse.ipsa_login("jdoe", IPython.get_ipython(), p="PASS")
"""
        )

    os.environ["STUDENT"] = student_name
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_cred(d=d, pass_code=pass_code)
    return student_name


def get_solution(sid):

    if "STUDENT" not in os.environ:
        set_up_student(None)

    from google.cloud import firestore

    output = firestore.Client().collection(sid).document("solution").get().to_dict()


@magics_class
class Evaluation(Magics):
    def __init__(self, shell):
        super(Evaluation, self).__init__(shell)

        self.argparser = argparse.ArgumentParser(description="Evaluation params")
        self.argparser.add_argument(
            "-t", "--timeit", action="store_true", help="flag to return timeit result instead of stdout"
        )

    @cell_magic
    @needs_local_scope
    def ipsa_question(self, line, cell, local_ns=None):
        from google.cloud import firestore

        if "STUDENT" not in os.environ:
            set_up_student(None)

        firestore.Client().collection(line).document(os.environ["STUDENT"]).set(
            {"answer": cell, "update_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )

        self.shell.run_cell(cell)
        print(f'Answer has been submited for: {line}/{os.environ["STUDENT"]}. You can resubmit it several times')
        return None

    @line_cell_magic
    @needs_local_scope
    def ipsa_solution(self, line, cell="", local_ns=None):

        from google.cloud import firestore

        if "STUDENT" not in os.environ:
            set_up_student(None)

        output = firestore.Client().collection(line).document("solution").get().to_dict()

        if output is None:
            print(f"Solution for {line} is not available (yet).")
        else:
            print(
                f"""########## Correction for {line} is:          ########## 
{output["answer"]}
########## Let's execute the code {line} now: ########## 
    """
            )
            self.shell.run_cell(output["answer"])
        return None
