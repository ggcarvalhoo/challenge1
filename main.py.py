from decimal import Decimal
import os, sys
import json
import re

json_file_path = r'processos'
files = os.listdir(json_file_path)

# print(files)

decodedJson = []
money_list = []
for file in files:
    f = open(f'processos/{file}', encoding='utf8')
    file_load = json.load(f)
    for key in file_load['instances']:
        money = key['valor']

        trim = re.compile(r'[^\d.,]+')
        result = trim.sub('', money)
        maketrans = result.maketrans
        result = result.translate(maketrans(',.', '.,'))
        result_final = float(result.replace(',', ''))
        money_list.append(result_final)

amount = sum(money_list)
amount_final = round(amount, 2)
print(amount_final)