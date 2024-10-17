import random
import colorama


#These are questions
def quiz_game():
    questions = [
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
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Leo Tolstoy"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
            "answer": "A"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
            "answer": "B"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["A) Tomato", "B) Avocado", "C) Pepper", "D) Onion"],
            "answer": "B"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["A) 1905", "B) 1912", "C) 1915", "D) 1920"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) Elephant", "B) Blue Whale", "C) Great White Shark", "D) Giraffe"],
            "answer": "B"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
            "answer": "C"
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["A) Helium", "B) Hydrogen", "C) Oxygen", "D) Lithium"],
            "answer": "B"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["A) Seoul", "B) Beijing", "C) Tokyo", "D) Bangkok"],
            "answer": "C"
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
            "answer": "B"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
            "answer": "C"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Diamond", "B) Gold", "C) Iron", "D) Quartz"],
            "answer": "A"
        },
        {
            "question": "Who discovered penicillin?",
            "options": ["A) Marie Curie", "B) Louis Pasteur", "C) Alexander Fleming", "D) Isaac Newton"],
            "answer": "C"
        },
        {
            "question": "Which organ in the human body is primarily responsible for detoxification?",
            "options": ["A) Heart", "B) Kidney", "C) Liver", "D) Lungs"],
            "answer": "C"
        },
        {
            "question": "What is the capital city of Australia?",
            "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
            "answer": "C"
        },
        {
            "question": "What is the most spoken language in the world?",
            "options": ["A) English", "B) Mandarin", "C) Spanish", "D) Hindi"],
            "answer": "B"
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
    ran_question = random.randint(0,33)
    
    return questions[ran_question]

def ask_question():
    sel_ques=quiz_game()
    print(f"Question is >> \t {sel_ques['question']} \n The OPTINS are >> \t {sel_ques['options']}")
    user_ans=input("The option SHOULD BE 'A, B, C or D \t\n")
    if user_ans not in ('A'or 'B'or'C'or'D'):
        print("Wrong Selection")
    elif user_ans == sel_ques['answer']:
        return True
    else:
        return False

print(ask_question())