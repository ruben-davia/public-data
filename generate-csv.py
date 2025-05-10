import csv
import random
from datetime import datetime, timedelta
import string

# Lists of common first names and last names
first_names = [
    "James",
    "Mary",
    "John",
    "Patricia",
    "Robert",
    "Jennifer",
    "Michael",
    "Linda",
    "William",
    "Elizabeth",
    "David",
    "Barbara",
    "Richard",
    "Susan",
    "Joseph",
    "Jessica",
    "Thomas",
    "Sarah",
    "Charles",
    "Karen",
    "Christopher",
    "Nancy",
    "Daniel",
    "Lisa",
    "Matthew",
    "Margaret",
    "Anthony",
    "Betty",
    "Mark",
    "Sandra",
    "Donald",
    "Ashley",
    "Steven",
    "Kimberly",
    "Paul",
    "Emily",
    "Andrew",
    "Donna",
    "Joshua",
    "Michelle",
]

last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzalez",
    "Wilson",
    "Anderson",
    "Thomas",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
    "Lee",
    "Perez",
    "Thompson",
    "White",
    "Harris",
    "Sanchez",
    "Clark",
    "Ramirez",
    "Lewis",
    "Robinson",
    "Walker",
    "Young",
    "Allen",
    "King",
    "Wright",
    "Scott",
    "Torres",
    "Nguyen",
    "Hill",
    "Flores",
]


def generate_random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"


def generate_random_date(start_date=datetime(2020, 1, 1)):
    days_between = (datetime.now() - start_date).days
    random_days = random.randint(0, days_between)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")


# Define the number of rows to generate
num_rows = 100

# Define the column headers
headers = ["id", "name", "age", "email", "join_date", "score"]

# Generate the data
data = []
for i in range(num_rows):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    row = [
        i + 1,  # id
        f"{first_name} {last_name}",  # name
        random.randint(18, 80),  # age
        email,  # email
        generate_random_date(),  # join_date
        round(random.uniform(0, 100), 2),  # score
    ]
    data.append(row)

# Write to CSV file
with open("random_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Generated random_data.csv with {num_rows} rows")
