import random

board = {
    1: " 1", 2: "2", 3: "3",
    4: " 4", 5: "5", 6: "6",
    7: " 7", 8: "8", 9: "9"
}
stat = {}

def init_stat(players):
    global stat
    for player in players:
        if player not in stat:
            stat[player] = {"wins":0, "losses":0,"ties":0, "win_streak" :0, "high_win_streak":0}

def update_stats(winner, player1, player2, tie=False):
    if tie:
        stat[player1]["ties"] += 1
        stat[player2]["ties"] += 1
    else:
        loser = player2 if winner == player1 else player1
        stat[winner]["wins"] += 1
        stat[winner]["win_streak"] += 1
        stat[winner]["high_win_streak"] = max(stat[winner]["high_win_streak"], stat[winner]["win_streak"])
        stat[loser]["losses"] += 1
        stat[loser]["win_streak"] = 0


def display_board():
    print("\n")
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("---+---+---")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---+---+---")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("\n")


def player_move(player_name,symbol):
    while True:
        try:
            pos = int(input(f"{player_name} ({symbol}), enter your move (1-9): "))
            if pos < 1 or pos > 9:
                    print("❌ Invalid position! Enter a number between 1 and 9.")
                    continue
        
            if board[pos] not in ("❌", "⭕", "😎", "🐱", "🐶", "⭐", "🔥", "💧"):
                board[pos] = symbol 
                break
            else:
                print("🚫 Cell already occupied! Try again.")
        
        except ValueError:
             print("❌ Please enter a valid number.")

def check_winner(symbol):
    winnig_comb = [
    [1,2,3], [4,5,6], [7,8,9], # row wise
    [1,4,7], [2,5,8], [3,6,9], # column wise
    [1,5,9], [3,5,7]           # diagonally
    ]

    for combo in winnig_comb:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False

def choose_symbol(available_symbols,player_name):
    """Prompt a player to choose a symbol from available options."""

    print('\nAvailable symbols:')
    for key,value in available_symbols.items():
        print(f'{key} => {value}')
    
    while True:
        try:
            choice = int(input(f"{player_name}, select your symbol number: "))
            if choice in available_symbols:
                return available_symbols.pop(choice)
            else:
                print("❌ Invalid choice! Please choose a valid number.")
        except:
            print("❌ Please enter a valid number.")

def choose_game_mode():
    print("\nChoose Game mode:")
    print("1. 1 Player (VS AI) mode")
    print("2. 2 Player mode")
    
    while True:
        mode = int(input("Enter 1 or 2 to select mode:"))
        if mode in [1,2]:
            return mode
        print("❌ Invalid choice. Only 2 modes available.")

def ai_difficulty():
    print("\nChoose AI Difficulty Level:")
    print("1. Easy ")
    print("2. Hard ")

    while True:
        level = int(input("Enter 1 or 2 to select level:"))
        if level in [1,2]:
            return level
        print("❌ Invalid choice. Only 2 levels available.")

def ai_move(symbol,difficulty,player_symbol):
    """Return AI move position."""
    available_pos = [pos for pos, val in board.items() if val not in ("❌", "⭕", "😎", "🐱", "🐶", "⭐", "🔥", "💧")]
    if difficulty == 1: # Easy
        return random.choice(available_pos)
    
    else: # Hard
        
        # Check for winning moves:
        for pos in available_pos:
            board[pos] = symbol
            if check_winner(symbol):
                board[pos] = str(pos) #Reset
                return pos
            board[pos] = str(pos) #Reset
        
        # Block Opponents moves:

        for pos in available_pos:
            board[pos] = player_symbol
            if check_winner(player_symbol):
                board[pos] = str(pos) #Reset
                return pos
            board[pos] = str(pos) #Reset
        
        # Otherwise Random
        return random.choice(available_pos)

def player_symbol_assign(mode):
    available_symbols = {
        1: "❌",
        2: "⭕",
        3: "😎",
        4: "🐱",
        5: "🐶",
        6: "⭐",
        7: "🔥",
        8: "💧"
    }
   
    if mode == 2: # 2 players mode
    # ---- player 1 ----
        p1_name = input("Enter Player 1 name: ")
        p1_symbol = choose_symbol(available_symbols,p1_name)
    
    # ---- Player 2 ----
        p2_name = input("Enter Player 2 name: ")
        p2_symbol = choose_symbol(available_symbols,p2_name)
   
    else: # 1-player mode vs AI
        ai_first = random.choice([True,False]) # who goes first
        if ai_first:
            p1_name = "🤖 AI"
            p1_symbol = random.choice(list(available_symbols.values()))
            available_symbols = {k:v for k,v in available_symbols.items() if v != p1_symbol}

            p2_name = input("Enter your name: ")
            p2_symbol = choose_symbol(available_symbols, p2_name)
        
        else:
            p1_name = input("Enter your name: ")
            p1_symbol = choose_symbol(available_symbols, p1_name)

            p2_name = "🤖 AI"
            p2_symbol = random.choice(list(available_symbols.values()))
            available_symbols = {k:v for k,v in available_symbols.items() if v != p2_symbol}

        
    return (p1_name,p1_symbol), (p2_name, p2_symbol)

def run_game():
    while True:
        board.update({i: f" {i}" for i in range(1, 10)})
       
        mode = choose_game_mode()
        difficulty = ai_difficulty() if mode == 1 else None
        
        # Assign names & symbols
        (p1_name,p1_symbol), (p2_name, p2_symbol) = player_symbol_assign(mode)
        current_player = (p1_name,p1_symbol)
        moves = 0

        if "AI" in p1_name:
            ai_opponent_symbol = p2_symbol
        elif "AI" in p2_name:
            ai_opponent_symbol = p1_symbol
        else:
            ai_opponent_symbol = None


        # Initialize stats
        init_stat([p1_name, p2_name])

        while True:
            display_board()
            # AI moves 
            if "AI" in current_player[0]:
                pos = ai_move(current_player[1], difficulty, ai_opponent_symbol)
                board[pos] = current_player[1]
                print(f"{current_player[0]} ({current_player[1]}) chooses position {pos}")

            else:
                player_move(current_player[0],current_player[1])
            moves += 1

            if check_winner(current_player[1]):
                display_board()
                print(f"🎉 {current_player[0]} ({current_player[1]}) wins!")
                
                other_player = p2_name if current_player[0] == p1_name else p1_name
                update_stats(current_player[0], current_player[0], other_player)
                break


            if moves == 9:
                display_board()
                print("🤝 It's a Tie!")
                update_stats(None, p1_name, p2_name, tie=True)
                break

            current_player = (p2_name,p2_symbol) if current_player[0] == p1_name else (p1_name, p1_symbol)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

def Show_stats():
    if not stat:
        print("📊 No stats available yet. Play some games first!")
        return
    for player, stats in stat.items():
        print(f"==== {player} ====")
        print("\n📊 Game Results:")
        print('\n🏆 Wins :',stats['wins'])
        print('💔 Losses :', stats['losses'])
        print('🤝 Ties :',  stats.get('ties', 0))
        print(f"🔥 Current Winning Streak: {stats['win_streak']} 🔥")
        print(f"🏅 Highest Winning Streak: {stats['high_win_streak']}")
        print('='*50)

def reset_stats():
    global stat
    for player in stat:
        stat[player] = {"wins":0, "losses":0, "ties":0, "win_streak":0, "high_win_streak":0}
    

def main_menu():
    print("🎯 Welcome to Python Tic-Tac-Toe!")

    while True:
        print("\n🎮 Tic-Tac-Toe Main Menu 🎮")
        print("1. Play")
        print("2. Restart")
        print("3. Show Results / Stats")
        print("4. Enter any key to exit...")
        choice = input("Enter your choice (1-4): ")
       
        if choice == "1":
            run_game()
        elif choice == "2":
            reset_stats()
            run_game()
        elif choice == "3":
            Show_stats()
        else:
            print("👋 Goodbye!")
            break

main_menu()