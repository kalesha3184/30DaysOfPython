# Mad Libs Generator - Day 1 Project

# Get user inputs
adjective = input("Enter an adjective: ")
noun=input("Enter a noun: ")
verb=input("Enter a verb: ")
place=input("Enter a place: ")
adjective1=input("Enter an adjective: ")


# Creating the story using f-strings

story=f"""Once upon a time, a {adjective} {noun} decided to {verb}. Everyone in {place} was amazed and clapped. It was the most {adjective1} day ever! To the audineces"""

# Print the result
print("\n" + "="*40)
print(story)
print("\n" + "="*40)