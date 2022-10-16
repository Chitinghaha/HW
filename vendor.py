import json
import yaml


money = int(input('輸入金額'))

with open('inventories.json', 'r' , encoding='utf-16') as f:
  data = json.load(f)

for i in data:
  if (money >= i['price']) & (i['number'] > 0):
    print("name:" + i['name'])
    print("price:" + str(i['price']))
    print("number:" + str(i['number']))

buy_doc = int(input('輸入商品編號'))

print('找零' + str(money - data[buy_doc]['price']) )
data[buy_doc]['number'] = data[buy_doc]['number']-1

with open('inventories.json', 'w' , encoding='utf-16') as f:
    json.dump(data, f)
    f.close()

recording = """
- 'eric'
- 'justin'
- 'mary-kate'
"""

with open('history.yaml', 'w') as file:
    prime_service = yaml.safe_load(file)
