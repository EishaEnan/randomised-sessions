import random

def calculate_time(card_value, min_duration, max_duration):
  """
  Calculates a duration based on a card value and a specified range,
  then rounds the result to the nearest multiple of 5.
  
  Args:
    card_value (int): The numerical value of the card (1-13).
    min_duration (int): The minimum possible duration in minutes.
    max_duration (int): The maximum possible duration in minutes.

  Returns:
    float: The calculated duration in minutes, rounded to the nearest multiple of 5.
  """
  # Ensure the card value is within the valid range (1-13)
  if not 1 <= card_value <= 13:
    raise ValueError("Card value must be between 1 and 13.")
  
  # Calculate the scaling factor
  scaling_factor = (max_duration - min_duration) / 12
  
  # Apply the linear scaling formula
  duration = min_duration + (card_value - 1) * scaling_factor
  
  # Round the duration to the nearest multiple of 5
  rounded_duration = round(duration / 5) * 5
  
  return float(rounded_duration)

def draw_card():
  """
  Simulates drawing a card from a deck.

  Returns:
    tuple: A tuple containing the card's numerical value (int), its name (str),
           and its suit (str).
  """
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  ranks = {
    1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 
    6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 
    11: 'Jack', 12: 'Queen', 13: 'King'
  }
  
  card_value = random.randint(1, 13)
  card_name = ranks[card_value]
  card_suit = random.choice(suits)
  
  return card_value, card_name, card_suit

# --- Main Program ---
def start_study_session():
    """
    Main function to run the card draw and calculate session/break times.
    """
    print("--- Let's get focused! ---")
    
    # 1. Draw a card for the study session
    study_card_value, study_card_name, study_card_suit = draw_card()
    study_duration = calculate_time(study_card_value, 45, 100)
    print(f"\nYour study card is: {study_card_name} of {study_card_suit}!")
    print(f"Your session will be: {study_duration} minutes.")
    
    # 2. Draw a card for the break
    break_card_value, break_card_name, break_card_suit = draw_card()
    break_duration = calculate_time(break_card_value, 10, 20)
    print(f"\nYour break card is: {break_card_name} of {break_card_suit}!")
    print(f"Your break will be: {break_duration} minutes.")

    print("\nGood luck! Enjoy your focused session and well-deserved break!")

# Run the program when the script is executed
if __name__ == "__main__":
    start_study_session()

