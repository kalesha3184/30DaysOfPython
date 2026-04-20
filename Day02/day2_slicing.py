# String Slicing - Getting parts of text

message = "Python Programming is fun!"

# Syntax: [start:end] - end is EXCLUDED
#        [start:] - from start to end
#        [:end] - from beginning to end
#        [start:end:step] - skip characters

print(f"Full message: {message}")

# Get first 6 characters (indices 0 to 5)
first_word = message[0:6]
print(f"First 6 chars: {first_word}")

# Get characters 7 to 18 (Programming)
second_word = message[7:18]
print(f"Characters 7-18: {second_word}")

# Get from index 7 to end
from_7_to_end = message[7:]
print(f"From index 7: {from_7_to_end}")

# Get first 10 characters
first_10 = message[:10]
print(f"First 10 chars: {first_10}")

# Get every 2nd character
every_other = message[::2]
print(f"Every 2nd char: {every_other}")

# Get last 4 characters
last_4 = message[-4:]
print(f"Last 4 chars: {last_4}")

# Reverse the string
reversed_msg = message[::-1]
print(f"Reversed: {reversed_msg}")