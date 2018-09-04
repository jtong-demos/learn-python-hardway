from sys import argv

script, filename = argv

print "we are going to erase %r" % filename
print "If you don't want that, press Ctrl-C"
print "Otherwise press ENTER to continue"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye"
target.truncate()

print "Please input 2 lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")

print "ok, I will write those to that file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

print "Finally, we will close it"
target.close()