
range = input("Enter your limit now. This is the number up till the skript will run \nAnswer here: ")
j = 0
for i in range(1, int(range)):
    if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % i == 0:
        print(i)
        j = j + 1
print("Amount of funi numbers: ", j)