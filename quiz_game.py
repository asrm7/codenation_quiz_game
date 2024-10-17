from colorama import init, Fore


init(autoreset=True) # Initialize Colorama

def quiz_game():
    # questions obtained in the Gemini
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
    
    

    total_score = 0
    random.shuffle(questions)  # Shuffle questions
