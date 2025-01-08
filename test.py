inv = {"Sword": 1}
itemAdd = {
            "Sword": 1,
            "dagger": 1,
            "Health potion": 2
            }

print(itemAdd)
for k in itemAdd:
    print(k)
    kCap = k.title()
    
    if kCap in inv:
        inv[kCap] += itemAdd[k]
    else:
        inv[kCap] = itemAdd[k]

print(inv)
