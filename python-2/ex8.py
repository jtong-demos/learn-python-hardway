formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three","four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "sentence 1",
    "sentence 2",
    "sentence 3",
    "sentence 4"
)

print "%s" %("one")