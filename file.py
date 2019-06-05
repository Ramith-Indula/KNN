import yaml
import io
import numpy as np
import pandas as pd


def getattributes():
    data_dict = dict()
    attrs = ['total_nom',
             'dit_sum',
             'noc_sum',
             'cbo_sum',
             'rfc_sum',
             'lcom4_sum',
             'npm_sum',
             'total_loc'

             ]

    stream = open("/home/ramith/Desktop/.Temp/metrics.yaml", "r")
    docs = yaml.load_all(stream)
    for doc in docs:
        for k, v in doc.items():
            if (k in attrs):
                data_dict[k] = [v]
        break

    data_dict
    arr = []
    dict_key = list(data_dict)
    for k in list(attrs):
        arr.append(data_dict[k][0])
    data = np.array(arr)
    # print(data)
    # df = pd.DataFrame.from_dict(data_dict)
    return data
