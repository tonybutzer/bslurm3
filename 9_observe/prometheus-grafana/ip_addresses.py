import sys

print ("[", end="")
for i in range(1,4):
    print(f"{sys.argv[i]}:9100,", end="")
print ("]")
