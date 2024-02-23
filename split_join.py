# ex1
import re
salad = "生菜,番茄,黄瓜"
ingredients = salad.split(",")
print(ingredients)

# ex2
salad = "生菜:番茄:黄瓜:芝士"
ingredients = salad.split(":", 2)
print(ingredients)

# ex3
salad = "生菜#番茄;黄瓜|芝士"
ingredients = re.split(r'[;|#|\|]', salad)
print(ingredients)

# ex4
ingredients = ["生菜", "番茄", "黄瓜"]
salad = ",".join(ingredients)
print(salad)

# ex5
numbers = [1, 2, 3, 4, 5]
string = ",".join(map(str, numbers))
print(string)

# ex6
numbers = [1, 2, 3, 4, 5]
string = ','.join([f"{num}" for num in numbers])
print(string)
