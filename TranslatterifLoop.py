#While and If loop :Start
def TranslatorPhrase(phrase):
    translator=""
    print(phrase)
    for myletter in phrase:
        if  myletter.lower() in "aeiou":
            translator=translator+ "g"
        else:
            translator=translator+ myletter
    return translator


#while and If the loop:Ends
print(TranslatorPhrase(input("Enter the phrase:")))

