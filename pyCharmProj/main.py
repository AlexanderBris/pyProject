
# ЗАДАНИЕ 1
a = "Python is the best programming language in the world"
b = len(a)
c = a[5: -7]
# результат
print(c)

# ЗАДАНИЕ 2
a = "Guido van Rossum is the benevolent dictator for life"
b = a[2::3]
# результат
print(b)

# ЗАДАНИЕ 4
a = "You have a problem with authority, Mr. Anderson."
symb = set(a) #разбиваем строку на отдельные символы без повторов
print(symb)
c = list(map(a.count, symb)) #ищем кол-во повторений для каждого элемента из "symb" в строке "a"
print(c)
d = list(zip(symb, c)) #создаем список из пар (символ, кол-во ссылок)
data = dict(d) #создаем словарь

# результат
print(data)