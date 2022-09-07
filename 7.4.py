prompt = 'Write a topping to add it to your order (write quit to order)'

topping = ''
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(topping.title() + ' was added to your order')
    else:
        print('Your pizza is now being made')