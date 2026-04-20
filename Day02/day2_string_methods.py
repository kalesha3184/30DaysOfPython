# Day 2: String Methods - Type every line!

# Original text

text="  hello WORLD  "
print(f"Original: '{text}'")


# .strip() - removes spaces from beginning and end

cleaned=text.strip()
print(f"After strip: '{cleaned}'")



# .upper() - makes everything UPPERCASE

upper_text=cleaned.upper()
upper_text1=text.upper()
print(f"Upperscase: {upper_text}")
print(f"Uppercase1: {upper_text1}")



# .lower() - makes everything LOWERCASE

lower_text=cleaned.lower()
print(f"Lowercase: {cleaned}")


# .capitalize() - makes First Letter capital, rest Lowercase

capitalized=cleaned.capitalize()
print(f"Capitalized: {capitalized}")


# .title() - makes  First Letter of EVERY word capital

title_text="welcome to the party american club".title()
print(f"Title case: {title_text}")

# .replace() - replace one one word with another word in the strings 

repalced="I like Dogs ".replace("Dogs", "Cats")
print(f"Replaced: {repalced}")

# .len() - gets Length of string (counts charcters)

name="kalesha"
print(f"Length of '{name}': {len(name)} characters")
