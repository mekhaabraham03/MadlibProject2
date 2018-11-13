Words_Needed = ["Adjective", "Adverb", "Body Part", "Color", "Event", "Food", "Fruit", "Liquid", "Material", "Name", "Noun", "Number", "Plural Noun", "Vegetable", "Verb"]
Dictonary = {}

for Word in Words_Needed:
    Temp_Word = input(f"Write a(n) {Word}:")
    Dictonary[Word] = Temp_Word

print(f"Please excuse {Dictonary['Name']} who is far too {Dictonary['Adjective']} to attend {Dictonary['Noun']} class.")

print(f"{Dictonary['Name']} is sick with {Dictonary['Body Part']} flu. Drink more {Dictonary['Liquid']} and take {Dictonary['Material']} as needed.")
