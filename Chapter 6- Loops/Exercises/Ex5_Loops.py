sandwich_orders = ['Chicken', 'Tuna', 'Egg', 'Grilled Cheese',
                    'Pastrami', 'Pastrami', 'Pastrami']

finished_sandwiches = []

while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
        print("\nSorry, but we ran out of pastrami.")


for sandwich in sandwich_orders:
    print(f"\nI made your {sandwich} sandwich.")

finished_sandwiches = sandwich_orders

for finish in finished_sandwiches:
    print(f"\nHere is the finished {finish}")
