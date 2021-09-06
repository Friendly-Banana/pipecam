
def info(o):
    print("Type: " + str(type(o)))
    print([s for s in dir(o) if not s.startswith("_")])