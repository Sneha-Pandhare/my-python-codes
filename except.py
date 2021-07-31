try:
    print(x)
except SyntaxError:
    print(" Variable x is not defined")
except:
    print("something else went wrong")