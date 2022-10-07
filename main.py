#tuples
print("what are your 3 favorite bands?")
band1 = input()
band2 = input()
band3 = input()
Bands = (band1,band2,band3)

for i in range(len(Bands)):
    print(Bands[i], end = " ")
print()
print(Bands[1])
print()
#list
foodList = []
print("What are your 5 favorite foods?")
for i in range(5):
    food = input()
    foodList.append(food)

for i in range(len(foodList)):
    print(foodList[i], end = " ")
print()
print(foodList[-1])
print()
#dictionary
HeroVillian = {}
print("what are your 6 favorite video game Hero/Villian pairs?")
for i in range(6):
    Hero = input()
    Villian = input()
    HeroVillian[Hero] = Villian

print(HeroVillian)
print()
print("which heroes villian would you like to see?")
choice = input()

print("You wanted to see,", choice,"'s Villains, who is,", HeroVillian[choice])
