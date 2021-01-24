word = input()

print("Won" if len(list(set(word))) == 1 else "Lost")
