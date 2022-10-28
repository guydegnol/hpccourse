import argparse
import datetime
import os
import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from IPython.core.magic import Magics, cell_magic, magics_class


def get_cred(cred="hpccourse/hpccourse/defzegzbzgh"):

    data = """{
    "type": "service_account",
    "project_id": "ipsastudents-81ae0",
    "private_key_id": "eagezehrzqHHZHZ",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCcR2NDjIoZWeyo\nWBkX74i9gb1/5RoKjzWoUuOXjPQVVJXcQtDID9s4lNKzeh44/pv0S7rypLRlVXDH\nE9pDwkfaButBIX/hipYhyz15s5GCv9K5YDV+TzeciokVkhTKNWfPn41gPwkRCyrk\n3Gl+u+UQVIyVgpkYCULs9Umrfjj1viJKm3y+gaPjxeOIvKmLgdgUZn936ENygkHM\naAkWged6bMBMFHBqJDTSG+cX+kiFcczipI9wel94XMpnpjRmyLGnUUoREBb6frdl\n22mHpz+Z9zi7XeECxNBillEIp72q8vFrTJR3nkQAP8+vwM0edZSujMHg5HMdNFTK\nu56SUacVAgMBAAECggEAP7l+WQeAMnkwHq8ZwGBcxkWWo4WkmkSuMQ5nnp8L0nzU\nxOV74/BPSGGrDyNPGpd7uWB+AT43DxEJdSv7tuCMUvO6TysdTbcoo+wPi8Y0ofed\nMhjwhyo/N3ZoEqMoFhIz2/4n9GSPymLe4UadP9/XNlL7pmWEDsCMCTq2CRdlm5KC\nfUesuic+U4xfhuhMBrA9NVao9wCjHVCtXCAUudZW7oLKnKRNRUa9ah5NSgKCSnWM\nxG/YvMSJQdlvbANLCtLy/+XAM2jSSlKrHWLl6LLTNOGGVmg6TWE5nqKfPFOqYwhJ\nRlPz6o1eIvPaxbxYzf+rgAaacuCQznpkK02AVPqMqwKBgQDQrepKTgS2XIuEXHjX\nqVdxUleUWmtGX9JgD6Y1jTgfkPhQ0aommEiGC4DFML5tFGVsngsAYSx/Vx80FEQ1\nQmGZwnYSPoKxr4u39NgAO7M1nT4NTtRBsbUPT6EF3yLUnkBlEcnjbc/3FPozG8Sl\nDwflESXFh0uI56OYDGtMUiH2hwKBgQC/t4+zssimXQ6I7XjxrtrW0vU6VP3KLB43\nvqZQr0tpYc0OFUx5Bbx8J2LuDjmDGVbWAsDkE9ZnS0iU/C2Dre1i7Dh6qZg3/Bhj\nNR8kMYVd80VWA/Tm7r3Awl9WBqLVvXQXWSsTCFjX5/jKcbotPVCd5AgUv9cPh+eg\nopMOYSuAgwKBgFOLrWc+QQi5mGnPk9nTxFxsOP/+C0DLkDBBU6vQ9A0/PwssRdDZ\n2v8/j7hiwXpuVgTcaU8nmGcK/EUfcAdaojSq9BZtzGlS/L8TWX8OZ7spTvSJANWk\nTfbpTHBLW2iASwuryYYyKrajQWBA18O1dtWwvcyNVCJlisuO/U46+7n1AoGBAKRh\n/wwkcpj611iezYHk3G0wSuYuM8Gi3HINvUsXUsDUA99cccqfGYMWvmPBvJxlIKi1\nibDGNaMx0NU1+MycWBvm0XKTchomxL5jsQT2lRT+Xugm0lkkQX1C7D21yO8d16mh\nYiaalJrjotXqd6kMltAa0rb/2qXNcNSyMQc2V/eDAoGAYVpmuJEJCSBj5GQnHgH6\n4bHjIriNmg33lx2goxQOoPkrla9z2Ork0+jM1CjYgKArMmFS+30c+mEj5Vv5Ybbu\np8QG6n8/N1I+Pd+Ps0InmyybN3tLaVQFkfdSfhOxa56NBd1vOsVSj2m/gTaLCm2o\n4i8UEuRjzbwJPN/uM+0JKjc=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-fzzb4@ipsastudents-81ae0.iam.gserviceaccount.com",
    "client_id": "egzezqh234ehzqh22",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fzzb4%40ipsastudents-81ae0.iam.gserviceaccount.com"
}"""

    # u = b"eNqVlkmvo0gChO_8ilJJc6Kr2DG0NFKzGTCLwey-PLGZfTE7tPq_z_PrV5qZ6plD5wEk8osgMhGK_B348j6-Tnuffv31y9cxHZYiTt_COO7mdvr6y5_T_dCVaTy9FckLKvoxHKc5Sdtp_EYhYQr_myuWcErfqnT_ZNMwS480H46nJN2l-_8AX9S312AFUda_GDfZZWzhiyIEH08BTZaFxZRZhmd0NqueeVWI9AqzjCmcGcbiWCVes8wqmUxgmO6dM7n4hup8KXd3L907wGMr_4QXdBYhEHHrlPLwOme--qVhuu7Fj82Jl3l6xGtdeU-K41C_wNZp2Hv1Vrs-LwEC3fNr9QjZeWJlH8qLPsj3AyFGQuQWWiEC3gXtI42LrnKr3FZ072G0OJIZa3Xj9qECMLEGZ9AxXXl3s74KOEcdaacZHmWJLMVFabAdzEKj3NKrvCiNmiWZc29pjBT0PaskDQiZysvShIw0VjtL7PPC25YIxj5YFec4Popepte0pnFf69u-vDW7KraO090ENiIfQ1IDKNpI_QHe6aM4-anAbTpb1LUg9yf0SS3nwb7csLYyGYMCl1WD0-RuzaUmZYSkJfrZVoCZIC0njF0m01iGEbjsfbeNUw16ZspobbVKT-q-imy8VZ7X4V7VVNasmUTb9pQKt4cDbFf3hEOsYYniwO-6IfbJafZYkLFxjN-ES2Itp2nmNGe5kvY-JnYUdx24GgUVwN0jTQAtL9d87yAdu3fCU-vOuXygEN7SomXsjZriTpgYNOTrtXrqG0_gR07j7CfK3ZK6IRQOeDjpOBcx6ODbI59zjR0YWnfDjl65UnK5yecYZ07u3qlTlVa56TcnpMOc0K1M4azW04BNhIJFsy5mUi8Ro6vcpO4Q6DMaWlpWrQySp9akqtr6VRTdJiNtTyDap_IwztdnsOYX4FYbB9khqbwY4RZtwfEAh4wJw3jmzKPtKwVGGdd4as9VYTOTN4e0V-zMQn15Fnyp9IGnm2xOnTpeM4k-fcl4MkBKO3tURm7CYdc0QiFyOH_WVGI6i-7YZiMTWBvkbhR8FkwEMBvxvraBZXTKNuAzRusZcz1pSGvjuj3d2DFyDJsUztiuOm3F1kLcllEMYWejO0TKqgF-fdSC5Z9zeJYJ8hrw4qQ5hYTmH5E5aMLBYxyLxjdJ-eSX2zANHrw4pGtgisriGLA87-YAT30Qw9ezsxFstFEXVJ35suFFN_KYka8E-t5acOFAHMoPKVKc-Jx83jMMYvMS0G9UpQVuQsGux0B2cxowZq1pj32q7uKbvmeNNncufQIqlTjqJsPlEoLJnIWOjRxMM6DrtWtgzUz2iny-qoMXg6ZZEI3YGhXd2tt5G68GBHIwr1Y8yzrkYtIMDBnrON4S_g6gCwWVp7xY_X52MzsOHaptxFiBBOcRM0nYldaTZu_TIdYWpFK251PX-2ns7cW6MLpXAfYj6m2JVT20YKx1HvYg2JUhLE2PZRDqiiSTty7xrrvcpS7G-Qo5OAmeWoTpRJZRbjkArWsV9yWJIEV6BFKFifBqzcGsUWKBSbK-OKPvjLzD0HQcx8-HGGje0hjsctlqWSkQoIh4UQ-1DdYdBNT22GOXBvYVO867ZlOJcjRttL7ZoD9nDVxXlekj3IlHkf1KJQjZ5EBQhGF9Gcpu8p8JWWn1xITwEEHo09dj3do1M0ZdKOXfIzOB2zfzRbhwFlsSotlKmUQCeCSV8lDoTYZh9YZm3WZeO6Ma6pA-0OtQwWCpIVwZZAozaM3ZAjE4BhuhJNyFCKJoBnrKFMmWgnREBo0ENEZYbpt9j3RsUkPXPFePxHrk1y0kSJ1NkOU6ulaJNlBmhyrXoB2AF5QjzLfyiNaLoUOzBsIXpYz_CXz0jqDzf-2iH_UV18V7-b2lTVjUr_56FEMahWP6LUyaoh2T6tvjOCL8t7825fcibL5nnzX72bLf4675yfmzPLMjPZ45iuFp_rqjP6hwnvK3eSheUD5N_fgrBH2ajd-zrsvq9GUKdVD3QlHodf0hnroqbX9W_8l9asO-GD_0H-h_vfT9JLAUSTq8bQRMv8XpML071f_ptK7rzzafIRYEegnGn9b6d5yG7v2Pfhk16RQm4RRCLzX0f_b_Hzj8N74A8Me_AFV5-bI="
    # data = zlib.decompress(b64d(u)).decode("utf-8")

    os.system(f"rm -rf {cred}")
    with open(cred, "w") as f:
        f.write(
            data.replace("eagezehrzqHHZHZ", "c77a63d9bde3c31b604df1585c8f1e6364f5cff7").replace(
                "egzezqh234ehzqh22", "109804974142774577736"
            )
        )
    return cred


def set_up_student(student_name):
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
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_cred()
    return student_name


@magics_class
class Evaluation(Magics):
    def __init__(self, shell):
        super(Evaluation, self).__init__(shell)

        self.argparser = argparse.ArgumentParser(description="Evaluation params")
        self.argparser.add_argument(
            "-t", "--timeit", action="store_true", help="flag to return timeit result instead of stdout"
        )

    @cell_magic
    def ipsa_question(self, line, cell):
        from google.cloud import firestore

        if "STUDENT" not in os.environ:
            set_up_student(None)

        firestore.Client().collection(line).document(os.environ["STUDENT"]).set(
            {"answer": cell, "update_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )

        output = f'Answer has been submited for: {line}/{os.environ["STUDENT"]}. You can resubmit it several times'
        print(output)
        return None

    @cell_magic
    def ipsa_solution(self, line, cell):
        from google.cloud import firestore

        if "STUDENT" not in os.environ:
            set_up_student(None)

        out = firestore.Client().collection(line).document("solution").get()

        output = f'Answer has been submited for: {line}/{os.environ["STUDENT"]}. You can resubmit it several times'
        print(output)
        return out
