def GramToOunce(gram):
    return gram * 28.3495231

ounce = GramToOunce(float(input("Enter the number of gramms: ")))

print(f"{ounce:.2f} ounces")
