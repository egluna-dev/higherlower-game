from art import logo, vs
from game_data import data
from random import randint


# Function that returns a random celebrity's profile
def random_celeb():
    random_index = randint(0, len(data) - 1)
    random_profile = data[random_index]
    celeb_profile = {
        "name": random_profile["name"],
        "follower_count": random_profile["follower_count"],
        "description": random_profile["description"],
        "country": random_profile["country"]
    }

    # return name, follower_count, description, country
    return celeb_profile


# Function compares follower counts and returns the largest count ie. correct answer
def compare_count(count_A, count_B):
    if count_A > count_B:
        return "a"
    else:
        return "b"


# Function creates a new round of celebrities to compare and returns their follower counts
def new_round():
    celeb_A = random_celeb()

    name_A = celeb_A["name"]
    follower_count_A = celeb_A["follower_count"]
    description_A = celeb_A["description"]
    country_A = celeb_A["country"]

    celeb_B = random_celeb()

    name_B = celeb_B["name"]
    follower_count_B = celeb_B["follower_count"]
    description_B = celeb_B["description"]
    country_B = celeb_B["country"]

    print(f"Compare A: {name_A}, a {description_A}, from {country_A}")
    print(vs)
    print(f"Against B: {name_B}, a {description_B}, from {country_B}")

    return follower_count_A, follower_count_B


# Function intializes game
def game_init():
    current_score = 0
    game_on = True

    while game_on:
        print(logo)

        user_incorrect = False

        while not user_incorrect:
            celeb_A, celeb_B = new_round()

            correct_answer = compare_count(celeb_A, celeb_B)

            print(f"Psst, the correct answer is {correct_answer}")

            user_select = input("Type 'A' or 'B': ")

            if user_select != 'a' and user_select != 'b':
                print("Please enter either 'a' or 'b'.")
            else:
                if user_select == correct_answer:
                    current_score += 1
                    print(f"You're right! Current score: {current_score}.\n")
                elif user_select != correct_answer:
                    game_on = False
                    user_incorrect = True
                    print(
                        f"Sorry, that's the wrong answer. Final score: {current_score}.")

                    play_again = input(
                        "Do you want to play again? Type 'y' if yes or 'n' to exit the game.\n")

                    if play_again == "y":
                        game_init()
                    elif play_again == "n":
                        game_on = False
                    else:
                        print("Please enter either 'y' or 'n'.\n")


game_init()
