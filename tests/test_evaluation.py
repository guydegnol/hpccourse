import hpccourse


import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d


def obscure(data: bytes) -> bytes:
    return b64e(zlib.compress(data, 9))


def unobscure(obscured: bytes) -> bytes:
    return zlib.decompress(b64d(obscured))


def test_evaluation():

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

    # Obsure
    b = data.encode("utf-8")
    u = obscure(b)
    print(u)

    # Unobscure
    d = unobscure(u)
    d = d.decode("utf-8")
    print(d)

    if d != data:
        raise Exception("It does not work")
