val = "{} {} {}"
val = val.format("coding", "is", "great")
print(val)

# indexed
val = "{1} {0} {2}"
val = val.format("is", "coding", "great")
print(val)

# initiated
val = "{first} {second} {last}"
val = val.format(second="is", first="coding", last="great")
print(val)

# float format, value:width.decimalPrecision
# width adds whitespace
val = 889 / 45
val = "{r:0.2f}".format(r=val)
print(val)
