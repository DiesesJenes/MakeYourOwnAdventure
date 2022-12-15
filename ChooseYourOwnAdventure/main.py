from sys import exit


def check_if_input_correct():       # checking if the input the player has given is correct
    global answer, possibilities
    while True:
        if answer.lower().strip() in possibilities:
            return
        else:
            answer = input("Please input a correct answer: ")


def check_chase_timer():            # checking if the monster caught up
    global chase_timer
    if chase_timer == 0:
        print("""
        You hear the sound of cracking branches and you know that the monster caught up to you. Out of Fear 
        you try to run. The direction does not matter. You just want to escape.... but it is to late... the monster 
        jumps you and throws you to the ground as it claws threw you.... """)
        exit("You lost the game.... ")


answer = input("Do you want to play the game? (yes/no): ")
possibilities = ["yes", "no"]
check_if_input_correct()

if answer.lower().strip() == "no": 

    print("Ok then...")

elif answer.lower().strip() == "yes":

    chase_timer = 5

    print("""
    You are getting chased by a monster in a dark forrest.
    You have no idea how you got here or why the monster is chasing you.
    All you know for sure is that the monster is 
    approximately 5 minutes behind you and that you want to survive!
    Every choice will lead to you getting further ahead, the monster getting closer or you keeping the distance.""")

    answer = input("Do you want to run or turn around an fight the monster? (run/fight): ")
    possibilities = ["run", "fight"]
    check_if_input_correct()

    if answer.lower().strip() == "fight":

        print("""
        You decide to turn around and fight the monster one on one.
        The monster approaches in a hasty manner amd you can only hear the sounds of cracking branches and rustling 
        leaves as the monster comes closer and closer. Because of the darkness you can not see the monster getting 
        closer and so you realize that the monster has already slit your throat.
        
        You died and lost the game....""")

    elif answer.lower().strip() == "run":

        print("""
        You made the right decision. Without a weapon a fight is pointless and even with one on you dont know if 
        you could win.
        Your escape leads you deeper in the forrest were you come to a fast stop as you roughly spot two paths in
        front of you.""")

        answer = input("""
        What will you do next? you can go left or right. But before you run further you can also 
        take a look around, but this will cost you time. (right/left/investigate): """)
        possibilities = ["right", "left", "investigate"]
        check_if_input_correct()

        investigate = False
        loop_checker = 1
        while answer.lower().strip() == "investigate":
            if loop_checker == 1:
                print("""
                You take a look around. While you cant see any of your close surroundings except the dense
                trees,you spot a small glowing light further in the left path. The investigation costed you about
                1 minute.""")
                answer = input("What will you do next? (right/left/investigate): ")
                possibilities = ["right", "left", "investigate"]
                check_if_input_correct()
                chase_timer -= 1
                loop_checker += 1

            elif loop_checker > 1:
                print("""
                You do not spot anything else. This further investigation costed you an additional minute""")
                answer = input("What will you do now? (right/left/investigate): ")
                possibilities = ["right", "left", "investigate"]
                check_if_input_correct()
                chase_timer -= 1
                loop_checker += 1
                check_chase_timer()


        if answer.lower().strip() == "right":
            print("""
            You run down the right path. While you run you can spot a small light to your left that shines
            threw the trees. Because of you being distracted by the light you do not see the deep slope in front of 
            you and you fall to your death...
            You died and lost the game....""")

        elif answer.lower().strip() == "left":
            print("""
            You run down the left path. As you see the light at the end of the path it becomes brighter the
            more you run. The closer you get the more you think to yourself, that this light must be a torch
            someone left. And you are right. Someone left a lit torch stuck between two rocks. The next question for
            you is if you take the torch or if you leave it behind. The monster could track you more easily with a
            light source in your hands.""")

            answer = input("What will you do? Take the torch and keep running or leave it behind? (take/leave)")
            possibilities = ["take", "leave"]
            check_if_input_correct()
