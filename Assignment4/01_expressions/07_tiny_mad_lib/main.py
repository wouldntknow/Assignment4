sentenceStart : str = "Welcome to Mad Libs game where each player willl enter an adjective"
"noun and verb to create an interesting fun story!"
adjective : str = input("Please type an adjective and press enter: ")
noun :  str = input("Please type a noun and press enter: ")
verb: str = input("Please type a verb and press enter: ")

print(sentenceStart  + " " + adjective +" " + noun + " " + verb)