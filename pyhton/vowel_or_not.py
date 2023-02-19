s="aeiou how are you"
vowel=set("aeiou")
for i in s:
    if i in vowel:
        vowel.remove(i)
if len(vowel)==0:
    print("All vowels present in the string")
else:
    print("All vowels are not present in the string")
