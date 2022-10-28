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
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1E54fc8hXLN3f\nCpIIdmXfn7sO2KxYBpS9lhiqT9N6kkeFyM5X5uNplhhrHdggzvWempHpPkONNf/I\nmhe7L+bh0oONYDk0gW6InXCUy1yau7+GoZ9AdXgakxOeaslyI1yCkITtoPMfbnhP\nLjS+oD/VHQFQqQNjMMfF3vQ3tZIOuCV6kXWubcyZK8nG0uyGmfzNTcSCokUgefTG\n00x34D/M+MwHj+cy5+rVBjYX2+FYeo5SCnA99PMMdsyrFVMwt3vF7jFUxAwto1oF\njmg9QP41Xh0QEnMNyV7DmIIsAwoGAuxmJciB3FPkH0rT5VsWTF9v5B87ClOo8zMM\na60ikILVAgMBAAECggEAIGAFDf+QCtIZS0cjDANLPJvdAI8J5WUr0+fRuiWynIAp\n7IgWKI4+C8NL018PJPKL5NMjEm5Q+p70gCPY6V1rrOWMIstY/wPDRQbNObVQddPq\nrwIXrJk0I6A3SkQyh0c+Q5PeSHRV88E3HoUW5hxVvV9FvGuzkNkIZt7xkEJU/m9u\nMwVXcWz+n/v/00JwLlq3cQ19IIQaaVzxKl5BT2+5/lPW+aBnf/RKv/cx77yXnGjK\nkLKa7GqSVkvRPl4I0udSaJO9NHhzE33j1WMnxOjl+ep5bcvQElLopjOLXOART4x/\nNnT8tFIUWFtZdp2R0y7lOIq/md6CW5MF6BHQcAAsgQKBgQDdUYPiGNnyxUNlGzey\nZy0r/VSZ4fsZJS4IUtTpgvbz1fwump2Xf/HqKwx3cpGjksakQ3t5qPbb+d+MDhse\nhlNVbsGiMpNphTqiF6oABx+2OpfNYc0wKu0zDenlsYJi9Xc6/3htQIgYFv4Xcj1c\niv/kGEKMt3MPPhPw+9H6Y5XbwQKBgQDRc7/SSstakMn/ErMhMvhUETkOW0gacE4Q\naFb2yOMxHOKcD5J+4dbz3dUK8zsdeHDPSzFjE7hTM0WE+HKMpcGeQO4OxiGoZOaI\nNTme1xExXw53cAVyd6drjp09ruqnRQcoyeTbX8R+g7egNJg+UqdkXCSy6Vraf4gb\nr/lppdR8FQKBgQCetlRTkerKVHhuS0R35dHZGATRjeNaNvV59pzFEKw0VKJScYLO\nIGzFtzVre3fBzAIzzkkACBFv0xNjBsKf80hTneeyf36DT42qrDm3Z2RwdDhkitxw\nzHfqAvJXTCLrAIkOgCJGht6SF/sDqWMjuHKlilg/PVd/+M6oJI6Cd2QCgQKBgF2T\nuT/a6r+rsJOlZyKOAySMDVG8tpoZUsdB1pirZ9WpchUHYAwQGlkZ4vThdqfUB5KV\npZr+VHvXjFe8KHFuHPL3T2SKYL87VUPFg9jTfXrxXSU/hy99Be+n59iHLY9N58Tx\nbq4UO1XKw19wIBS4GNFd2YeVemHkWIsGNAhfbm+BAoGBAJn2ihnQXHO0ZhDJ+pyG\nhHdovfUxMKAhYMjqxHtgFVYf9M1B3JiZ4uPQ0eOjqJcxCGmsanPvwPMo1gBHnnq/\nl9h4fRaB2G6l5K9KhWxPGdPlC/7ViNJ5nI1k2TOH0MGf/YXlKTjAEr621IJ3jdGJ\nsGamFkUqi9IqQalQ6/gsUtov\n-----END PRIVATE KEY-----\n",
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
            data.replace("eagezehrzqHHZHZ", "c258568be9cd7de0c83a3631b45492940aba370c").replace(
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
