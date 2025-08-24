items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

for key, value in items_purchase.items():
    clean_price = value.replace(",", "").strip("$")
    items_purchase[key] = clean_price

clean_wallet = int(wallet.replace(",", "").strip("$"))

cart = []
for key, value in items_purchase.items():
    if int(value) <= clean_wallet:
        cart.append(key)

if cart == []:
    print("Nothing")
else:
    print(sorted(cart))