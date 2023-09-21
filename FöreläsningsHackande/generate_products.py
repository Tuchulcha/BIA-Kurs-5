import csv
import random

NUMBER_OF_ROWS = 1000

product_property = ["Blue", "Large", "Slim", "Magnificent", "Fantastic",
                    "Awesome", "Incredible", "Amazing", "Stunning", "Beautiful", "Slimy"]
product_name = ["Shirt", "Pants", "Shoes", "Hat", "Gloves",
                "Socks", "Jacket", "Coat", "Scarf", "Tie"]


def random_price():
    price = random.randint(10, 99)
    price = f"{price}9"

    if random.randint(0, 10) == 0:
        price = None

    return price


def random_product_name():
    name = random.choice(product_property) + " " + \
        random.choice(product_property) + " " + random.choice(product_name)
    return name


def random_size():
    size = random.choice(["XS", "S", "M", "L", "XL"])
    return size


def random_color():
    color = random.choice(["Red", "Blue", "Green", "Yellow", "Black", "White"])
    return color


product_id = 0

with open("product_data.csv", "w", newline="") as csvfile:
    fieldnames = ["product_id", "product_name", "price", "size", "color"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(NUMBER_OF_ROWS):
        product_id += 1

        row = {
            "product_id": product_id,
            "product_name": random_product_name(),
            "price": random_price(),
            "size": random_size(),
            "color": random_color()
        }

        writer.writerow(row)
