# ex1.
meat = ["牛肉", "鸡肉", "鱼肉"]
vegetable = ["生菜", "番茄", "黄瓜"]

burger = list(zip(meat, vegetable))
print(burger)

# ex2.
bread = ["牛肉汉堡", "鸡肉汉堡", "鱼肉汉堡"]
meat = ["牛肉", "鸡肉", "鱼肉"]
vegetable = ["生菜", "番茄", "黄瓜"]

for b, m, v in zip(bread, meat, vegetable):
    print(f'{b} 包含 {m} 和 {v}')

# ex3.
bread = ["牛肉汉堡", "鸡肉汉堡", "鱼肉汉堡"]
meat = ["牛肉", "鸡肉", "鱼肉"]
vegetable = ["生菜", "番茄", "黄瓜"]

burger = {b: [m, v] for b, m, v in zip(bread, meat, vegetable)}
print(burger)
