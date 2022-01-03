# Create a function to count from
# 0 to 100 by counting by twos

# ---------------- Create a function - Jacob (Best) ----------------
def countingBy2Jacob():
    variable = 2
    while variable < 100:
        print(variable)
        variable += 2

countingBy2Jacob()


# ------------ Best Students ----------------
def count():
    for i in range(0, 100):
        if i%2 == 0:
            print(i)

count()
