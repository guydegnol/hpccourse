import pandas as pd
import hpccourse


def test_languages():

    df = hpccourse.get_languages_perf()
    print(df)
