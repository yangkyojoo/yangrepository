# print("Hello World!")
# print("Good Bye.")

f = open('test.txt', 'r')
html = f.read(100)

f.close()

print(html)