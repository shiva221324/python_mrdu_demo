file=open("marks.txt","w")
file.write("95")
file.write("12")
file.write("76")
file.close()

file2=open("marks.txt","r") 
data=file2.read()
print(data)
