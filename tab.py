import os
os.chdir('e:/workspace/HeadFirstPython/chapter3')


data = open('sketch.txt')
# Do something with the data
# in "the_file"
print(data.readline().strip())
print(data.readline())
data.seek(0)
for each_line in data:
	print(each_line.strip())
data.close()