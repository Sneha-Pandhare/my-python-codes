try:
    f = open("demofile.txt")
    f.write("Sneha Pandhare")
except:
    print("Something went wrong")
finally:
    f.close()