#Ikke-muterbar type (int)
a = 1337
b = a

print(f"a: {a} ({id(a)})")
print(f"b: {b} ({id(b)})")

a += 6440

print(f"a: {a} ({id(a)})")
print(f"b: {b} ({id(b)})")