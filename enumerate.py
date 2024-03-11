# ex1. 使用 enumerate 迭代食物列表并打印
foods = ['春卷', '沙拉', '鸡肉串']
for index, food in enumerate(foods, start=1):
    print(f"{index}: {food}")

# ex2. 创建食物列表的索引列表
foods = ['寿司', '意面', '烤鸡']
indexed_foods = [(index, food) for index, food in enumerate(foods)]
# indexed_foods = list(enumerate(foods))
print(indexed_foods)

# ex3. 打印索引为偶数的食物
foods = ['春卷', '沙拉', '鸡肉串', '寿司', '意面', '烤鸡']
for index, food in enumerate(foods):
    if index % 2 == 0:
        print(f"序列号 {index}: 食物是 {food}")

# ex4. 结合两个列表打印出食物的价格
dishes = ['烤玉米', '炸鱼球', '土豆泥']
prices = [12, 15, 9]
for index, (dish, price) in enumerate(zip(dishes, prices)):
    print(f"{index}: {dish} 的价格是 {price} 元")

# ex5. 创建开胃菜和索引的字典
appetizers = ['蛋糕', '冰淇淋', '果汁']
appetizer_dict = {index: appetizer for index,
                  appetizer in enumerate(appetizers)}
print(appetizer_dict)
