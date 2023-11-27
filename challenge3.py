# Challenge 3: Consonant value
def consonant_value(word):
    consonant_values = {letter: ord(letter) - ord('a') + 1 for letter in word if letter not in "aeiou"}
    
    # Group consecutive consonants
    groups = []
    current_group = []
    for letter in word:
        if letter not in "aeiou":
            current_group.append(letter)
        else:
            if current_group:
                groups.append(current_group)
                current_group = []
    if current_group:
        groups.append(current_group)
    
    # Calculate values for each group and return the maximum
    max_value = 0
    for group in groups:
        group_value = sum(consonant_values[letter] for letter in group)
        max_value = max(max_value, group_value)
    
    return max_value

# Test cases
print(consonant_value("chepkoech"))  # Output: 39
print(consonant_value("lazy_people_are_wise"))  # Output: 66