def solve(numheads, numlegs):
    for i in range(numheads+1):
        j = numheads - i
        if 2*i + 4*j == numlegs:
            return f"Number of chickens is {i} and rabbits is {j}"
    return "No solutions"

numheads = 35 
numlegs = 94 
solutions = solve(numheads, numlegs)
print(solutions)
