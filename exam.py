#Questions
print("Quistion = 5 + 6 ?\na.12\nb.11\nc.14\nd.9")
answer1 = input('which one ? ')
print("Quistion = 18 - 5 ?\na.12\nb.11\nc.13\nd.9")
answer2 = input('which one ? ')
print("Quistion = 22 / 2\na.11\nb.44\nc.19\nd.10")
answer3 = input('which one ? ')
# function to calculate score with answer variables
def score():
    if answer1 == 'b' and answer2 == 'c' and answer3 == 'a':
        return "Your score is 100 %"
    elif answer1 == 'b' and answer2 == 'c' or answer1 == 'b' and answer3 == 'a' or answer2 == 'c' and answer3 == 'a':
        return "Your score is 66 %"
    elif answer1 == 'b' or answer2 == 'c' or answer3 == 'a':
        return "Your score is 33 %"
    else:
        return "Your score is 0 %"
print(score())


