import random
from colorama import Fore, Back,Style 

<<<<<<< HEAD

#These are questions
def quiz_game():
    ran_question = random.randint(0,32)
    Fore.RED
   # questions obtained in the Gemini
    questions = [
=======
# resets the color to default after printing
colorama.init(autoreset=True)
# A function that create a list of questions
def questioner():
   # questions from Gemini AI  
   my_list_of_questions = [
>>>>>>> a7e9f57d24a806c1ee9ffb52d6e077b76d459fa3
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Arctic Ocean", "B) Indian Ocean", "C) Atlantic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A) 5", "B) 6", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Leo Tolstoy", "B) Mark Twain", "C) William Shakespeare", "D) Charles Dickens"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Au", "B) Pb", "C) Ag", "D) Fe"],
            "answer": "A"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A) Nitrogen", "B) Carbon Dioxide", "C) Oxygen", "D) Hydrogen"],
            "answer": "B"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["A) Pepper", "B) Avocado", "C) Tomato", "D) Onion"],
            "answer": "B"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["A) 1915", "B) 1912", "C) 1905", "D) 1921"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) Great White Shark", "B) Blue Whale", "C) Elephant", "D) Giraffe"],
            "answer": "B"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Pablo Picasso", "B) Vincent van Gogh", "C) Leonardo da Vinci", "D) Claude Monet"],
            "answer": "C"
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["A) Oxygen", "B) Hydrogen", "C) Helium", "D) Lithium"],
            "answer": "B"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["A) Beijing", "B) Seoul", "C) Tokyo", "D) Bangkok"],
            "answer": "C"
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
            "answer": "B"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A) Earth", "B) Venus", "C) Mercury", "D) Mars"],
            "answer": "C"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Diamond", "B) Iron", "C) Gold", "D) Quartz"],
            "answer": "A"
        },
        {
            "question": "Who discovered penicillin?",
            "options": ["A) Louis Pasteur", "B) Marie Curie", "C) Alexander Fleming", "D) Isaac Newton"],
            "answer": "C"
        },
        {
            "question": "Which organ in the human body is primarily responsible for detoxification?",
            "options": ["A) Kidney", "B) Heart", "C) Liver", "D) Lungs"],
            "answer": "C"
        },
        {
            "question": "What is the capital city of Australia?",
            "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
            "answer": "C"
        },
        {
            "question": "What is the most spoken language in the world?",
            "options": ["A)  Mandarin", "B)English", "C) Spanish", "D) Hindi"],
            "answer": "A"
        },
        {
            "question": "What is the currency of the United Kingdom?",
            "options": ["A) Euro", "B) Pound Sterling", "C) Dollar", "D) Yen"],
            "answer": "B"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
            "answer": "B"
        },
        {
            "question": "What is the largest desert in the world?",
            "options": ["A) Sahara", "B) Arabian", "C) Gobi", "D) Antarctic"],
            "answer": "D"
        },
        {
            "question": "What is the main language spoken in Brazil?",
            "options": ["A) Spanish", "B) Portuguese", "C) English", "D) French"],
            "answer": "B"
        },
        {
            "question": "Which famous scientist developed the theory of relativity?",
            "options": ["A) Isaac Newton", "B) Galileo Galilei", "C) Albert Einstein", "D) Stephen Hawking"],
            "answer": "C"
        },
        {
            "question": "What is the capital of Canada?",
            "options": ["A) Toronto", "B) Ottawa", "C) Vancouver", "D) Montreal"],
            "answer": "B"
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "options": ["A) Tiger", "B) Lion", "C) Bear", "D) Elephant"],
            "answer": "B"
        },
        {
            "question": "What is the primary ingredient in traditional hummus?",
            "options": ["A) Chickpeas", "B) Lentils", "C) Beans", "D) Peas"],
            "answer": "A"
        },
        {
            "question": "Which planet is known for its rings?",
            "options": ["A) Jupiter", "B) Saturn", "C) Neptune", "D) Uranus"],
            "answer": "B"
        },
        {
            "question": "In which continent is the Sahara Desert located?",
            "options": ["A) Asia", "B) North America", "C) Africa", "D) Australia"],
            "answer": "C"
        },
        {
            "question": "What is the capital of Italy?",
            "options": ["A) Florence", "B) Venice", "C) Rome", "D) Milan"],
            "answer": "C"
        },
        {
            "question": "Which element is essential for the formation of bones?",
            "options": ["A) Calcium", "B) Iron", "C) Potassium", "D) Magnesium"],
            "answer": "A"
        }
    ]
   # shuffle the list of questions
   random.shuffle(my_list_of_questions)
   # return the shuffle list
   return my_list_of_questions

<<<<<<< HEAD
def ask_question(sel_ques):
    print(Fore.BLUE+f"\t Question is \t>> \t {sel_ques['question']}") 
    print(Fore.GREEN+f"\t The OPTINS are >> \t {sel_ques['options']}"+Fore.YELLOW)
    user_ans=input("\t YOUR CHOICE \t>> \t")
    if user_ans  not in ('A' , 'B' , 'C' , 'D'):
       print("\t\tWrong Selection")
       sel_ques=quiz_game()
    elif user_ans == sel_ques['answer']:
        print("\t\tGreat! Right Answer")
        return True
    else:
        print(f"\t\tSorry! Wrong Answer")
        return False
score = 0

i = 1

while i<3:
    sel_ques=quiz_game() 
    ch_ans=ask_question(sel_ques)
    if ch_ans == False:
        score-=2
    elif ch_ans== True:
        score+=5
    i+=1
         

print(Fore.CYAN+f"The Total Score is >> \t {score}"+Style.RESET_ALL)
=======

def score(total_sc):
  # Final score message
  print(colorama.Fore.MAGENTA + f"Your score is: {total_sc}")
  if total_sc >= 15:
    print(colorama.Fore.GREEN + "Great job! ")
  elif total_sc >= 5:
    print(colorama.Fore.YELLOW + "Not so great! Keep it up!")
  else:
    print(colorama.Fore.RED + "Looser!")


def game():
    total_sc = 0
    questions = questioner()
    # A for loop iterating over a list["question"]    
    for a in questions:
        print(colorama.Fore.CYAN + a["question"])
        # A for loop iterating over a list["options"]    
        for b in a["options"]:
            print(colorama.Fore.GREEN + b)
        
        answer = input(colorama.Fore.YELLOW + "Enter your answer (A, B, C, or D): ").strip().upper()
        # while loop until get a valid choice ('A', 'B', 'C', 'D')
        while answer not in ['A', 'B', 'C', 'D']:
            print(colorama.Fore.RED + "Invalid input. Enter A, B, C, or D.")
            answer = input(colorama.Fore.YELLOW + "Enter your answer (A, B, C, or D): ").strip().upper()
        # checks the answer given and awards points
        if answer == a["answer"]:
            total_sc += 5
            print(colorama.Fore.GREEN + "Correct! You earned 5 points.")
        else:
            total_sc -= 2
            print(colorama.Fore.RED + "Incorrect! You lost 2 points.")
        # Adds spacing between questions
        print()  

    # Show the final score once after all questions are answered
    score(total_sc)
# the main function of program    
def main():
    # while loop to check if the user wants to continue
    while True:
      game()
      playing = input(colorama.Fore.CYAN + "Play again? (yes/no): ").strip().lower()
      if playing != 'yes':
         break

# Run the game
main()
>>>>>>> a7e9f57d24a806c1ee9ffb52d6e077b76d459fa3
