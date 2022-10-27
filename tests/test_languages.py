import hpccourse

from hpccourse import languages


def test_languages():
    instrs = grodt.Instruments.get_list()
    data = dapir.get_data("ILIAD", task="Normalize", use_cache=True)

    from grodt.models import model

    print(data.columns)
    model.calculate_preds(data, instrs["ILIAD"])

    print(data.columns)
