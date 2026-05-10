letter = "hey my name is {1} and i am from {0}"
country="india"
name="harry"
# print(letter.format(country,name))

print(f"hey my name is {name} and i am from {country}")


price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))