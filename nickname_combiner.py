import random
import sys

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    _HAS_COLOR = True
except ImportError:
    _HAS_COLOR = False

nickname_history = []


def get_input(prompt):
    return input(prompt).strip()


def combine_style1(name1, name2):
    """First 2 letters of name1 + last 2 letters of name2"""
    return name1[:2] + name2[-2:]


def combine_style2(name1, name2):
    """First half of name1 + second half of name2"""
    mid1 = len(name1)//2
    mid2 = len(name2)//2
    return name1[:mid1] + name2[mid2:]


def combine_style3(name1, name2):
    """Random characters from both names"""
    pick1 = ''.join(random.choice(name1) for _ in range(2))
    pick2 = ''.join(random.choice(name2) for _ in range(2))
    return pick1 + pick2


def combine_style4(name1, name2):
    """First 3 letters of both names"""
    return name1[:3] + name2[:3]


def combine_style5(name1, name2):
    """Reversed combinations"""
    return name2[::-1][:2] + name1[::-1][:2]


def generate_meaning():
    """Generate a fun meaning for the nickname"""
    adjectives = ['Brave', 'Smart', 'Cool', 'Funny', 'Creative', 'Lucky', 'Charming', 'Energetic']
    return random.choice(adjectives)


def display_nickname(nickname):
    if _HAS_COLOR:
        print(Fore.CYAN + f"Generated Nickname: {nickname}" + Style.RESET_ALL)
    else:
        print(f"Generated Nickname: {nickname}")


def choose_style(name1, name2):
    print("\nChoose nickname style:")
    print("1. First 2 letters of Name1 + last 2 letters of Name2")
    print("2. First half of Name1 + Second half of Name2")
    print("3. Random characters from both names")
    print("4. First 3 letters of both names")
    print("5. Reversed combinations")
    choice = get_input("Enter style number (1-5): ")
    if choice == '1':
        return combine_style1(name1, name2)
    elif choice == '2':
        return combine_style2(name1, name2)
    elif choice == '3':
        return combine_style3(name1, name2)
    elif choice == '4':
        return combine_style4(name1, name2)
    elif choice == '5':
        return combine_style5(name1, name2)
    else:
        print("Invalid choice, using default style 1")
        return combine_style1(name1, name2)


def main():
    print("=== Auto Nickname Combiner ===")
    while True:
        name1 = get_input("Enter first name: ")
        name2 = get_input("Enter second name: ")

        nickname = choose_style(name1, name2)
        meaning = generate_meaning()
        display_nickname(nickname)
        print(f"Nickname meaning: {meaning}")

        nickname_history.append({'nickname': nickname, 'meaning': meaning})

        cont = get_input("\nDo you want to generate another nickname? (y/n): ").lower()
        if cont != 'y':
            print("\n=== Session History ===")
            for idx, item in enumerate(nickname_history, start=1):
                print(f"{idx}. {item['nickname']} — {item['meaning']}")
            print("Goodbye!")
            sys.exit(0)


if __name__ == '__main__':
    main()
