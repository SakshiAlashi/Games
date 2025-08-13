result = {"wins":0, 'loses':0, 'ties':0}
win_streak = 0

def play(): 
    global win_streak
    
    import random
    actions = ['stone', 'paper', 'scissors']
    user_in = input("Please select your action eg(stone/paper/scissors):")

    com_move = random.choice(actions)
    
    if user_in.lower() not in actions:
        print('🚫 Invalid move!! Valid moves ==>stone/paper/scissors')
        return 
    
    print(f"Computer Move: {com_move}\nYour Move: {user_in}")

    if user_in.lower() == com_move:
        print(f"Its a tie !!")
        result['ties'] += 1
        win_streak = 0

    elif (user_in.lower() == 'stone' and com_move == actions[2]) or (user_in.lower() == 'paper' and com_move == actions[0]) or (user_in.lower() == 'scissors' and com_move == actions[1]):
        print(f"🎉Congratulations!!🎉\n You Won!!")
        result['wins'] += 1
        win_streak += 1

    else:
        print(f"Computer Move: {com_move}\nYour move: {user_in}\n😥Sorry😥\n You lost!!")
        result['loses'] += 1
        win_streak = 0

    print(f"🔥 Current Winning Streak: {win_streak} 🔥")



def start():
    print("Welcome to PyGames. Lets play Stone-Paper-Scissors")
    while True:
        print("1. Enter 1 to Start playing.")
        print("2. Enter 2 to Restart (reset stats & streak).")
        print("3. Enter 3 to see Result")
        print("4. Enter any other key to exit...")

        
        choice = input('Select your choice:')

        if choice == '1':
            play()
        elif choice == '2':
            global win_streak
            result['ties'] = 0
            result['loses'] = 0
            result['wins'] = 0
            win_streak = 0
            print("🔄 Game stats & winning streak reset!Starting new game...\n")
            play()
        elif choice == '3':
            print('='*50)
            print("\n📊 Game Results:")
            print('\n🏆 Wins :',result['wins'])
            print('💔 Losses :', result['loses'])
            print('🤝 Ties :', result['ties'])
            print(f"🔥 Current Winning Streak: {win_streak} 🔥")
            print('='*50)
        else :
            print("Exited..")
            break
start()



