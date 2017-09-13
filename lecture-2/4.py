prices = []

while True:
    price_srt = input('Enter price: ')
    if price_srt == 'stop' and len(prices) < 4:
        print('Enter atleast 4 prices')
        continue
    else:
        if price_srt == 'stop':
            break
    try:
        price_srt = float(price_srt)
    except:
        print('All prices must be in numbers.')

    else:
        prices.append(float(price_srt))

price_max = max(prices)
price_min = min(prices)

while (price_max in prices) and (price_min in prices):
    prices.remove(price_max)
    prices.remove(price_min)

if len(prices) == 0:
    print('No middle price!')
else:
    print(sum(prices) / len(prices))
