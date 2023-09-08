f = open("q/data2.csv", "r", encoding='utf8')
count = 0
while f.readline():
    count += 1
print(count)
