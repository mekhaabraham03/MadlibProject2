from sys import argv

adjective, color, noun = argv
prompt = '>'

print(f"I know the teacher is very {adjective}. Sometimes he wears a {color} shirt with {noun} on it.")

print(f"Name an item")
iteam = input(prompt)

print(f"Name a place")
place = input(prompt)

print(f"Name a person")
person = input(prompt)

print(f"I canot find my {iteam} anywhere! It's not even at {place}. While I was at {place}, I saw {person}... maybe they have it.")

Words_Needed = ["Time", "Feeling", "Food", "Vehicle", "Grade level","Funny job", "Thing", "Adjective", "Hard task", "Name", "Verb", "School subject", "Body part", "Facial feature"]
Dictionary = {}

for Word in Words_Needed:
    Temp_Word = input(f"Write a(n) {Word}:")
    Dictionary[Word] = Temp_Word

print(f"It is the first day of school. NOOOO. I spent {Dictionary['Time']} hours moaning and groaning in bed. I was so {Dictionary['Feeling']} because I had to strat {Dictionary['Grade level']} grade. I ran downstairs to eat {Dictionary['Food']} for breakfast. When I walked outside, the {Dictionary['Vehicle']} had already left.")

print(f"I go to school so I can be a {Dictionary['Funny job']} when I grow up. They do {Dictionary['Hard task']}. Those professionals are very {Dictionary['Adjective']}. I hate other jobs because they use {Dictionary['Thing']}. I completely against that. ") 

print(f" Dear {Dictionary['Name']},")
print(f"I still remeber the first time I {Dictionary['Verb']} eyes on you.")
print(f"It was during {Dictionary['School subject']} class, and you canme in to give out teacher a {Dictionary['Thing']}.")
print(f"One day I want to hold your {Dictionary['Body part']} and kiss it")
print(f"Best Wishes <3, oh ans P.S. I LOVE your {Dictionary['Facial feature']}")

Words_Needed = ["Color", "Country", "Article of Clothing", "Verb", "Adjective", "Animal","Name","Food", "Store", "Candy", "Dance type", "Celebrity","Song", "Pronoun", "Verb2","Costume", "Number"]
Dictionary = {}
for Word in Words_Needed:
    Temp_Word = input(f"Write a(n) {Word}:")
    Dictionary[Word] = Temp_Word

print(f"I went to {Dictionary['Store']} to buy a {Dictionary['Animal']} last friday. I've been needing a friend. I found out that it only eats {Dictionary['Food']}, but I only had {Dictionary['Candy']} with me.I let it eat the {Dictionary['Candy']} and it ....ummmm..... died.")

print(f"I decided to take a {Dictionary['Dance type']} dance class. {Dictionary['Celebrity']} ended up teaching the class using the song {Dictionary['Song']}.") 

print(f" Dear  parents or guardians of {Dictionary['Name']}, {Dictionary['Name']} has been doing very {Dictionary['Adjective']} this semester. I thought it be very important that you were aware.")
print(f"{Dictionary['Pronoun']} is very rude to his classmates. He is also very intrested in {Dictionary['Verb']}ing. He needs to work on {Dictionary['Verb2']}ing however.")


print(f"My friend hired me to be a {Dictionary['Costume']} for {Dictionary['Number']} dollars. I was the best damn {Dictionary['Costume']} out there. The children were throwing {Dictionary['Candy']} at me. One apple was thrown at me too")

print(f"Today I get to marry {Dictionary['Name']}! It was the happiest day of my life. I wore a {Dictionary['Color']} {Dictionary['Article of Clothing']}. I had my whole family help me pick it out. We got married in {Dictionary['Country']}, also the best place for a honeymoon.")
