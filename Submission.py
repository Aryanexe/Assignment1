#list example
list1=["hello", "this is","a list"]
list2=[362.7,43,"World",True]
print(list1)
print(list2)
print(list1+list2)

#indexing
print(list2[1])
list2[1]=34
list2[-2]="trampoline"
print(list2[-2])

#appending data
list2.append(69)
print(list2)

#inserting data
list2.insert(1,"inserted")
print(list2)

#deleting data
del list2[-1]
print(list2)

list2.remove(34)
print(list2)


#tuple example
tuple1=(["data", 23, True, 42.46])
print(tuple1)
tuple2=(["second", 54])
print(tuple1,tuple2)


#Dictionary example
dict={
       "Name":["Aryan","Sihag"],
       "University":"BITS Pilani",
       "OS":"Windows",
       "RAM":"8GB"
}
print(dict["Name"],dict["OS"])

#update
dict["version"]=7
print(dict)
dict["Name"]="Jojo"
print(dict)

#deleting
del dict["OS"]
print(dict)


#slicing
var="Engineering"
print(var[0:6]) # 0 to 6 index value with 6th index value excluded.
print(var[3:])
print(var[:4])
print(var[-6:-1])
print(var[0:100])


#step index (negative and positive both)
print(var[1:8:2])
print(var[::-2])
print(var[8:1:-2])
print(var[10::-3])

