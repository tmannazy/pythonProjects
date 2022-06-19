# customers = [
#     {
#         'name': 'Omotola Fashola',
#         'acct_num': '001',
#         'age': 21,
#         'balance': 10_000,
#         'type': 'savings',
#         'gender': 'female',
#         'is_married': False,
#     },
#
#     {
#         'name': 'Idiot Olamide',
#         'acct_num': '010',
#         'age': 32,
#         'balance': 10_000,
#         'type': 'savings',
#         'gender': 'male',
#         'is_married': False,
#     },
#
#     {
#         'name': 'Ololade Asake',
#         'acct_num': '075',
#         'age': 24,
#         'balance': 70_000,
#         'type': 'savings',
#         'gender': 'female',
#         'is_married': True,
#     },
#
#     {
#         'name': 'Dorcas Charles',
#         'acct_num': '015',
#         'age': 19,
#         'balance': 30_000,
#         'type': 'savings',
#         'gender': 'female',
#         'is_married': False,
#     },
#
#     {
#         'name': 'Emmanuel Obsession',
#         'acct_num': '092',
#         'age': 76,
#         'balance': 1_000_000,
#         'type': 'current',
#         'gender': 'male',
#         'is_married': True,
#     },
#
#     {
#         'name': 'Eden Ace',
#         'acct_num': '083',
#         'age': 26,
#         'balance': 500_000,
#         'type': 'current',
#         'gender': 'female',
#         'is_married': True,
#     },
#
#     {
#         'name': 'Abigail UCJ',
#         'acct_num': '021',
#         'age': 22,
#         'balance': 50_000,
#         'type': 'current',
#         'gender': 'male',
#         'is_married': True,
#     },
#
#     {
#         'name': 'Shaf Specimen',
#         'acct_num': '019',
#         'age': 16,
#         'balance': 6_000_000,
#         'type': 'current',
#         'gender': 'male',
#         'is_married': False,
#     },
#
#     {
#         'name': 'Boyo Power',
#         'acct_num': '005',
#         'age': 29,
#         'balance': 2_000_000,
#         'type': 'current',
#         'gender': 'male',
#         'is_married': False,
#     },
# ]


customers = [
    {
        "name": "Omotola Fashola",
        "acct_num": "001",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": True
    },
    {
        "name": "Idiot Olamide",
        "acct_num": "010",
        "age": 32,
        "balance": 1_005,
        "type": "savings",
        "gender": "male",
        "is_married": False
    },
    {
        "name": "Abdur-Rahman Fashola",
        "acct_num": "020",
        "age": 26,
        "balance": 100_000,
        "type": "current",
        "gender": "male",
        "is_married": True
    },
    {
        "name": "Ololade Boyo",
        "acct_num": "031",
        "age": 18,
        "balance": 34_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Dorcas Charles",
        "acct_num": "011",
        "age": 19,
        "balance": 30_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Emmanuel Obsession",
        "acct_num": "092",
        "age": 76,
        "balance": 1_000_000,
        "type": "current",
        "gender": "male",
        "is_married": True
    },
    {
        "name": "Eden Ace",
        "acct_num": "041",
        "age": 16,
        "balance": 150_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Blessing Elon",
        "acct_num": "063",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Odogwu Buga",
        "acct_num": "081",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "male",
        "is_married": False
    },
    {
        "name": "Abigail UCJ",
        "acct_num": "044",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
]


# names = [customer['name'] for customer in customers]
# names_in_set = {key: value for key, value in enumerate(customers)}
# avg_of_customers_age = sum(customer['age'] for customer in customers) / len(customers)
# print(names)
# savings_acct_holders = [customer for customer in customers if customer['type'] == 'savings']
# savings_acct_holders = [dict(name=c['name'], balance=c['balance']) for c in customers if
#                         c['type'] == 'savings']
# print(names_in_set)
# print(savings_acct_holders)
# print({'balance': sum(c['balance'] for c in customers if c['type'] == 'current')})

def get_balance(dict_: dict) -> int:
    return dict_['age']


# print(sorted(customers, key=get_balance, reverse=True))
print(min(customers, key=get_balance))
# c = [customer for customers in sorted(customers.sort(key=get_balance, reverse=True))]
# print(customers)
