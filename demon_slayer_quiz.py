import streamlit as st
import random

# Initialize session state variables if not set
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_complete" not in st.session_state:
    st.session_state.quiz_complete = False
if "last_answer_correct" not in st.session_state:
    st.session_state.last_answer_correct = None
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False
if "intensity" not in st.session_state:
    st.session_state.intensity = 1

quiz = [
    {"question": "What is the name of the main character in Demon Slayer?", "options": ["Zenitsu Agatsuma", "Tanjiro Kamado", "Inosuke Hashibira", "Kanao Tsuyuri"], "answer": "Tanjiro Kamado"},
    {"question": "Who killed Tanjiro’s family?", "options": ["Rui", "Muzan Kibutsuji", "Akaza", "Daki"], "answer": "Muzan Kibutsuji"},
    {"question": "Which breathing style does Tanjiro learn initially?", "options": ["Flame Breathing", "Water Breathing", "Thunder Breathing", "Beast Breathing"], "answer": "Water Breathing"},
    {"question": "Who is Tanjiro’s demon sister?", "options": ["Kanao Tsuyuri", "Mitsuri Kanroji", "Nezuko Kamado", "Shinobu Kocho"], "answer": "Nezuko Kamado"},
    {"question": "Who is the Flame Hashira?", "options": ["Gyomei Himejima", "Sanemi Shinazugawa", "Giyu Tomioka", "Kyojuro Rengoku"], "answer": "Kyojuro Rengoku"},
    {"question": "What unique ability does Nezuko have?", "options": ["Firing blood attacks", "Shadow control", "Immunity to sunlight", "Ice manipulation"], "answer": "Immunity to sunlight"},
    {"question": "Who uses Thunder Breathing?", "options": ["Zenitsu Agatsuma", "Inosuke Hashibira", "Tanjiro Kamado", "Obanai Iguro"], "answer": "Zenitsu Agatsuma"},
    {"question": "Which demon slayer wears a boar mask?", "options": ["Zenitsu Agatsuma", "Kanao Tsuyuri", "Inosuke Hashibira", "Tanjiro Kamado"], "answer": "Inosuke Hashibira"},
    {"question": "Who is the leader of the Demon Slayer Corps?", "options": ["Anosuke Hashibira", "Muzan Kibutsuji", "Gyomei Himejima", "Kagaya Ubuyashiki"], "answer": "Kagaya Ubuyashiki"},
    {"question": "What is the highest rank a demon slayer can achieve?", "options": ["Captain", "Hashira", "Leader", "Elite"], "answer": "Hashira"},

    {"question": "What is the main weapon used by Demon Slayers?", "options": ["Spears", "Katanas", "Nichirin Blades", "Swords"], "answer": "Nichirin Blades"},
    {"question": "Who is the Water Hashira?", "options": ["Kyojuro Rengoku", "Giyu Tomioka", "Sanemi Shinazugawa", "Muichiro Tokito"], "answer": "Giyu Tomioka"},
    {"question": "Which breathing style is unique to Mitsuri Kanroji?", "options": ["Love Breathing", "Insect Breathing", "Flame Breathing", "Wind Breathing"], "answer": "Love Breathing"},
    {"question": "Who created the Moon Breathing?", "options": ["Tamayo", "Muzan Kibutsuji", "Yoriichi Tsugikuni", "Kagaya Ubuyashiki"], "answer": "Yoriichi Tsugikuni"},
    {"question": "Which demon slayer uses Snake Breathing?", "options": ["Sanemi Shinazugawa", "Gyomei Himejima", "Obanai Iguro", "Muichiro Tokito"], "answer": "Obanai Iguro"},
    {"question": "What is the signature move of Water Breathing?", "options": ["Thunder Clap and Flash", "Water Surface Slash", "Flame Tiger", "Beast Head"], "answer": "Water Surface Slash"},
    {"question": "What mountain does Tanjiro train on?", "options": ["Mount Fuji", "Mount Sagiri", "Mount Hiei", "Mount Rokko"], "answer": "Mount Sagiri"},
    {"question": "Who is the Mist Hashira?", "options": ["Muichiro Tokito", "Shinobu Kocho", "Zenitsu Agatsuma", "Sanemi Shinazugawa"], "answer": "Muichiro Tokito"},
    {"question": "Which demon kills Sabito and Makomo?", "options": ["Rui", "Temari Demon", "Kaigaku", "Hand Demon"], "answer": "Hand Demon"},
    {"question": "What is the alternate dimension controlled by Nakime?", "options": ["Infinity Castle", "Shadow Realm", "Dream World", "Demon's Abyss"], "answer": "Infinity Castle"},

    {"question": "Which artifact is used to forge Nichirin Blades?", "options": ["Blue spider lily", "Flame Essence", "Dragon scales", "Special ore"], "answer": "Special ore"},
    {"question": "Who is the Spider Demon Family leader on Natagumo Mountain?", "options": ["Enmu", "Doma", "Akaza", "Rui"], "answer": "Rui"},
    {"question": "What technique gives Demon Slayers enhanced abilities?", "options": ["Magic", "Breathing Techniques", "Curses", "Spells"], "answer": "Breathing Techniques"},
    {"question": "Who sacrifices herself to poison Doma?", "options": ["Kanae Kocho", "Mitsuri Kanroji", "Kanao Tsuyuri", "Shinobu Kocho"], "answer": "Shinobu Kocho"},
    {"question": "Who wields the Insect Breathing style?", "options": ["Obanai Iguro", "Kanao Tsuyuri", "Shinobu Kocho", "Mitsuri Kanroji"], "answer": "Shinobu Kocho"},
    {"question": "Which Hashira is blind but extremely strong?", "options": ["Gyomei Himejima", "Kyojuro Rengoku", "Sanemi Shinazugawa", "Giyu Tomioka"], "answer": "Gyomei Himejima"},
    {"question": "Who is the Water Breathing master?", "options": ["Giyu Tomioka", "Tanjiro Kamado", "Sakonji Urokodaki", "Zenitsu Agatsuma"], "answer": "Sakonji Urokodaki"},
    {"question": "Which sword color does Tanjiro’s blade turn initially?", "options": ["Red", "Black", "Blue", "White"], "answer": "Black"},
    {"question": "What animal delivers messages for the Demon Slayer Corps?", "options": ["Owl", "Raven", "Crow", "Sparrow"], "answer": "Crow"},
    {"question": "What flower is used to poison demons?", "options": ["Spider Lily", "Rose", "Cherry Blossom", "Wisteria"], "answer": "Wisteria"},

    {"question": "Which demon art does Muzan Kibutsuji use?", "options": ["Flame Control", "Blood Demon Art", "Shadow Manipulation", "Illusion"], "answer": "Blood Demon Art"},
    {"question": "Which demon is immune to sunlight naturally?", "options": ["Muzan Kibutsuji", "Rui", "Akaza", "Nezuko Kamado"], "answer": "Nezuko Kamado"},
    {"question": "Who is the Thunder Hashira?", "options": ["Sanemi Shinazugawa", "Zenitsu Agatsuma", "Mitsuri Kanroji", "Inosuke Hashibira"], "answer": "Zenitsu Agatsuma"},
    {"question": "What is the key to defeating Upper Moon demons?", "options": ["Magic spells", "Decapitation with Nichirin Blade", "Sunlight exposure", "Water Breathing"], "answer": "Decapitation with Nichirin Blade"},
    {"question": "Which breathing style was created first?", "options": ["Love Breathing", "Sun Breathing", "Water Breathing", "Flame Breathing"], "answer": "Sun Breathing"},
    {"question": "Who uses Beast Breathing?", "options": ["Gyomei Himejima", "Inosuke Hashibira", "Tanjiro Kamado", "Sanemi Shinazugawa"], "answer": "Inosuke Hashibira"},
    {"question": "Who is the co-owner of Tamayo's medicines?", "options": ["Yushiro", "Muzan", "Kokushibo", "Akaza"], "answer": "Yushiro"},
    {"question": "What is the name of Zenitsu’s sparrow?", "options": ["Kaburamaru", "Ninju", "Chuntaro", "Amiko"], "answer": "Chuntaro"},
    {"question": "Which demon killed Sabito?", "options": ["Temari Demon", "Rui", "Akaza", "The Hand Demon"], "answer": "The Hand Demon"},
    {"question": "What is the name of the swordsmith who reforges Katana?", "options": ["Hotaru Haganezuka", "Kagaya Ubuyashiki", "Urokodaki", "Kokushibo"], "answer": "Hotaru Haganezuka"},

    {"question": "Who uses the Love Breathing technique?", "options": ["Mitsuri Kanroji", "Sanemi Shinazugawa", "Obanai Iguro", "Shinobu Kocho"], "answer": "Mitsuri Kanroji"},
    {"question": "What style does Sanemi Shinazugawa use?", "options": ["Water Breathing", "Love Breathing", "Wind Breathing", "Fire Breathing"], "answer": "Wind Breathing"},
    {"question": "What is the demon rank below Upper Moon?", "options": ["Midnight", "Lower Moon", "Foot Soldiers", "Mid Tier"], "answer": "Lower Moon"},
    {"question": "What is the name of the sound breathing user from training arc?", "options": ["Sanemi Shinazugawa", "Zenitsu Agatsuma", "Obanai Iguro", "Tengen Uzui"], "answer": "Tengen Uzui"},
    {"question": "Which Hashira fights on the Mugen Train?", "options": ["Sanemi Shinazugawa", "Mitsuri Kanroji", "Giyu Tomioka", "Kyojuro Rengoku"], "answer": "Kyojuro Rengoku"},
    {"question": "Who is the main antagonist in Swordsmith Village?", "options": ["Gyutaro", "Kaigaku", "Rui", "Daki"], "answer": "Gyutaro"},
    {"question": "Which Hashira is known for their stone-like strength?", "options": ["Sanemi Shinazugawa", "Gyomei Himejima", "Obanai Iguro", "Muichiro Tokito"], "answer": "Gyomei Himejima"},
    {"question": "Who is Tanjiro’s main rival and friend?", "options": ["Sanemi Shinazugawa", "Kanao Tsuyuri", "Inosuke Hashibira", "Zenitsu Agatsuma"], "answer": "Inosuke Hashibira"},
    {"question": "What causes demons to be vulnerable to Nichirin Blades?", "options": ["Water", "Salt", "Sunlight", "Fire"], "answer": "Sunlight"},
    {"question": "Who is the snake breathing user?", "options": ["Sanemi Shinazugawa", "Obanai Iguro", "Gyomei Himejima", "Muichiro Tokito"], "answer": "Obanai Iguro"},

    {"question": "Who is the youngest Hashira?", "options": ["Kanao Tsuyuri", "Muichiro Tokito", "Zenitsu Agatsuma", "Inosuke Hashibira"], "answer": "Muichiro Tokito"},
    {"question": "What is Muzan Kibutsuji’s primary goal?", "options": ["Become a Hashira", "Rule the Demon Slayer Corps", "Become immortal", "Destroy all demons"], "answer": "Become immortal"},
    {"question": "Who kills the demon Rui?", "options": ["Kyojuro Rengoku", "Tanjiro Kamado", "Zenitsu Agatsuma", "Inosuke Hashibira"], "answer": "Tanjiro Kamado"},
    {"question": "Which demon was formerly a doctor and creates medicine?", "options": ["Doma", "Tamayo", "Muzan", "Akaza"], "answer": "Tamayo"},
    {"question": "Which Hashira is obsessed with cleanliness and order?", "options": ["Sanemi Shinazugawa", "Gyomei Himejima", "Kyojuro Rengoku", "Obanai Iguro"], "answer": "Obanai Iguro"},
    {"question": "Which technique is Zenitsu best known for?", "options": ["Thunder Breathing: First Form", "Water Breathing: Fifth Form", "Flame Breathing: Third Form", "Moon Breathing"], "answer": "Thunder Breathing: First Form"},
    {"question": "Where is the Swordsmith Village located?", "options": ["Mount Sagiri", "Mount Natagumo", "Taisho Era Japan", "Hidden Forest"], "answer": "Mount Natagumo"},
    {"question": "What is the main setting era of Demon Slayer?", "options": ["Modern Era", "Meiji Era", "Taishō Era", "Edo Period"], "answer": "Taishō Era"},
    {"question": "Which character is Tanjiro’s closest friend and supports him the most?", "options": ["Zenitsu Agatsuma", "Shinobu Kocho", "Inosuke Hashibira", "Kanao Tsuyuri"], "answer": "Zenitsu Agatsuma"},
    {"question": "Who wields Flame Breathing?", "options": ["Giyu Tomioka", "Obanai Iguro", "Muichiro Tokito", "Kyojuro Rengoku"], "answer": "Kyojuro Rengoku"}
]



correct_feedback = {
    1: [  # Low intensity
        "Meow, you got it right.",
        "Right!",
        "Good job, meow",
        "Meow meow, that’s correct.",
        "Well done meow",
        "You did well",
        "Nice one!",
        "Correct, nya.",
        "Keep it up, meow.",
        "You’re my favorite kitty"
    ],
    2: [  # Medium intensity
        "Meow meow! That’s right",
        "Yippee! Mew mew!",
        "Good job, meow!",
        "You’re pawsome, mew!",
        "Keep going meow.",
        "So fun!",
        "Hehe, mew mew correct!",
        "Nyaa! You got it!",
        "Purrfect!",
        "You’re my favorite kitty!"
    ],
    3: [  # High intensity
        "Yay! Mew mew mew!",
        "OMG meow! I want all your kittens!",
        "Totally purrfect, mew mew mew!",
        "You’re the bestest kitty, meow meow!",
        "Meow-wow! I’m so proud of you, mew!",
        "Heehee, mew mew mew mew!",
        "Fur real? You’re amazing",
        "Mew mew mew! Love you, meow!",
        "You’re the cat’s whiskers, meow!",
        "You da bestest kitty here, mew mew!"
    ]
}

incorrect_feedback = [
    "Oops, Are you a muggle? Try again meow",
    "Wrong answer, meow!",
    "That’s muggle level..",
    "Oh no, wow..no",
    "Close, but not really meow!",
    "Muggle alert!",
    "EWW!",
    "Excuse ME! That's a NO.",
    "Meow mew! try once more!",
    "Nope, that’s a muggle move"
]

def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False
    st.session_state.last_answer_correct = None
    st.session_state.show_feedback = False
    st.session_state.intensity = 1
    if "started" in st.session_state:
        del st.session_state.started

def select_intensity():
    st.title("Select your Meowness Intensity")
    options = ["Low", "Medium", "High"]
    choice = st.radio("Choose your level", options, index=0, key="intensity_choice")
    intensity_map = {"Low": 1, "Medium": 2, "High": 3}
    st.session_state.intensity = intensity_map[choice]
    if st.button("Start"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_complete = False
        st.session_state.last_answer_correct = None
        st.session_state.show_feedback = False
        st.session_state.started = True
        st.rerun()

def show_question():
    idx = st.session_state.current_question
    q = quiz[idx]

    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(f"Question {idx + 1} / {len(quiz)}")
    with col2:
        st.metric("Score", f"{st.session_state.score}")

    st.write(q["question"])
    choice = st.radio("Choose:", q["options"], key=f"q{idx}")

    if not st.session_state.show_feedback:
        if st.button("Submit"):
            correct = (choice == q["answer"])
            st.session_state.last_answer_correct = correct
            if correct:
                st.session_state.score += 1
            st.session_state.show_feedback = True
            st.rerun()
    else:
        if st.session_state.last_answer_correct:
            intensity = st.session_state.intensity
            message = random.choice(correct_feedback[intensity])
            st.success(message)
        else:
            message = random.choice(incorrect_feedback)
            st.error(f"{message} The correct answer is {q['answer']}.")

        if idx == len(quiz) - 1:
            st.session_state.show_feedback = False
            st.session_state.quiz_complete = True
            st.rerun()
        else:
            if st.button("Next Question"):
                st.session_state.current_question += 1
                st.session_state.show_feedback = False
                st.rerun()

def show_results():
    total_questions = 60  # Total number of questions in the app
    score = st.session_state.score  # Final score

    # Highlighted large score display
    st.markdown(f'<h1 style="color: #FF4500;">Your final score: {score} / {total_questions}</h1>', unsafe_allow_html=True)

    # Define 6 statements mapped to score ranges
    final_statements = [
        "Don't worry meow, every kitty starts somewhere meow!",
        "Meow! You're learning steadily, great job meow!",
        "Nice! You're making good progress, keep those paws moving meow!",
        "Purrfect! You're doing really well, almost like a clever cat meow!",
        "Amazing! You're almost a master kitty. OMG meow, looks like mating season is around the corner meow!",
        "Fur real, you are the bestest kitty around! MEOW! I want to have your kittens meow!"
    ]


    # Determine which statement to show based on score range
    if score <= 10:
        message = final_statements[0]
    elif score <= 20:
        message = final_statements[1]
    elif score <= 30:
        message = final_statements[2]
    elif score <= 40:
        message = final_statements[3]
    elif score <= 50:
        message = final_statements[4]
    else:
        message = final_statements[5]

    st.markdown(f"### {message}")

    # Optional: Play again button
    if st.button("Play Again"):
        restart_quiz()
        st.rerun()


if "started" not in st.session_state or not st.session_state.started:
    select_intensity()
elif not st.session_state.quiz_complete:
    show_question()
else:
    show_results()

