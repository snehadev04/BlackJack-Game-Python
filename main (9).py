  import random  # Importing the random module to generate random numbers
  from art import logo  # Importing the game logo from the art module
  from replit import clear  # Importing the clear function from the replit module for clearing the console

  def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # List of cards in the deck
    card = random.choice(cards)  # Randomly selects a card from the deck
    return card


  def calculate_score(cards):
    """Takes a list of cards and returns the calculated score."""

    if sum(cards) == 21 and len(cards) == 2:  # Checks if the player has a blackjack
      return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:  # Checks if there is an ace in the hand and the total score is over 21
      cards.remove(11)  # Replaces the value of ace from 11 to 1
      cards.append(1)
    return sum(cards)  # Returns the total score of the hand


  def compare(user_score, computer_score):
    """Compares the scores of the player and computer and determines the winner."""
    if user_score > 21 and computer_score > 21:  # Checks if both player and computer are over 21
      return "You went over. You lose 😤"
    if computer_score == user_score:  # Checks for a draw
      return "draw"
    elif computer_score == 0:  # Checks if computer has a blackjack
      return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:  # Checks if player has a blackjack
      return "you win with a  Blackjack 😱"
    elif user_score > 21:  # Checks if player is over 21
      return "you went over. you loose!!"
    elif computer_score > 21:  # Checks if computer is over 21
      return "opponent went over. you win!!"
    elif user_score > computer_score:  # Checks if player has higher score than computer
      return "you win!!"
    else :
      return "you loose"

  def play_game():
    """Runs the Blackjack game."""
    print(logo)  # Displays the game logo

    user_cards = []  # Initializes an empty list to store user's cards
    computer_cards = []  # Initializes an empty list to store computer's cards

    is_game_over = False  # Flag to track if the game is over
    for i in range(2):  # Deals two cards to the player and computer
      user_cards.append(deal_card())  # Adds a card to the player's hand
      computer_cards.append(deal_card())  # Adds a card to the computer's hand

    while not is_game_over:
      user_score = calculate_score(user_cards)  # Calculates the player's score
      computer_score = calculate_score(computer_cards)  # Calculates the computer's score
      print(f"  Your cards: {user_cards}, current score: {user_score}")  # Displays player's current hand and score
      print(f"  Computer's first card: {computer_cards[0]}")  # Displays computer's first card

      if user_score == 0 or computer_score == 0 or user_score > 21:  # Checks if the game is over
        is_game_over = True  # Ends the game if the conditions are met

      else:
        user_deal = input("type 'yes' to draw a card or type 'no' to pass ")  # Prompts user to draw or pass
        if user_deal == "yes":  # If user chooses to draw a card
          user_cards.append(deal_card())  # Adds a card to the player's hand
        else:
          is_game_over = True  # Ends the game if user chooses to pass

    while computer_score != 0 and computer_score < 17:  # Computer continues to draw cards if score is less than 17
      computer_cards.append(deal_card())  # Adds a card to the computer's hand
      computer_score = calculate_score(computer_cards)  # Calculates the computer's score

    print(f"  Your final hand: {user_cards}, final score: {user_score}")  # Displays player's final hand and score
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")  # Displays computer's final hand and score
    print(compare(user_score, computer_score))  # Compares scores and determines the winner

  while input("Want to play a game of Blackjack? type 'yes' for a game and 'no' to pass"):  # Prompts user to start a new game
    clear()  # Clears the console
    play_game()  # Starts a new game
