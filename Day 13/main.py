#strings are immutable
a = "!!!Harry !!!!!!!!! Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","Johnny"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())
print(len(blogHeading))
print(len(blogHeading.center(50)))
print(a.count("Harry"))

str1 = "welcome to the console !!!"
print(str1.endswith("!!!"))

print(str1.endswith("to",4,10))

str2 = "He's name is Dan. He is an honest man"
print(str2.find("issh"))
print(str2.index("is"))

str3 = "welcometotheconsole"
print(str3.isalnum())

str4 = "Welcome"
print(str4.isalpha())
print(str4.islower())

str5 = "we wish you a merry christmas\n"
print(str5.isprintable())

str6 = " "
print(str6.isspace())

str7 = "World Health organization"
print(str7.istitle())

str8 = "Python is a Interpreted Language"
print(str8.startswith("Python"))
print(str8.swapcase())
print(str8.title())

