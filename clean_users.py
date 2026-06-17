import pandas as pd


users = [
    {"name": "Alice ", "age": "25", "salary": "50000"},
    {"name": "bob", "age": "thirty", "salary": "60000"},
    {"name": "  CHARLIE", "age": "35", "salary": None},
    {"name": None, "age": "40", "salary": "70000"},
]

# def clean_users(users:list[dict]) -> list[dict]:
df = pd.DataFrame(users)
for i in df:
    if df['name'] == 'nan':
        df[
for i in df['name']:
    print(type(i))
    # return name

# users = clean_users(users)
# print(users)