import pandas as pd
import tqdm

f = open("q/data2.csv", "r", encoding='utf8')
data_map = {}
f.readline()  # del first line

qbar = tqdm.tqdm(total=878503)
while d := f.readline():
    data = d.split(',')
    qbar.update(1)

    # List format:
    # [date,time,item_id,quantity,price(cny/kg),type,discount]

    item_id = data[2]
    quantity = data[3]
    date = data[0]
    if item_id not in data_map:  # check if item_id is in map.
        data_map[item_id] = {}
    if date not in data_map[item_id]:
        data_map[item_id][date] = 0.
    data_map[item_id][date] += float(quantity)

print(data := pd.DataFrame(data_map))
data.corr().to_excel("q/corr.xlsx")
