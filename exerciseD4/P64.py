# funkcja odwołująca się do obiektu globalnie zadeklarowanego w sktypcie
def returnColour():
    global value    # pobieram wartość globalną
    value = not value   # modyfikacja obiektu globalnego
    return "black" if value else "white";

value = True
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
