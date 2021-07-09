from CorePython.pythonClass import pythonClass

python_class_obj = pythonClass(user="rgr1", pwd="****", host="ibm01", db="vtest191")
print(python_class_obj.hostname)

python_class_obj = pythonClass("rgr10", "*****", "ibm02", "vtest181")
print(python_class_obj.hostname)
