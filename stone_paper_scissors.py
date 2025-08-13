import random
result = {"wins":0, 'loses':0, 'ties':0}
win_streak = 0
high_win_streak = 0
def play(): 
    global win_streak,high_win_streak
    
    
    actions = ['stone', 'paper', 'scissors']
    win_emojis = ["🏆", "🎯", "🥳", "🚀", "🔥"]
    loss_emojis = ["💔", "😥", "😓", "😢"]
    tie_emojis = ["🤝", "😐", "🙃"]

    user_in = input("Please select your action eg(stone/paper/scissors):")

    com_move = random.choice(actions)
    
    if user_in.lower() not in actions:
        print('🚫 Invalid move!! Valid moves ==>stone/paper/scissors')
        return 
    
    print(f"Computer Move: {com_move}\nYour Move: {user_in}")

    if user_in.lower() == com_move:
        print(random.choice(tie_emojis) + "Its a tie !!")
        result['ties'] += 1
        # win_streak = 0 if i want to reset streak on ties

    elif (user_in.lower() == 'stone' and com_move == actions[2]) or (user_in.lower() == 'paper' and com_move == actions[0]) or (user_in.lower() == 'scissors' and com_move == actions[1]):
        print(f"🎉Congratulations!!🎉\n{random.choice(win_emojis)} You Won!!")
        result['wins'] += 1
        win_streak += 1
        high_win_streak = max(high_win_streak,win_streak)

    else:
        print(f"\n😥Sorry😥\n{random.choice(loss_emojis)} You lost!!")
        result['loses'] += 1
        win_streak = 0

    print(f"🔥 Current Winning Streak: {win_streak} 🔥")



def start():
    print("Welcome to PyGames. Lets play Stone-Paper-Scissors")
    global win_streak, high_win_streak

    while True:
        print("1. Enter 1 to Start playing.")
        print("2. Enter 2 to Restart (reset stats & streak).")
        print("3. Enter 3 to see Result")
        print("4. Enter any other key to exit...")

        
        choice = input('Select your choice:')

        if choice == '1':
            while True:
                play()
                again = input('Play again? (y/n):').lower()
                if again != 'y':
                    break
        
        elif choice == '2':
            result['ties'] = 0
            result['loses'] = 0
            result['wins'] = 0
            win_streak = 0
            high_win_streak = 0
            print("🔄 Game stats & winning streak reset!Starting new game...\n")
            while True:
                play()
                again = input('Play again? (y/n): ').lower()
                if again != 'y':
                    break

        elif choice == '3':
            print('='*50)
            print("\n📊 Game Results:")
            print('\n🏆 Wins :',result['wins'])
            print('💔 Losses :', result['loses'])
            print('🤝 Ties :', result['ties'])
            print(f"🔥 Current Winning Streak: {win_streak} 🔥")
            print(f"🏅 Highest Winning Streak: {high_win_streak}")
            print('='*50)
        else :
            print("Exited..")
            break
start()



