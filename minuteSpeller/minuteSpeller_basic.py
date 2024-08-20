# Create a word game in Python, meant to test a users vocabulary to determine how many words they know. 
# Each round lasts sixty seconds, during which players submit as many words as possible, without repeating any, before the round is over. 
# The game is able to recognize any entry made as a valid or invalid Merriam Webster Dictionary entry.

# 1. User Input and Timing: The game must collect words from the user within a 60-second window.
# 2. Validation: The game needs to check each word against a valid dictionary to ensure it's a real word.
# 3. Scoring: Track the number of valid, unique words submitted by the player.
# 4. Dictionary API: We'll use an API like the Merriam-Webster API for word validation.

import time
import requests

API_KEY = "your_merriam_webster_api_key"
BASE_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json"

def validate_word(word):
    """
    Validate a word using the Merriam-Webster Dictionary API.
    """
    url = f"{BASE_URL}/{word}?key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0 and 'meta' in data[0]:
            return True
    return False

def vocabulary_game():
    print("Welcome to the Vocabulary Test Game!")
    print("You have 60 seconds to enter as many valid words as possible. No repeats allowed.")
    
    valid_words = set()
    start_time = time.time()
    end_time = start_time + 60  # Game lasts for 60 seconds
    
    while time.time() < end_time:
        word = input("Enter a word: ").strip().lower()
        
        if word in valid_words:
            print(f"You've already entered '{word}'. Try a different word.")
            continue
        
        if validate_word(word):
            valid_words.add(word)
            print(f"'{word}' is a valid word!")
        else:
            print(f"'{word}' is not a valid word.")
    
    print("\nTime's up!")
    print(f"You entered {len(valid_words)} valid words.")
    print("Words you entered:", ', '.join(valid_words))

# Start the game
vocabulary_game()
