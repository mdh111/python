telNumbers = {"person1":12345,"person2":4325}
print(telNumbers["person2"])
telNumbers["person3"] = 55555
print(telNumbers)

for name in telNumbers:
    print(name, telNumbers[name])