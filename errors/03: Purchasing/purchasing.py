def process_transactions(purchase_orders):
    leftovers = []

    for order in purchase_orders:
        try:
            leftover = purchase_item(order["price"], order["gold_available"])
            leftovers.append(leftover)
        except Exception as err:
            print(err)

    return leftovers


def main():
    print("Processing transactions...")
    leftovers = process_transactions(
        [
            {"price": 10.00, "gold_available": 125.00},
            {"price": 5.00, "gold_available": 2.00},
            {"price": 20.01, "gold_available": 5.20},
            {"price": 1.04, "gold_available": 254.00},
            {"price": 40.20, "gold_available": 6.00},
            {"price": 16.00, "gold_available": 235.01},
            {"price": 10.70, "gold_available": 10.70},
            {"price": 12.00, "gold_available": 2.30},
        ]
    )
    print("Transactions complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")


def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception(f"{gold_available:.2f} is not enough for {price:.2f}")
    return gold_available - price


main()