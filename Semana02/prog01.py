
print("Hello World")

message = "Hello World"
print(message)

message = "Yuri\'s World"
print(message)

message = "Hello World"
print(len(message))

print(message[0])

print(message[0:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count("l"))

print(message.find("World"))

print(message.find("other word"))

message.replace("World","other word")

print(message)

greeting = "Hello"
name = "Yuri"
message = greeting + ", "+ name + ". Welcome!"
print(message)
message = "{}, {}. Welcome!".format(greeting,name)
print(message)
message = f"{greeting}, {name}. Welcome!"
print(message)
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)
print(dir(name))

# print(help(str))
# print(help(str.lower))