students={ 
    "alice": 90,
      "Bob": 75 ,
        "Jane": 85}

for name, score in
students.items():
    print(name, score)

average = sum(students.values()) / len(students)
print("average:", average)

print("highest:", max(students, key= students.get))
print("lowest:", min(students,key=students.get))

name = input("enter students name:")
print(students.get(name, "Not found"))
