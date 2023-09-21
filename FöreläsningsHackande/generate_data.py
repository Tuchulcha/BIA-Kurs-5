import csv
import random

NUMBER_OF_ROWS = 1000

first_names = ["Linus", "Bill", "Steve", "Mark", "Elon",
               "Jeff", "Larry", "Sergey", "Sundar", "Satya"]
last_names = ["Torvalds", "Gates", "Jobs", "Zuckerberg", "Musk",
              "Bezos", "Page", "Brin", "Pichai", "Nadella"]


def random_email(first_name, last_name):
    email = first_name.lower() + "." + last_name.lower() + "@example.com"

    email = "invalid_email" if random.randint(0, 5) == 0 else email

    return email


def random_age():
    age = random.randint(0, 100)

    if random.randint(0, 5) == 0:
        age = None

    return age


def random_person(customer_id):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    name = first_name + " " + last_name
    email = random_email(first_name, last_name)
    age = random_age()
    purchase_frequency = random.choice(["high", "medium", "low"])
    phone = f"07{random.randint(10,99)}-{random.randint(100000,999999)}"

    return {
        "customer_id": customer_id,
        "name": name,
        "email": email,
        "age": age,
        "purchase_frequency": purchase_frequency,
        "phone": phone
    }


with open("customer_data.csv", "w", newline="") as csvfile:
    fieldnames = ["customer_id", "name", "email", "age", "purchase_frequency", "phone"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    customer_id = 0
    for i in range(NUMBER_OF_ROWS):
        customer_id += 1
        row = random_person(customer_id)
        writer.writerow(row)