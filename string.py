# string function
line=input("Enter line : ")
print(len(line))
print(line[0])
print(line[5:])

print(line.endswith("ssss."))
new=line.capitalize()
line=new
print(line)
new1=line.replace("o","a")
print(new1)
print(line.find("s"))
print(line.count("s"))