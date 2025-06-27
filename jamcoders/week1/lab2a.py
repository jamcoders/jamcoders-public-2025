# For answer checking without revealing the answer
def check_answers(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


def check_answer_0_1(answer):
    check_answers(answer, False, "0.1")

def check_answer_0_2(answer):
    check_answers(answer, False, "0.2")

def check_answer_0_3(answer):
    check_answers(answer, True, "0.3")

def check_answer_0_4(answer):
    check_answers(answer, True, "0.4")

def check_answer_0_5(answer):
    check_answers(answer, True, "0.5")

def check_answer_0_6(answer):
    check_answers(answer, False, "0.6")

def check_answer_0_7(answer):
    check_answers(answer, True, "0.7")

def check_answer_0_8(answer):
    check_answers(answer, True, "0.8")

def check_answer_1_1(answer):
    check_answers(answer, "B", "1.1")

def check_answer_1_2(answer):
    check_answers(answer, "C", "1.2")

def check_answer_2_0(answer):
    check_answers(answer, "It's not too hot.", "2.0")

def check_answer_2_4(answer1, answer2):
    answers = [answer1] + [answer2]
    check_answers(answers, [2,1], "2.4")

def check_answer_2_6(answer):
    check_answers(answer, ['Perfect day for the beach!', 'Wear a hoodie and bring a raincoat.', 'Dress warmly, it’s cold out.', 'Wear shorts and take an umbrella.'], "2.6")

def check_answer_3_1(answer_A, answer_B, answer_C, answer_D):
    answers = [answer_A] + [answer_B] +[answer_C] +[answer_D] 
    check_answers(answers, [2,1,4,3], "3.1")

def check_answer_3_4(answer):
    check_answers(answer, "I am cool.", "3.4")

def check_answer_4_4(ans):
    answers = [False,True,False,False,True,True,True]
    for i in range(len(answers)):
        check_answers(ans[i],answers[i], i+1)

# Choose your own adventure game
def play_game():
    # Setting up our whole story 
    input_request = "Enter your choice: "
    error_message = "Alas, you didn't select A, B, or C properly." 

    # Q1: Moat - B
    moat_scene = "Wonderful witch Adrianna arrives at the murky moat surrounding the castle, where giant alligators \npatrol the waters. She must make her way past this first obstacle to break into the castle and get \ncloser to rescuing Prince Manolis.\n"
    moat_question = "How should wonderful witch Adrianna get by the agitated alligators?\n"
    moat_option_a = "\tA: Fly over the moat on your broomstick.\n"
    moat_option_b = "\tB: Cast a sleep spell on the alligators and sneak across the bridge.\n"
    moat_option_c = "\tC: Toss some enchanted fish into the moat to distract them while she wades across.\n"

    moat_response_a = "A sudden gust knocks Adrianna off her broom, splashing her into the moat before she scrambles out, soaked.\n"
    moat_response_b = "The alligators drift into enchanted slumber, and Adrianna tiptoes across safely.\n"
    moat_response_c = "The gators finish the fish too quickly and start chasing Adrianna, forcing her to sprint back to shore.\n"

    # Q2: Inner Courtyard - A 
    courtyard_scene = "Adrianna gracefully enters the inner courtyard, and quickly hides in the doorway. The dragon's minions \nare swarming the area, guarding the stairwell!\n"
    courtyard_question = "What should wonderful witch Adrianna do to get by the guards?\n"
    courtyard_option_a = "\tA: Disguise herself as a minion using a quick glamor spell.\n"
    courtyard_option_b = "\tB: Throw a glitterbomb potion to distract them.\n"
    courtyard_option_c = "\tC: Bribe them with enchanted candies to let her pass.\n" 

    courtyard_response_a = "Adrianna's nose grows pointy, and she shuffles past unnoticed while they argue about chores.\n"
    courtyard_response_b = "The potion explodes too early, covering Adrianna in glitter and making her easy to spot. The minions \nchase Adrianna around the courtyard before she narrowly escapes.\n"
    courtyard_response_c = "They take the candies but demand even more, blocking Adrianna's way with sticky hands.\n"

    # Q3: Tower Stairs - A 
    tower_scene = "Adrianna avoids detection and shuts the door behind her, but Emberwing's smoky breath fills the stairwell.\n"
    tower_question = "How should the wonderful witch safely make it to the top of the tower?\n"
    tower_option_a = "\tA: Summon a wind spell to clear the smoke.\n"
    tower_option_b = "\tB: Hold her breath and dash through.\n"
    tower_option_c = "\tC: Use her cloak of shadows to move unseen through the smoke.\n"

    tower_response_a = "A gust swirls the smoke away, clearing Adrianna's path up the stairs.\n"
    tower_response_b = "Halfway up, she gasps, coughing and tumbling back down, dazed.\n"
    tower_response_c = "Adrianna trips over her own cloak in the thick smoke, landing with a thud that echoes loudly.\n"

    # Q4: Cage - C 
    cage_scene = "Finally at the top, Adrianna finds Prince Manolis chained in a glowing cage.\n"
    cage_question = "Adrianna has to choose how to break him out.\n"
    cage_option_a = "\tA: Use her crystal wand to unlock the cage.\n"
    cage_option_b = "\tB: Search the room for a hidden key left by a friendly mouse.\n"
    cage_option_c = "\tC: Whisper a freeing spell into the lock.\n"

    cage_response_a = "The wand sparks, but the lock refuses to open, and the noise alerts the minions downstairs.\n"
    cage_response_b = "She finds a key, but it is made of cheese—clearly a prank from the minions.\n"
    cage_response_c = "Her whispered words shimmer through the air and the chains fall away, freeing Manolis.\n"

    # Q5: Escape - B 
    escape_scene = "Emberwing catches on that an escape is happening! Wonderful witch Adrianna and Prince Manolis \nprepare to free.\n"
    escape_question = "What should they do to get away from the dragon?\n"
    escape_option_a = "\tA: Challenge Emberwing with a thunder spell so Manolis can run.\n"
    escape_option_b = "\tB: Ride her broom with Manolis out the window.\n"
    escape_option_c = "\tC: Hide under Adrianna's invisibility cloak and sneak out.\n"

    escape_response_a = "The spell fizzles, and Emberwing snorts smoke, forcing them both to hide behind a barrel.\n"
    escape_response_b = "Adrianna and Manolis narrowly escape, soaring into the moonlight, free at last! They return to safety, \nand the kingdom is finally free from the dragon's wrath, protected by the wonderful witch.\n"
    escape_response_c = "The wonderful witch trips over Manolis's foot under the cloak, knocking over a lantern with a loud clang.\n"

    # Ending Scenes
    fail_rescue = "Despite your best efforts, the wonderful witch Adrianna couldn't save Prince Manolis from Emberwing. \nThe tower looms dark as she retreats, her cloak torn and her wand dimming in the dawn mist. But in \nher heart, Adrianna vows she will return, braver and wiser, to try again..."

    # Start by assuming you'll succeed... 
    success = True
    proper_format = True

    # Turn 1: Crossing the Moat
    print(moat_scene + moat_question + moat_option_a + moat_option_b + moat_option_c)
    choice = input(input_request)

    if choice == "A":
        print(moat_response_a)
        success = False
    elif choice == "B": ## SUCCESS ## 
        print(moat_response_b)
    elif choice == "C":
        print(moat_response_c)
        success = False
    else:
        print(error_message)
        proper_format = False

    
    # Turn 2: Inner Courtyard
    # Only continue if you've succeeded so far
    if success and proper_format: 
            print(courtyard_scene + courtyard_question + courtyard_option_a + courtyard_option_b + courtyard_option_c)
            choice = input(input_request)

            if choice == "A": ## SUCCESS ## 
                print(courtyard_response_a)
            elif choice == "B": 
                print(courtyard_response_b)
                success = False
            elif choice == "C":
                print(courtyard_response_c)
                success = False
            else:
                print(error_message)
                proper_format = False

    # Turn 3: Tower Stairs
    # Only continue if you've succeeded so far
    if success and proper_format: 
            print(tower_scene + tower_question + tower_option_a + tower_option_b + tower_option_c)
            choice = input(input_request)

            if choice == "A": ## SUCCESS ## 
                print(tower_response_a)
            elif choice == "B": 
                print(tower_response_b)
                success = False
            elif choice == "C":
                print(tower_response_c)
                success = False
            else:
                print(error_message)
                proper_format = False

    # Turn 4:  Cage
    # Only continue if you've succeeded so far
    if success and proper_format: 
            print(cage_scene + cage_question + cage_option_a + cage_option_b + cage_option_c)
            choice = input(input_request)

            if choice == "A": 
                print(cage_response_a)
                success = False
            elif choice == "B": 
                print(cage_response_b)
                success = False
            elif choice == "C": ## SUCCESS ## 
                print(cage_response_c)
            else:
                print(error_message)
                proper_format = False

    # Turn 5: Escape
    # Only continue if you've succeeded so far
    if success and proper_format: 
            print(escape_scene + escape_question + escape_option_a + escape_option_b + escape_option_c)
            choice = input(input_request)

            if choice == "A": 
                print(escape_response_a)
                success = False
            elif choice == "B": ## SUCCESS ## 
                print(escape_response_b)
            elif choice == "C":
                print(escape_response_c)
                success = False
            else:
                print(error_message)
                proper_format = False


    if not success:
         print(fail_rescue)
