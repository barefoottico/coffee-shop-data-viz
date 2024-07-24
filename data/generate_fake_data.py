#!/usr/bin/env python3

import pandas as pd
from faker import Faker
import random
import os

# Directory for saving data
data_dir = '/Users/anthonytatis/gitfolder/publicstash/open_source_project/coffee-shop-data-viz/data'

# Ensure the directory exists
os.makedirs(data_dir, exist_ok=True)

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 100

# Generate Customers
def generate_customers(num_records):
    customers = []
    for _ in range(num_records):
        customers.append({
            'customer_id': _ + 1,
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address_id': random.randint(1, num_records),
            'registration_date': fake.date_this_decade(),
            'loyalty_points': random.randint(0, 100)
        })
    return customers

# Generate Addresses
def generate_addresses(num_records):
    addresses = []
    for _ in range(num_records):
        addresses.append({
            'address_id': _ + 1,
            'street': fake.street_address(),
            'city': fake.city(),
            'state': fake.state(),
            'postal_code': fake.zipcode(),
            'country': fake.country()
        })
    return addresses

# Generate Items
def generate_items(num_records):
    categories = ['Coffee', 'Pastry', 'Sandwich', 'Beverage']
    items = []
    for _ in range(num_records):
        items.append({
            'item_id': _ + 1,
            'item_name': fake.word(),
            'item_category': random.choice(categories),
            'price': round(random.uniform(1.0, 10.0), 2)
        })
    return items

# Generate Ingredients
def generate_ingredients(num_records):
    ingredients = []
    for _ in range(num_records):
        ingredients.append({
            'ingredient_id': _ + 1,
            'ingredient_name': fake.word(),
            'unit_of_measure': random.choice(['kg', 'g', 'ml', 'liter']),
            'stock_quantity': round(random.uniform(1.0, 100.0), 2),
            'cost_per_unit': round(random.uniform(0.5, 5.0), 2)
        })
    return ingredients

# Generate Recipes
def generate_recipes(num_records):
    recipes = []
    for _ in range(num_records):
        recipes.append({
            'recipe_id': _ + 1,
            'item_id': random.randint(1, num_records),
            'ingredient_id': random.randint(1, num_records),
            'quantity': round(random.uniform(0.1, 1.0), 2)
        })
    return recipes

# Generate Inventory
def generate_inventory(num_records):
    inventory = []
    for _ in range(num_records):
        inventory.append({
            'inventory_id': _ + 1,
            'ingredient_id': random.randint(1, num_records),
            'quantity': round(random.uniform(1.0, 100.0), 2),
            'last_updated': fake.date_this_year()
        })
    return inventory

# Generate Staff
def generate_staff(num_records):
    staff = []
    for _ in range(num_records):
        staff.append({
            'staff_id': _ + 1,
            'name': fake.name(),
            'role': random.choice(['Barista', 'Manager', 'Chef']),
            'email': fake.email(),
            'phone': fake.phone_number()
        })
    return staff

# Generate Shifts
def generate_shifts(num_records):
    shifts = []
    for _ in range(num_records):
        shifts.append({
            'shift_id': _ + 1,
            'shift_start_time': fake.time(),
            'shift_end_time': fake.time()
        })
    return shifts

# Generate Rota
def generate_rota(num_records):
    rota = []
    for _ in range(num_records):
        rota.append({
            'rota_id': _ + 1,
            'staff_id': random.randint(1, num_records),
            'shift_id': random.randint(1, num_records),
            'start_date': fake.date_this_month(),
            'end_date': fake.date_this_month()
        })
    return rota

# Generate Roles
def generate_roles(num_records):
    roles = []
    for _ in range(num_records):
        roles.append({
            'role_id': _ + 1,
            'role_name': fake.word(),
            'description': fake.sentence()
        })
    return roles

# Generate User Role Assignments
def generate_user_role_assignments(num_records):
    assignments = []
    for _ in range(num_records):
        assignments.append({
            'assignment_id': _ + 1,
            'user_id': random.randint(1, num_records),
            'role_id': random.randint(1, num_records),
            'assignment_date': fake.date_this_year()
        })
    return assignments

# Create DataFrames
customers_df = pd.DataFrame(generate_customers(num_records))
addresses_df = pd.DataFrame(generate_addresses(num_records))
items_df = pd.DataFrame(generate_items(num_records))
ingredients_df = pd.DataFrame(generate_ingredients(num_records))
recipes_df = pd.DataFrame(generate_recipes(num_records))
inventory_df = pd.DataFrame(generate_inventory(num_records))
staff_df = pd.DataFrame(generate_staff(num_records))
shifts_df = pd.DataFrame(generate_shifts(num_records))
rota_df = pd.DataFrame(generate_rota(num_records))
roles_df = pd.DataFrame(generate_roles(num_records))
assignments_df = pd.DataFrame(generate_user_role_assignments(num_records))

# Save DataFrames to CSV
customers_df.to_csv('raw_data/customers.csv', index=False)
addresses_df.to_csv('raw_data/addresses.csv', index=False)
items_df.to_csv('raw_data/items.csv', index=False)
ingredients_df.to_csv('raw_data/ingredients.csv', index=False)
recipes_df.to_csv('raw_data/recipes.csv', index=False)
inventory_df.to_csv('raw_data/inventory.csv', index=False)
staff_df.to_csv('raw_data/staff.csv', index=False)
shifts_df.to_csv('raw_data/shifts.csv', index=False)
rota_df.to_csv('raw_data/rota.csv', index=False)
roles_df.to_csv('raw_data/roles.csv', index=False)
assignments_df.to_csv('raw_data/user_role_assignments.csv', index=False)

print("Fake data CSV files have been created successfully.")

