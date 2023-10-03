import time

# Function to start countdown timer
def start_countdown(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time Remaining: {remaining_time} seconds", end='\r')
        time.sleep(1)
    return start_time

# Function to check if player wins or loses
def check_win_or_lose(remaining_time):
    if remaining_time > 0:
        print(f"You broke the safe with {remaining_time} seconds remaining.")
    else:
        print("Sorry, you didnt break the safe in time. Better luck next time!")

# Main game function
def main_game():
    countdown_duration = 300  # 5 minutes in seconds
    print("Welcome to the Game!")

    # Start the countdown and get the start time
    start_time = start_countdown(countdown_duration)

    # Check if the player wins or loses based on the remaining time left
    check_win_or_lose(countdown_duration - int(time.time() - start_time))

if __name__ == "__main__":
    main_game()