

storage = []


def ask_username():
    username = ""
    while not username:
        temp = input("Enter your gmail address username "
                         "| <username>@gmail.com >> ")
        if "@" in temp:
            print("Do not use your complete email address, "
                  "only enter the username")
        else:
            username = temp
    return username


def shuffle(obj, init_pos):
    global storage
    temp = ""
    for i in range(init_pos, len(obj)):
        temp = obj[:i] + "." + obj[i:]
        if temp not in storage:
            if ".." not in temp:
                storage.append(temp)
                shuffle(temp, init_pos+2)
    return storage


# Ask for user input, then
# Make sure the base username doesn't contain a ".", then
# Start program
target = ask_username().replace(".", "")
shuffle(target, 1)


# Start writing to file
counter = 0
file = open('result.txt', 'w')
file.write("""
---------------------------------------------------
You can create accounts with this emails
---------------------------------------------------
""")
for i in storage:
    counter += 1
    temp = str(counter) + ". " +  str(i) + "@gmail.com"
    file.write(temp)
    file.write("\n")


# Say goodbye!
print("""
---------------------------------------------------
Check result.txt for the email combination list
---------------------------------------------------
""")
