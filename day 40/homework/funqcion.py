# პითონში მონაცემების გამოსატანად ან დამუშავებისთვის რამდენიმე  ჩაშენებული ფუნქცია და მეთოდი არსებობს. ქვემოთ მოცემულია რამდენიმე მათგანი:

# 1. input()

#გამოიყენება მომხმარებლისგან მონაცემების შესატანად.

# მიიღებული მნიშვნელობა ყოველთვის იქნება ტექსტის ტიპის (str).


name = input("რა არის თქვენი სახელი? ")
print("გამარჯობა,", name)


# ---

# 2. len()

# აბრუნებს ელემენტების რაოდენობას სტრიქონში, სიაში ან სხვა იტერირებად ობიექტში.


message = "გამარჯობა"
print(len(message))  # 9


# ---

# 3. type()

#აბრუნებს ობიექტის ტიპს.


num = 42
print(type(num))  # <class 'int'>


# ---

# 4. str(), int(), float()

str(): # მონაცემების ტექსტად გადაქცევა.

int(): # მონაცემების მთელ რიცხვად გადაქცევა.

float(): # მონაცემების მცურავ წერტილად გადაქცევა.


num = 42
print(str(num))  # "42"
print(float(num))  # 42.0


# ---
