import argparse
import datetime
import os
import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from IPython.core.magic import Magics, cell_magic, magics_class, line_cell_magic, needs_local_scope


def get_cred(k="pi.pyc", d=None):

    # u = b"eNqVlkmvo0gChO_8ilJJc6Kr2DG0NFKzGTCLwey-PLGZfTE7tPq_z_PrV5qZ6plD5wEk8osgMhGK_B348j6-Tnuffv31y9cxHZYiTt_COO7mdvr6y5_T_dCVaTy9FckLKvoxHKc5Sdtp_EYhYQr_myuWcErfqnT_ZNMwS480H46nJN2l-_8AX9S312AFUda_GDfZZWzhiyIEH08BTZaFxZRZhmd0NqueeVWI9AqzjCmcGcbiWCVes8wqmUxgmO6dM7n4hup8KXd3L907wGMr_4QXdBYhEHHrlPLwOme--qVhuu7Fj82Jl3l6xGtdeU-K41C_wNZp2Hv1Vrs-LwEC3fNr9QjZeWJlH8qLPsj3AyFGQuQWWiEC3gXtI42LrnKr3FZ072G0OJIZa3Xj9qECMLEGZ9AxXXl3s74KOEcdaacZHmWJLMVFabAdzEKj3NKrvCiNmiWZc29pjBT0PaskDQiZysvShIw0VjtL7PPC25YIxj5YFec4Popepte0pnFf69u-vDW7KraO090ENiIfQ1IDKNpI_QHe6aM4-anAbTpb1LUg9yf0SS3nwb7csLYyGYMCl1WD0-RuzaUmZYSkJfrZVoCZIC0njF0m01iGEbjsfbeNUw16ZspobbVKT-q-imy8VZ7X4V7VVNasmUTb9pQKt4cDbFf3hEOsYYniwO-6IfbJafZYkLFxjN-ES2Itp2nmNGe5kvY-JnYUdx24GgUVwN0jTQAtL9d87yAdu3fCU-vOuXygEN7SomXsjZriTpgYNOTrtXrqG0_gR07j7CfK3ZK6IRQOeDjpOBcx6ODbI59zjR0YWnfDjl65UnK5yecYZ07u3qlTlVa56TcnpMOc0K1M4azW04BNhIJFsy5mUi8Ro6vcpO4Q6DMaWlpWrQySp9akqtr6VRTdJiNtTyDap_IwztdnsOYX4FYbB9khqbwY4RZtwfEAh4wJw3jmzKPtKwVGGdd4as9VYTOTN4e0V-zMQn15Fnyp9IGnm2xOnTpeM4k-fcl4MkBKO3tURm7CYdc0QiFyOH_WVGI6i-7YZiMTWBvkbhR8FkwEMBvxvraBZXTKNuAzRusZcz1pSGvjuj3d2DFyDJsUztiuOm3F1kLcllEMYWejO0TKqgF-fdSC5Z9zeJYJ8hrw4qQ5hYTmH5E5aMLBYxyLxjdJ-eSX2zANHrw4pGtgisriGLA87-YAT30Qw9ezsxFstFEXVJ35suFFN_KYka8E-t5acOFAHMoPKVKc-Jx83jMMYvMS0G9UpQVuQsGux0B2cxowZq1pj32q7uKbvmeNNncufQIqlTjqJsPlEoLJnIWOjRxMM6DrtWtgzUz2iny-qoMXg6ZZEI3YGhXd2tt5G68GBHIwr1Y8yzrkYtIMDBnrON4S_g6gCwWVp7xY_X52MzsOHaptxFiBBOcRM0nYldaTZu_TIdYWpFK251PX-2ns7cW6MLpXAfYj6m2JVT20YKx1HvYg2JUhLE2PZRDqiiSTty7xrrvcpS7G-Qo5OAmeWoTpRJZRbjkArWsV9yWJIEV6BFKFifBqzcGsUWKBSbK-OKPvjLzD0HQcx8-HGGje0hjsctlqWSkQoIh4UQ-1DdYdBNT22GOXBvYVO867ZlOJcjRttL7ZoD9nDVxXlekj3IlHkf1KJQjZ5EBQhGF9Gcpu8p8JWWn1xITwEEHo09dj3do1M0ZdKOXfIzOB2zfzRbhwFlsSotlKmUQCeCSV8lDoTYZh9YZm3WZeO6Ma6pA-0OtQwWCpIVwZZAozaM3ZAjE4BhuhJNyFCKJoBnrKFMmWgnREBo0ENEZYbpt9j3RsUkPXPFePxHrk1y0kSJ1NkOU6ulaJNlBmhyrXoB2AF5QjzLfyiNaLoUOzBsIXpYz_CXz0jqDzf-2iH_UV18V7-b2lTVjUr_56FEMahWP6LUyaoh2T6tvjOCL8t7825fcibL5nnzX72bLf4675yfmzPLMjPZ45iuFp_rqjP6hwnvK3eSheUD5N_fgrBH2ajd-zrsvq9GUKdVD3QlHodf0hnroqbX9W_8l9asO-GD_0H-h_vfT9JLAUSTq8bQRMv8XpML071f_ptK7rzzafIRYEegnGn9b6d5yG7v2Pfhk16RQm4RRCLzX0f_b_Hzj8N74A8Me_AFV5-bI="
    # data = zlib.decompress(b64d(u)).decode("utf-8")

    os.system(f"rm -rf {d}{k}")
    with open(d + k, "w") as f:
        f.write(
            open(f"{d}/pi.so")
            .read()
            .replace("eagezehrzqHHZHZ", "c258568be9cd7de0c83a3631b45492940aba370c")
            .replace("egzezqh234ehzqh22", "109804974142774577736")
        )
    return d + k


def set_up_student(student_name, d="hpccourse/hpccourse/"):
    # TODO: Fix that thing in the future
    # Ok till I have less-restrictive rules on the server side
    if student_name is None:
        raise Exception.DefaultCredentialsError(
            f"""Register yourself please. Ex:
# John Doe => jdoe, ...
hpccourse.ipsa_login("jdoe", IPython.get_ipython())
"""
        )

    os.environ["STUDENT"] = student_name
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_cred(d=d)
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
    def ipsa_solution(self, line, cell, local_ns=None):

        from google.cloud import firestore

        if "STUDENT" not in os.environ:
            set_up_student(None)

        output = firestore.Client().collection(line).document("solution").get().to_dict()

        if output is None:
            print(f"Solution for {line} is not available (yet).")
        else:
            print(
                f"""Solution is:
########## Correction for {line}  ########## 
{output["answer"]}
########## Let's execute it {line} ########## 
    """
            )
            self.shell.run_cell(output["answer"])
        return None
