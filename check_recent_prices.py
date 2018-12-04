hourly_price = []
filepath = "hourly_prices.txt"
with open(filepath, encoding="utf8") as fp:
    for line in fp:
        hourly_price.extend(line.strip().split(', '))

for time, price in zip(hourly_price[::2], hourly_price[1::2]):
    print("Time: {} Price: ${} USD".format(time, price))