# Day 2 Project: Username Validator & Formatter
# This program cleans, validates, and formats usernames

print("="*50)
print("   USERNAME VALIDATOR & FORMATTER")
print("="*50)

# Get username from user
raw_username = input("\nEnter desired username: ")

print(f"\nRaw input: '{raw_username}'")

# Step 1: Clean the username (remove spaces from ends)
cleaned_username = raw_username.strip()
print(f"After cleaning: '{cleaned_username}'")

# Step 2: Convert to lowercase (usernames are usually case-insensitive)
formatted_username = cleaned_username.lower()
print(f"After lowercase: {formatted_username}")

# Step 3: Check length
min_length = 5
max_length = 15

username_length = len(formatted_username)

print(f"\nUsername length: {username_length} characters")

# Step 4: Validate and give feedback
print("\n" + "-"*50)
print("VALIDATION RESULTS:")
print("-"*50)

if username_length < min_length:
    print(f"❌ Too short! Need at least {min_length} characters.")
    print(f"   You need {min_length - username_length} more character(s).")
    
elif username_length > max_length:
    print(f"❌ Too long! Maximum {max_length} characters allowed.")
    print(f"   Please remove {username_length - max_length} character(s).")
    
else:
    print(f"✅ '{formatted_username}' is AVAILABLE!")
    print(f"   Perfect length: {username_length} characters")
    
    # Extra: Check if username contains only letters and numbers
    if formatted_username.isalnum():
        print("   ✅ Contains only letters and numbers (good!)")
    else:
        print("   ⚠️ Contains special characters (allowed but less common)")

print("\n" + "="*50)
print("✨ Username is ready for your account! ✨")
print("="*50)