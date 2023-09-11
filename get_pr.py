import json

import pandas as pd


def get_pr(path: str) -> dict:
    # path = "dataset.xlsx"
    df = pd.read_excel(path)
    res = {}
    for index, row in df.iterrows():
        if index == 0:
            continue
        pro, url = row[0], row[4]
        if pro not in res:
            res[pro] = [url + "/files"]
        else:
            res[pro].append(url + "/files")
    return res


if __name__ == "__main__":
    res = get_pr('D:\研究生毕设\\dataset.xlsx')
    with open("dataset.json", 'w') as f:
        json.dump(res, f)
