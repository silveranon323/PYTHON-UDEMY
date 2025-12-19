student={
    "name":"Hem",
    "A\d":"qsadwfd"
}
print(student.items())

sr=sorted(student,key=Lambda s:s["name"])
print(sr)
nums=[1,2,3,4,5]
squareresult=[lambda x : x*2 ]