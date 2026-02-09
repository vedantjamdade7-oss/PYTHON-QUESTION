f = open("poem.txt")
content = f.read()
if("little star" in content):
    print("The word little star is present in this content")

else:
    print("The word little star is not present in the content")


f.close()