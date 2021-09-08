
def info(obj):
    print("Type: " + str(type(obj)))
    print([s for s in dir(obj) if not s.startswith("_")])