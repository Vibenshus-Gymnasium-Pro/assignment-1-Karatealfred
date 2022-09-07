current_users = ['Karatealfred', 'DONA', 'Bastian', 'Alfred', 'Josef']
new_users = ['Phillip', 'Karatealfred', 'dona', 'Anna', 'Fabian']

for i in range(len(current_users)):
    current_users[i] = current_users[i].casefold()

for new_user in new_users:
    if new_user.casefold() in current_users:
        print("You need to enter another username", new_user)
    else:
        print("Username was accepted", new_user)