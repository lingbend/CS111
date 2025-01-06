from Grid import Grid

chicken = Grid(5,8)
chicken.set(2, 4, 'chicken')
print(chicken.grid)

print(chicken.get(2, 4))

duck = 'chicken'

print(duck == chicken)