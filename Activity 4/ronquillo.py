sampleText1 = "My name is {}. Age {}. I love Doodling."
sampleText1a = sampleText1.format("Lovely", "18")
print(sampleText1a)

sampleText2 = "My name is {1}. Age {2}. I love {0}."
sampleText2a = sampleText2.format("Doodling", "Lovely", "18")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {doodling}. And I love playing {play}."
sampleText3a = sampleText3.format(doodling="sunset", play="games", name="Lovely")
print(sampleText3a)

item = "Sisig"
cost = 500
SampleText4 = "The product is %s and the cost is %.2f." % (item, cost)
print(SampleText4)

item = "IPod"
cost = 25,000
Sample5 = f"The item is {item}  that cost is {cost} pesos"
print(Sample5)
