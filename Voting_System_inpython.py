import os
import time

# ================= CONSTANTS =================
MAX_CANDIDATES = 10
MAX_VOTERS = 100

# ANSI Colors
RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
BOLD    = "\033[1m"

# ================= DATA STRUCTURES =================
class Candidate:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.votes = 0

candidates = []
voted_ids = []

# ================= UTILITY FUNCTIONS =================
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def print_border():
    print("+----------------------------------+")

def loading_effect():
    print("Processing", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print()

# ================= MAIN MENU =================
def main_menu():
    clear_screen()
    print_border()
    print(f"| {BOLD}{CYAN}  Voting Management System  {RESET} |")
    print_border()
    print("| 1. Admin Panel                    |")
    print("| 2. User Panel                     |")
    print("| 3. Exit                           |")
    print_border()

# ================= ADMIN PANEL =================
def admin_panel():
    password = input(YELLOW + "Enter Admin Password: " + RESET)

    if password != "ayush123":
        print(RED + "Incorrect Admin Password!" + RESET)
        return

    while True:
        print(f"\n{BOLD}{MAGENTA}Admin Panel{RESET}")
        print_border()
        print("1. Add Candidate")
        print("2. Delete Candidate")
        print("3. View Results")
        print("4. Logout")
        print_border()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_candidate()
        elif choice == "2":
            delete_candidate()
        elif choice == "3":
            display_results()
        elif choice == "4":
            return
        else:
            print(RED + "Invalid choice!" + RESET)

# ================= ADD CANDIDATE =================
def add_candidate():
    if len(candidates) >= MAX_CANDIDATES:
        print(RED + "Candidate list is full!" + RESET)
        return

    name = input("Enter Candidate Name: ").strip()
    symbol = input("Enter Candidate Symbol: ").strip()

    candidates.append(Candidate(name, symbol))
    print(GREEN + "Candidate Added Successfully!" + RESET)

# ================= DELETE CANDIDATE =================
def delete_candidate():
    name = input("Enter Candidate Name to Delete: ").strip()

    for i, candidate in enumerate(candidates):
        if candidate.name == name:
            candidates.pop(i)
            print(GREEN + "Candidate Deleted Successfully!" + RESET)
            return

    print(RED + "Candidate Not Found!" + RESET)

# ================= USER PANEL =================
def user_panel():
    voter_id = input(YELLOW + "Enter College ID (ABC1234567): " + RESET).strip()

    if not is_valid_id(voter_id):
        print(RED + "Invalid ID Format!" + RESET)
        return

    if has_voted(voter_id):
        print(RED + "Fake Voter! You have already voted." + RESET)
        return

    cast_vote(voter_id)

# ================= ID VALIDATION =================
def is_valid_id(voter_id):
    if len(voter_id) != 10:
        return False

    if not voter_id[:3].isupper():
        return False

    if not voter_id[3:].isdigit():
        return False

    return True

def has_voted(voter_id):
    return voter_id in voted_ids

# ================= CAST VOTE =================
def cast_vote(voter_id):
    print(f"\n{BOLD}{CYAN}Candidates:{RESET}")
    print_border()

    for idx, candidate in enumerate(candidates, start=1):
        print(f"{idx}. {candidate.name} ({candidate.symbol})")

    print_border()

    try:
        choice = int(input("Enter Candidate Number to Vote: "))
        if choice < 1 or choice > len(candidates):
            raise ValueError
    except ValueError:
        print(RED + "Invalid Choice!" + RESET)
        return

    candidates[choice - 1].votes += 1
    voted_ids.append(voter_id)

    print(GREEN + "Vote Casted Successfully!" + RESET)

# ================= DISPLAY RESULTS =================
def display_results():
    print(f"\n{BOLD}{CYAN}Election Results:{RESET}")
    print_border()

    winner = None
    max_votes = -1

    for candidate in candidates:
        print(f"| {candidate.name:<15} | {candidate.votes:<6} |")
        if candidate.votes > max_votes:
            max_votes = candidate.votes
            winner = candidate.name

    print_border()
    print(f"\n{BOLD}{GREEN}Winner: **{winner if winner else 'No Winner'}**{RESET}")

# ================= MAIN FUNCTION =================
def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_panel()
        elif choice == "2":
            user_panel()
        elif choice == "3":
            print(YELLOW + "Exiting..." + RESET)
            break
        else:
            print(RED + "Invalid choice! Try again." + RESET)

# ================= PROGRAM START =================
if __name__ == "__main__":
    main()