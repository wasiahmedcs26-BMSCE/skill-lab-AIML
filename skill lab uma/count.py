txt=input("Enter a word: ")
vcount=0
for ch in txt:
    if ch in "aeiouAEIOU":
        vcount+=1
print(f"Number of vowels in {txt} is {vcount}")