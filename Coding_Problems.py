# Loading libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

Main_dir = r"E:\Data Science\Data Science Projects\04_Python_Interview_Test/"
os.chdir(Main_dir)

auth = False
username = input("insert your name:\n")
password = input("insert your password:\n")
# print(username + " " + password)

if username == "Hermes" and password == "1234":
    auth = True
else:
    print("Usuario o contraseña incorrectos. Quedan 2 intentos.")
    username = input("insert your name:\n")
    password = input("insert your password:\n")
    if username == "Hermes" and password == "1234":
        auth = True
    else:
        print("Usuario o contraseña incorrectos. Queda 1 intento.")
        username = input("insert your name:\n")
        password = input("insert your password:\n")
        if username == "Hermes" and password == "1234":
            auth = True
        else:
            print("El acceso ha sido bloqueado.")

if auth == True:
    print("Bienvenido a su banco.")
    balance = 2000

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Transfer")
    print("5. Exit")

    option = int(input())
    if option == 1:
        print("How much do you want to deposit?")
        deposit = int(input())
        balance += deposit
        print(f"Your current balance is: {balance}")
    elif option == 2:
        print("How much do you want to withdraw?")
        withdraw = int(input())
        balance -= withdraw
        print(f"Your current balance is: {balance}")
    elif option == 3:
        print(f"Your current balance is: {balance}")
    elif option == 4:
        print("How much do you want to transfer?")
        transfer = int(input())
        balance -= transfer
        print(f"Your current balance is: {balance}")
    elif option == 5:
        print("Goodbye. See you soon!")
    else:
        raise Exception("Please, select an available option.")

my_list = ['cat', 'bat', 'rat', 'elephant']
for index, item in enumerate(my_list):
    print('The index: ' + str(index) + ' The item: ' + item)

