import hellomoduł1 # import previous moduł to this moduł

hellomoduł1.say_hello()               # odwołaj się do funkcji z poprzedniego modułu poprzez  kropkę
name = input("Jak Ci na imię? : ")
hellomoduł1.say_hello_with_name(name)
