import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of a hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(player_score, dealer_score):
    """Compares the player's score with the dealer's score."""
    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 0:
        return "Blackjack! You win!"
    elif dealer_score == 0:
        return "Dealer has Blackjack. You lose!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_blackjack():
    """Main function to play a game of Blackjack."""
    print("🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮")
    print("Welcome to Blackjack!")
    player_cards = [deal_card(), deal_card()]   
    dealer_cards = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if should_continue == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))

if __name__ == "__main__":
    play_blackjack()