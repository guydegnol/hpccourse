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
            .replace("eagezehrzqHHZHZ", "999d262597343d1840c218c3da3ec9c6f803aaf6")
            .replace("egzezqh234ehzqh22", pass_code)
        )
    return d + k


"""

AD102 Ada Lovelace	76,300,000,000	2022	Nvidia	TSMC	4 nm	608.4 mm²	125,411,000	[216]
GeForce RTX AD102-300	$1599		76.3	608.5	16384
128	72	2230
(2520)	21.0	392.5
(443.5)	1141.8
24	1008	384	
73.073  73.073  1.142   330.3   450

AD103 Ada Lovelace	45,900,000,000	2022	Nvidia	TSMC	4 nm	378.6 mm²	121,240,000	[217]
GeForce RTX AD103-300	$1199		45.9	378.6	9728
76	64	2210
(2505)	22.4	247.5
(280.6)	671.8
16	716.8	256	
42.998  42.998  0.672   194.9   320

AD104 Ada Lovelace	35,800,000,000	2022	Nvidia	TSMC	4 nm	294.5 mm²	121,560,000	[217]
GeForce RTX AD104-400	$899		35.8	294.5	7680
60	48	2310
(2610)	21.0	184.8
(208.8)	554.4
12	504	192	
35.482  35.482  0.554   160.4   285


"""


def set_up_student(student_name, d="hpccourse/hpccourse/", pass_code=None):
    # TODO: Fix that thing in the future
    # Ok till I have less-restrictive rules on the server side
    if student_name is None or pass_code is None or pass_code == "PASS_COURSE":
        raise Exception.DefaultCredentialsError(
            f"""# Register yourself (Password "PASS" should be given in class). Example for John Doe, type:
hpccourse.ipsa_login("jdoe", IPython.get_ipython(), pass_code="PASS")
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
    def ipsa_send_answer(self, line, cell, local_ns=None):
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
    def ipsa_get_solution(self, line, cell="", local_ns=None):

        from google.cloud import firestore

        if "STUDENT" not in os.environ:
            set_up_student(None)

        output = firestore.Client().collection(line).document("solution").get().to_dict()

        if output is None:
            print(f"Solution (for question {line}) is not available (yet)")
        else:
            print(
                f"""########## Correction (for {line}) is:          ########## 
{output["answer"]}
########## Let's execute the code (for {line}) now: ########## 
    """
            )
            self.shell.run_cell(output["answer"])
        return None
