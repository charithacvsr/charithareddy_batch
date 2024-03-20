### day9###

'''
# find the uncommon words from 2 strings
s1="hello how are you "
s2="hello how is"
s1=s1.split("")
s2=s2.split("")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
  '''      '''
# write a code print the 8th fibonachi number
# 0,1,1,2,3,5,8

num=8
n1=0
n2=1
for val in range(num):
    ans=n1+n2
    n1=n2
print(ans)
'''


#!   constructors
#! eg:2
#* unparamatarised constructor
class profile:
    def_init_(self):
        print("hello world")
obj = profile()
obj_init_()


#? parametarised constructor
class profile:
    def_init_(self,id,name,age):
        print(id,name,age)
obj=profile(1,"sid",29)

#? eg:4
class c1:
    name = "sid"
    place ="cbe"
    def m1(self):
        name = "sid"
        place = "cbe"
        print(name,place)
        print(self.email)
object = c1()
object.m1()
s1= "Hello how are you"
s2="Hello how is"

s1=s1.split(" ")
s2=s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)



#? to use the variable inside the consturctor in another methods

class class1:
    def_init_(self):
        self.name="sid"



# -----> inheritance
# the process of utilising the methods and attributes of parent class
# throught the object the child class it is called as inhertiance
****?5 types of inheritance
# single inhertaince
# multilevel inheritance
# multiple  inheritance
# hybird inheritance
# heriarichal inheritance


### single inheritance
# it has only one parent class and only one child class
# eg:1
class parent:
    def m1(self):
        print("iam parent class")
class child:
    def m2(self):
        print("iam child class")
p = parent()
p.m2()
obj = child()
obj.m1()

#! eg:2
class c1
   def_init_(self):
       print("iam constructor from parent clas")
class child1(C1)
  pass
obj = child1()


#!eg:3
class parent:
    name = "sidhu"
class child(parent):
    name ="name1"
    def child(parent):
        print(self.name)
d = child()
d.display()
 #! multilevel inheritance
        
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def dog_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
1:41 PM
class voice:
#     def sound(self):
#         print("All the animals have their own voices")
        
# class dog(voice):
#     def dog_voice(self):
#         print("bark")
        
# class cat(dog):
#     def cat_voice(self):
#         print("Meow")
        
# class parrot(cat):
#     def parrot_voice(self):
#         print("speak")
        
# all = parrot()
# all.dog_voice()
# all.cat_voice()
# all.sound()
# all.parrot_voice()



class honda_city:
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class amaze(honda_city):
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

    def amaze_body_specs(self, color, weight, height, length



class while_pertol:
       def function_w(self): print("used to Airplans")
class Organic_petrol:
   def function_o(self):
print("used for Bike, cars")
class premium_petrol:
    def function_p(self): print("spots cars, bikes")
class petrol (while_pertol, Organic_petrol, premium_petrol):
   def defanitination(self)
       print("petrols types")
p=petrol()
p.defination()
p.function

# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)




#! Heirarical inheritance.
#? The one parent classe will asct as parent for all the child classes
class catagory:
def weight(self, weight): print(weight)
I
def display(self, color, taste): print(color, taste)
 class Tomato(catagory):
def tomato_specs (self):
color="black"
taste "neutral taste"
self.display(color, taste)
class carrot (catagory):
def carrot_specs (self):
color="green"
c=carrot()
c.carrot_specs()
c.weight("30gms")

# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")




# ! -------> Polymorphism
# poly - many, morph--> form
# A function which has the ability t perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

# polymorphism in operations









































