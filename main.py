text = '''gcs: G111
gcd: G110
rnd: 333918575.1654972101
url: https://www.binance.com/en
gtm: 2wg680M86QHGF
auid: 71389560.1654971730'''


def clean_dict(data):
    text_list = data.splitlines()
    dic = {}
    for i in text_list:
        dic[i.split(': ')[0]] = i.split(': ')[1]
    return dic


print(clean_dict(text))
