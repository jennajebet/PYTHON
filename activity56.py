class Kenya():
    def capital(self):
        print("Nairobi is the capital of Kenya")
    def language(self):
        print("The language spoke in Kenya is both Kiswahili and English")
    def type(self):
        print("Kenya is a developing country")

class Germany():
    def capital(self):
        print("Berilin is the capital of Germany")
    def language(self):
        print("The language spoken in Germany is the West Germanic language")
    def type(self):
        print("Germany is a developed country")

obj_kenya=Kenya()
obj_germany=Germany()

for country in(obj_germany,obj_kenya):
    country.capital()
    country.language()
    country.type()


# 1) Create a class `India` with three methods:
#    a) `capital()` to print the capital of India.
#    b) `language()` to print the main language spoken in India.
#    c) `type()` to print the type of country India is.

# 2) Create another class `USA` with the same method names:
#    a) `capital()` to print the capital of USA.
#    b) `language()` to print the primary language of USA.
#    c) `type()` to print the type of country USA is.

# 3) Create objects for both classes:
#    a) `obj_ind = India()`
#    b) `obj_usa = USA()`

# 4) Use a common interface (polymorphism) to call the same method names
#    on different objects:
#    a) Use a `for` loop to iterate through `(obj_ind, obj_usa)`.
#    b) For each object `country`, call:
#       - `country.capital()`
#       - `country.language()`
#       - `country.type()`
#    (Each object runs its own class implementation of these methods.)