import streamlit as st
import random


easy_quiz = [
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

# --- Hard quiz questions (advanced set I created) ---
hard_quiz = [
    {"question": "What is the full name of Tanjiro's swordsmith?", "options": ["Hotaru Haganezuka", "Kotetsu Haganezuka", "Hotaru Hanagazaka", "Haruto Haganezuka"], "answer": "Hotaru Haganezuka"},
    {"question": "Which Hashira lost his left arm after his battle with Kokushibo?", "options": ["Gyomei Himejima", "Obanai Iguro", "Sanemi Shinazugawa", "Muichiro Tokito"], "answer": "Obanai Iguro"},
    {"question": "How many total forms does the Hinokami Kagura (Sun Breathing) have as shown in the anime and manga?", "options": ["10", "13", "15", "12"], "answer": "13"},
    {"question": "Who is the only Hashira to wield a weapon other than a sword?", "options": ["Tengen Uzui", "Sanemi Shinazugawa", "Gyomei Himejima", "Kyojuro Rengoku"], "answer": "Tengen Uzui"},
    {"question": "What is the name of the Upper Moon One demon?", "options": ["Kokushibo", "Muzan Kibutsuji", "Doma", "Akaza"], "answer": "Kokushibo"},
    {"question": "Which demon possesses six arms and fights with weighted kusarigama?", "options": ["Akaza", "Susamaru", "Gyutaro", "Nakime"], "answer": "Susamaru"},
    {"question": "What material is key to forging Nichirin blades?", "options": ["Ore infused with sunlight", "Iron from a meteorite", "Special ore infused with sunlight", "Dragon scales"], "answer": "Special ore infused with sunlight"},
    {"question": "Which Hashira is blind but renowned for immense strength?", "options": ["Gyomei Himejima", "Kyojuro Rengoku", "Muichiro Tokito", "Sanemi Shinazugawa"], "answer": "Gyomei Himejima"},
    {"question": "Who is responsible for developing the anti-demon drug used by Demon Slayers?", "options": ["Tamayo", "Muzan Kibutsuji", "Kagaya Ubuyashiki", "Yushiro"], "answer": "Tamayo"},
    {"question": "Which Hashira uses Insect Breathing?", "options": ["Shinobu Kocho", "Mitsuri Kanroji", "Kanao Tsuyuri", "Obanai Iguro"], "answer": "Shinobu Kocho"},
    {"question": "Who is the demon known as the Drum Demon?", "options": ["Kyogai", "Rui", "Hantengu", "Gyutaro"], "answer": "Kyogai"},
    {"question": "Which form of Water Breathing does Tanjiro often use?", "options": ["Water Surface Slash", "Dance of the Fire God", "Thunderclap and Flash", "Beast Head"], "answer": "Water Surface Slash"},
    {"question": "What is the name of the alternate dimension where Upper Moons battle?", "options": ["Infinity Castle", "Shadow Realm", "Dream World", "Demon Abyss"], "answer": "Infinity Castle"},
    {"question": "What is the specific weakness that Nezuko has which differs from other demons?", "options": ["Immunity to sunlight", "Cannot consume human blood", "Cannot use Blood Demon Art", "No regeneration"], "answer": "Immunity to sunlight"},
    {"question": "Who was the original creator of the Sun Breathing technique?", "options": ["Yoriichi Tsugikuni", "Kagaya Ubuyashiki", "Tanjiro Kamado", "Muzan Kibutsuji"], "answer": "Yoriichi Tsugikuni"},
    {"question": "What is the name of the flower used to poison demons?", "options": ["Wisteria", "Spider Lily", "Cherry Blossom", "Lotus"], "answer": "Wisteria"},
    {"question": "Which demon ranked as Upper Moon Six has a sister named Daki?", "options": ["Gyutaro", "Kaigaku", "Doma", "Akaza"], "answer": "Gyutaro"},
    {"question": "Which of the following Hashira has the fastest breathing technique?", "options": ["Zenitsu Agatsuma", "Kyojuro Rengoku", "Muichiro Tokito", "Tengen Uzui"], "answer": "Zenitsu Agatsuma"},
    {"question": "What is the full name of the Hashira known as the Mist Hashira?", "options": ["Muichiro Tokito", "Sanemi Shinazugawa", "Obanai Iguro", "Tengen Uzui"], "answer": "Muichiro Tokito"},
    {"question": "What is the specific curse that Upper Moon Four Hantengu uses?", "options": ["Multiple body splits into clones", "Poison gas attack", "Illusory flames", "Super speed"], "answer": "Multiple body splits into clones"},
    {"question": "How many Hashira are there in total?", "options": ["9", "10", "12", "13"], "answer": "9"},
    {"question": "Which Hashira specializes in Love Breathing?", "options": ["Mitsuri Kanroji", "Shinobu Kocho", "Kanao Tsuyuri", "Obanai Iguro"], "answer": "Mitsuri Kanroji"},
    {"question": "Who trained Tanjiro in Water Breathing techniques?", "options": ["Sakonji Urokodaki", "Kyojuro Rengoku", "Shinobu Kocho", "Gyomei Himejima"], "answer": "Sakonji Urokodaki"},
    {"question": "What is the name of Zenitsu's sparrow?", "options": ["Chuntaro", "Kaburamaru", "Kaze", "Hibari"], "answer": "Chuntaro"},
    {"question": "Which Hashira fights using Sound Breathing?", "options": ["Tengen Uzui", "Obanai Iguro", "Sanemi Shinazugawa", "Gyomei Himejima"], "answer": "Tengen Uzui"},
    {"question": "What blood-related ability does Muzan Kibutsuji possess that aids his regeneration?", "options": ["Blood Demon Art", "Honing regenerative cells", "Blood puppeteering", "Poison manipulation"], "answer": "Blood Demon Art"},
    {"question": "Who is the demon that was previously a doctor and allies with Tamayo?", "options": ["Tamayo", "Tamashi", "Kokushibo", "Akaza"], "answer": "Tamayo"},
    {"question": "Which demon slayer was once engaged to Koyuki?", "options": ["Akaza", "Kokushibo", "Doma", "Gyutaro"], "answer": "Akaza"},
    {"question": "Who is the main antagonist in the Swordsmith Village Arc?", "options": ["Gyutaro", "Daki", "Upper Moon Three", "Kaigaku"], "answer": "Gyutaro"},
    {"question": "What is the rank immediately below Upper Moon among demons?", "options": ["Lower Moon", "Midnight", "Foot Soldiers", "Mid Tier"], "answer": "Lower Moon"},
    {"question": "Which Hashira carries a boar mask?", "options": ["Inosuke Hashibira", "Sanemi Shinazugawa", "Zenitsu Agatsuma", "Kanao Tsuyuri"], "answer": "Inosuke Hashibira"},
    {"question": "What is the full name of the demon who controls the Infinity Castle?", "options": ["Nakime", "Kokushibo", "Muzan Kibutsuji", "Gyutaro"], "answer": "Nakime"},
    {"question": "What is the primary fighting style of Sanemi Shinazugawa?", "options": ["Wind Breathing", "Flame Breathing", "Water Breathing", "Beast Breathing"], "answer": "Wind Breathing"},
    {"question": "Who is the youngest Hashira ever introduced?", "options": ["Muichiro Tokito", "Kanao Tsuyuri", "Zenitsu Agatsuma", "Inosuke Hashibira"], "answer": "Muichiro Tokito"},
    {"question": "Where is the Swordsmith Village located?", "options": ["Mount Natagumo", "Mount Sagiri", "Taisho Era Japan", "Mount Rokko"], "answer": "Mount Natagumo"},
    {"question": "Who is the co-owner of Tamayo's medicines?", "options": ["Yushiro", "Muzan Kibutsuji", "Kokushibo", "Gyomei Himejima"], "answer": "Yushiro"},
    {"question": "What color does Tanjiro’s Nichirin blade change to after mastering the Hinokami Kagura?", "options": ["Red", "Black", "Blue", "White"], "answer": "Red"},
    {"question": "Who is the main caregiver and mentor to Kanao Tsuyuri?", "options": ["Shinobu Kocho", "Mitsuri Kanroji", "Kagaya Ubuyashiki", "Obanai Iguro"], "answer": "Shinobu Kocho"},
    {"question": "Which demon slayer's fighting style is known as 'Beast Breathing'?", "options": ["Inosuke Hashibira", "Zenitsu Agatsuma", "Tanjiro Kamado", "Sanemi Shinazugawa"], "answer": "Inosuke Hashibira"},
    {"question": "How many siblings does Tanjiro Kamado have, including Nezuko?", "options": ["6", "5", "7", "8"], "answer": "6"},
    {"question": "What is the name of the swordsmith who reforges Tanjiro’s sword after it breaks?", "options": ["Hotaru Haganezuka", "Kokushibo", "Yushiro", "Urokodaki"], "answer": "Hotaru Haganezuka"},
    {"question": "Which Hashira died protecting the Mugen Train passengers?", "options": ["Kyojuro Rengoku", "Gyomei Himejima", "Tengen Uzui", "Shinobu Kocho"], "answer": "Kyojuro Rengoku"},
    {"question": "Who is the first demon that Tanjiro kills with his new Hinokami Kagura technique?", "options": ["Rui", "Enmu", "Kyogai", "Hand Demon"], "answer": "Rui"},
    {"question": "Who is the Hashira famous for their extreme obsession with cleanliness?", "options": ["Obanai Iguro", "Sanemi Shinazugawa", "Zenitsu Agatsuma", "Mitsuri Kanroji"], "answer": "Obanai Iguro"},
    {"question": "Which demon uses a set of hand fans and explosive techniques?", "options": ["Tengen Uzui", "Sanemi Shinazugawa", "Gyomei Himejima", "Tanjiro Kamado"], "answer": "Tengen Uzui"},
    {"question": "What is Tanjiro’s primary motivation for joining the Demon Slayer Corps?", "options": ["To avenge his family and cure Nezuko", "To become the strongest swordsman", "To find a cure for all demons", "To protect the Wisteria family"], "answer": "To avenge his family and cure Nezuko"},
    {"question": "Which Hashira is known as the Serpent Hashira?", "options": ["Obanai Iguro", "Sanemi Shinazugawa", "Gyomei Himejima", "Tengen Uzui"], "answer": "Obanai Iguro"},
    {"question": "What is the special property of the Wisteria flower in the Demon Slayer universe?", "options": ["It poisons demons", "It enhances breathing techniques", "It is a source of sunlight", "It strengthens Nichirin Blades"], "answer": "It poisons demons"},
    {"question": "Who is the demon that maintained a close relationship with Muzan and was known for creating medicine?", "options": ["Tamayo", "Doma", "Akaza", "Kokushibo"], "answer": "Tamayo"},
    {"question": "Who trains Zenitsu in his Thunder Breathing techniques?", "options": ["Tanmura", "Sakonji Urokodaki", "Kyojuro Rengoku", "Zenitsu is mostly self-taught"], "answer": "Zenitsu is mostly self-taught"}
]

advanced_quiz = [
    {"question": "Which Upper Moon did Muichiro Tokito defeat before his death?", "options": ["Hantengu", "Gyokko", "Daki", "Gyutaro"], "answer": "Gyokko"},
    {"question": "What was the original human name of Kokushibo before turning into a demon?", "options": ["Michikatsu Tsugikuni", "Yoriichi Tsugikuni", "Kazuya Tsugikuni", "Hotaru Tsugikuni"], "answer": "Michikatsu Tsugikuni"},
    {"question": "How many times was Muzan Kibutsuji nearly killed before the final battle?", "options": ["Once", "Twice", "Three times", "Four times"], "answer": "Twice"},
    {"question": "Which Pillar is the first to unlock the Demon Slayer Mark among the modern Hashira?", "options": ["Giyu Tomioka", "Muichiro Tokito", "Tanjiro Kamado", "Kyojuro Rengoku"], "answer": "Muichiro Tokito"},
    {"question": "What condition must be met for a Demon Slayer Mark to awaken?", "options": ["Body temperature above 39°C", "Killing an Upper Moon", "Touching sunlight", "Training under a Hashira"], "answer": "Body temperature above 39°C"},
    {"question": "What is the true purpose of the Transparent World ability?", "options": ["Perceive opponent’s muscles and movements", "See demons in the dark", "Avoid sunlight damage", "Enhance sword speed"], "answer": "Perceive opponent’s muscles and movements"},
    {"question": "Who preserved Yoriichi Tsugikuni’s hanafuda earrings and passed them down to Tanjiro’s family?", "options": ["Sumiyoshi", "Tanjiro’s father", "Kagaya Ubuyashiki", "Tamayo"], "answer": "Sumiyoshi"},
    {"question": "What is the rarest color a Nichirin Blade can take, symbolizing full mastery of all breathing forms?", "options": ["Crimson Red", "Black", "Rainbow", "Gold"], "answer": "Crimson Red"},
    {"question": "What is the main drawback of activating the Demon Slayer Mark?", "options": ["Shortens life expectancy", "Weakens vision", "Increases demon attraction", "Causes rapid aging"], "answer": "Shortens life expectancy"},
    {"question": "Which Upper Moon’s death directly caused Muzan to begin panicking for the first time?", "options": ["Gyutaro and Daki", "Akaza", "Kokushibo", "Doma"], "answer": "Akaza"},
    {"question": "What is the human emotion that fueled Akaza’s strength as a demon?", "options": ["Wrath", "Grief", "Pride", "Loyalty"], "answer": "Grief"},
    {"question": "Who succeeded Kagaya Ubuyashiki after his death?", "options": ["Kiriya Ubuyashiki", "Amane Ubuyashiki", "Tanjiro Kamado", "Giyu Tomioka"], "answer": "Kiriya Ubuyashiki"},
    {"question": "Which breathing technique is a derivative of Flame Breathing?", "options": ["Love Breathing", "Serpent Breathing", "Mist Breathing", "Sound Breathing"], "answer": "Love Breathing"},
    {"question": "Which two Hashira gained the Demon Slayer Mark after the battle with Gyokko and Hantengu?", "options": ["Mitsuri Kanroji and Muichiro Tokito", "Sanemi Shinazugawa and Giyu Tomioka", "Tengen Uzui and Shinobu Kocho", "Kyojuro Rengoku and Giyu Tomioka"], "answer": "Mitsuri Kanroji and Muichiro Tokito"},
    {"question": "What happens to Nichirin Blades when they are turned crimson during battle?", "options": ["Inhibit demon regeneration", "Increase cutting speed", "Emit light", "Become unbreakable"], "answer": "Inhibit demon regeneration"},
    {"question": "What Breathing Style did Yoriichi create as the foundation for all others?", "options": ["Sun Breathing", "Flame Breathing", "Water Breathing", "Void Breathing"], "answer": "Sun Breathing"},
    {"question": "Who was the first demon to ever betray Muzan Kibutsuji?", "options": ["Tamayo", "Akaza", "Rui", "Kaigaku"], "answer": "Tamayo"},
    {"question": "What is the primary difference between the Demon Slayer Mark and the Transparent World?", "options": ["Mark enhances power, Transparent World improves perception", "They are the same ability", "Both grant speed only", "Transparent World is exclusive to demons"], "answer": "Mark enhances power, Transparent World improves perception"},
    {"question": "Which Upper Moon used emotional clones to fight?", "options": ["Hantengu", "Doma", "Akaza", "Gyokko"], "answer": "Hantengu"},
    {"question": "What is the relation between Yoriichi and Michikatsu Tsugikuni?", "options": ["Twin brothers", "Father and son", "Mentor and student", "Distant cousins"], "answer": "Twin brothers"},
    {"question": "Which Hashira is the only one known to have retired alive after the Entertainment District Arc?", "options": ["Tengen Uzui", "Sanemi Shinazugawa", "Gyomei Himejima", "Kyojuro Rengoku"], "answer": "Tengen Uzui"},
    {"question": "Who developed the antidote used to turn Nezuko back into a human?", "options": ["Tamayo", "Yushiro", "Urokodaki", "Kagaya"], "answer": "Tamayo"},
    {"question": "What rank was Kaigaku before becoming a demon?", "options": ["Demon Slayer Corps member", "Lower Moon One", "Hashira", "Zenitsu’s senior disciple"], "answer": "Zenitsu’s senior disciple"},
    {"question": "What did Muzan absorb to reach his final form?", "options": ["Tamayo’s medicine", "Nezuko’s blood", "Blue Spider Lily essence", "Kokushibo’s cells"], "answer": "Blue Spider Lily essence"},
    {"question": "Which Hashira discovered Nezuko’s resistance to sunlight first?", "options": ["Sanemi Shinazugawa", "Giyu Tomioka", "Mitsuri Kanroji", "Obanai Iguro"], "answer": "Sanemi Shinazugawa"},
    {"question": "Who initially proposed the idea of Demon Slayers forming ranks?", "options": ["Kagaya Ubuyashiki", "Yoriichi Tsugikuni", "Amane Ubuyashiki", "Tamayo"], "answer": "Kagaya Ubuyashiki"},
    {"question": "What is the symbolic meaning of Tanjiro’s black Nichirin blade?", "options": ["Unknown potential and rarity", "Failure to master Flame Breathing", "Cursed steel", "Sign of weakness"], "answer": "Unknown potential and rarity"},
    {"question": "What is the name of Tanjiro’s father?", "options": ["Tanjuro Kamado", "Sumiyoshi", "Takero Kamado", "Kengen Kamado"], "answer": "Tanjuro Kamado"},
    {"question": "Which demon was once a monk before becoming an Upper Moon?", "options": ["Akaza", "Kokushibo", "Doma", "Gyutaro"], "answer": "Doma"},
    {"question": "Who was the first Hashira to die in combat against the Upper Moons?", "options": ["Kyojuro Rengoku", "Muichiro Tokito", "Shinobu Kocho", "Mitsuri Kanroji"], "answer": "Kyojuro Rengoku"},
    {"question": "What emotion caused Akaza’s regeneration to increase mid-battle?", "options": ["Respect", "Rage", "Fear", "Regret"], "answer": "Respect"},
    {"question": "Which demon consumed the most humans among Muzan’s Twelve Kizuki?", "options": ["Doma", "Akaza", "Kokushibo", "Rui"], "answer": "Doma"},
    {"question": "What technique lets users momentarily see the Transparent World via breath control?", "options": ["Selfless State", "Marked Vision", "Breath Sync Mode", "Perfect Concentration"], "answer": "Selfless State"},
    {"question": "Who was responsible for sealing Muzan inside the Infinity Castle during the final battle?", "options": ["Nakime", "Tamayo", "Yushiro", "Giyu Tomioka"], "answer": "Yushiro"},
    {"question": "How is Yushiro different from typical demons?", "options": ["Created willingly and retains humanity", "Sunlight immune", "No Blood Demon Art", "Cannot heal"], "answer": "Created willingly and retains humanity"},
    {"question": "Which Upper Moon’s demise caused Tanjiro to briefly lose consciousness from exhaustion?", "options": ["Gyutaro", "Akaza", "Gyokko", "Rui"], "answer": "Gyutaro"},
    {"question": "What flower did Muzan fail to locate for centuries?", "options": ["Blue Spider Lily", "Wisteria", "Lotus Blossom", "Moon Lily"], "answer": "Blue Spider Lily"},
    {"question": "Who utilizes the ‘Constant Total Concentration Breathing’ technique at all times?", "options": ["Tanjiro Kamado", "Zenitsu Agatsuma", "Kanao Tsuyuri", "Giyu Tomioka"], "answer": "Tanjiro Kamado"},
    {"question": "What specific ability does Nezuko gain when awakened in her advanced demon form?", "options": ["Full sunlight resistance", "Awareness speech", "Instant regeneration", "Mind control immunity"], "answer": "Full sunlight resistance"},
    {"question": "Which demon referred to humans as ‘fragile art pieces’?", "options": ["Gyokko", "Doma", "Rui", "Akaza"], "answer": "Gyokko"},
    {"question": "What weapon does Gyomei Himejima use in battle?", "options": ["Flail and axe", "Greatsword", "Chain-spear", "Dual gloves"], "answer": "Flail and axe"},
    {"question": "What ranking did Kanao Tsuyuri achieve before mastering Flower Breathing Final Form?", "options": ["Tsuguko", "Pillar", "Intermediate", "Upper Rank apprentice"], "answer": "Tsuguko"},
    {"question": "Who awakened Tanjiro from Muzan’s blood influence at the end of the series?", "options": ["Nezuko", "Kanao", "Yushiro", "Giyu Tomioka"], "answer": "Kanao"},
    {"question": "What is the origin of the Demon Slayer Corps according to the manga?", "options": ["Formed by Yoriichi’s disciples", "Formed by Tamayo’s followers", "Created after Muzan’s first slaughter", "A royal samurai order"], "answer": "Formed by Yoriichi’s disciples"},
    {"question": "Who was the first person Yoriichi ever saved from a demon?", "options": ["Sumire", "Sumiyoshi", "Tanjuro", "Hanako Kamado"], "answer": "Sumiyoshi"},
    {"question": "Which demon can manipulate space within a castle-like area?", "options": ["Nakime", "Doma", "Akaza", "Kaigaku"], "answer": "Nakime"},
    {"question": "How many Upper Moons existed at peak of Muzan’s rule?", "options": ["Six", "Twelve", "Nine", "Seven"], "answer": "Six"},
    {"question": "Which Hashira was the final one to die in the series?", "options": ["Obanai Iguro", "Mitsuri Kanroji", "Gyomei Himejima", "Sanemi Shinazugawa"], "answer": "Gyomei Himejima"},
    {"question": "What made Kokushibo’s Blood Demon Art so dangerous?", "options": ["Created blades from his flesh", "Manipulated blood illusions", "Used poison sound waves", "Split bodies into clones"], "answer": "Created blades from his flesh"},
    {"question": "Who was Tanjiro’s last opponent as a human?", "options": ["Muzan Kibutsuji", "Akaza", "Kokushibo", "Enmu"], "answer": "Muzan Kibutsuji"},
    {"question": "Which technique did Yoriichi use that even Muzan couldn’t counter?", "options": ["Thirteenth Form of Sun Breathing", "Transparent World", "Crimson Blade Slash", "Hinokami Dance"], "answer": "Thirteenth Form of Sun Breathing"},
    {"question": "What caused Zenitsu to invent his unique Thunder Breathing technique variation?", "options": ["Survival instinct after Kaigaku’s betrayal", "Training failure", "Hashira advice", "Rage against Muzan"], "answer": "Survival instinct after Kaigaku’s betrayal"},
    {"question": "Which demon was immune to Tamayo’s anti-demon drug?", "options": ["Muzan Kibutsuji", "Akaza", "Kokushibo", "Gyutaro"], "answer": "Muzan Kibutsuji"},
    {"question": "What element did Flame Breathing focus on mastering?", "options": ["Heart rhythm synchronization", "Speed bursts", "Raw power and precision", "Arcing motion"], "answer": "Raw power and precision"},
    {"question": "Which two characters reincarnate together in modern Japan according to the manga epilogue?", "options": ["Obanai Iguro and Mitsuri Kanroji", "Sanemi and Genya", "Giyu and Shinobu", "Tanjiro and Nezuko"], "answer": "Obanai Iguro and Mitsuri Kanroji"},
    {"question": "What is the symbolic pattern of the Ubuyashiki family's curse?", "options": ["Facial decay and short lifespan", "Blindness in male heirs", "Loss of voice", "Uncontrolled aging"], "answer": "Facial decay and short lifespan"},
    {"question": "What is the ability that allows demons to survive decapitation by Nichirin Blades?", "options": ["Regeneration exceeding threshold", "Evolutional merger", "Muzan’s direct blood link", "Armored skin"], "answer": "Muzan’s direct blood link"},
    {"question": "Which demon’s body disintegrated out of acceptance rather than pain?", "options": ["Akaza", "Gyokko", "Rui", "Doma"], "answer": "Akaza"},
    {"question": "Which character was said to most closely resemble Yoriichi in spirit and combat style?", "options": ["Tanjiro Kamado", "Giyu Tomioka", "Kyojuro Rengoku", "Muichiro Tokito"], "answer": "Tanjiro Kamado"},
    {"question": "What family heirloom inspired Tanjiro’s breathing transformation?", "options": ["The Dance of the Fire God", "Wisteria crest", "Blue spider lily scroll", "Kamado crest"], "answer": "The Dance of the Fire God"}
]

god_level_quiz = [
    {
        "question": "What is the kanji meaning and symbolic significance of Yoriichi Tsugikuni’s hanafuda earrings?",
        "options": [
            "Sun and Moon; symbolizing life and death balance",
            "Two dragons; representing strength and duality",
            "Sun; representing the original source of all Breathing Styles",
            "Cherry blossoms; symbolizing fleeting life"
        ],
        "answer": "Sun; representing the original source of all Breathing Styles"
    },
    {
        "question": "Mechanically, what physiological change occurs that causes the Demon Slayer Mark to shorten the user’s lifespan?",
        "options": [
            "Accelerated cellular metabolism and energy expenditure",
            "Immune system compromise due to overbreathing",
            "Mutation of blood cells by the mark’s energy",
            "Brain overload from enhanced sensory input"
        ],
        "answer": "Accelerated cellular metabolism and energy expenditure"
    },
    {
        "question": "Which breathing styles share identical root movements derived from [translate:日輪] Sun Breathing, and which diverge completely?",
        "options": [
            "Flame, Love, and Serpent Breathing share root movements; Mist Breathing diverges",
            "Water, Thunder, and Beast Breathing share root movements; Flame diverges",
            "Flame, Water, and Wind Breathing share root movements; Love diverges",
            "Love, Mist, and Sound Breathing share root movements; Serpent diverges"
        ],
        "answer": "Flame, Love, and Serpent Breathing share root movements; Mist Breathing diverges"
    },
    {
        "question": "How many times did Muzan Kibutsuji clone himself during the final battle before his death?",
        "options": [
            "2 times",
            "5 times",
            "7 times",
            "10 times"
        ],
        "answer": "7 times"
    },
    {
        "question": "What is the full name and notable personality traits of the swordsmith who reforges Tanjiro’s blade?",
        "options": [
            "Hotaru Haganezuka; strict and obsessive about cleanliness",
            "Tetsuo Haganezuka; jovial but forgetful",
            "Hotaru Haganezuka; eccentric, temperamental, but highly skilled",
            "Sakonji Urokodaki; wise and patient mentor"
        ],
        "answer": "Hotaru Haganezuka; eccentric, temperamental, but highly skilled"
    },
    {
        "question": "Explain how the melody played by the Drum Demon (Kyogai) enhances his Blood Demon Art’s power?",
        "options": [
            "The melody manipulates spatial dimensions to trap opponents",
            "Playing different rhythms changes his strength and attack patterns",
            "Specific drumbeats emit sound waves that generate shockwaves",
            "The melody induces illusions that weaken enemy resolve"
        ],
        "answer": "The melody manipulates spatial dimensions to trap opponents"
    },
    {
        "question": "Which Hashira’s breathing style incorporates techniques inspired explicitly by traditional Taishō-era martial arts?",
        "options": [
            "Sanemi Shinazugawa’s Wind Breathing",
            "Tengen Uzui’s Sound Breathing",
            "Muichiro Tokito’s Mist Breathing",
            "Kyojuro Rengoku’s Flame Breathing"
        ],
        "answer": "Sanemi Shinazugawa’s Wind Breathing"
    },
    {
        "question": "Name the demon classification system invented by Muzan among the Twelve Kizuki including extinct ranks mentioned only in databooks.",
        "options": [
            "Upper Moon, Lower Moon, Shadow Clan",
            "Upper Moon Six, Forgotten Moon, Scripted Moon",
            "Upper Moon, Lower Moon, Former Moon",
            "Kizuki Alpha, Beta, and Gamma series"
        ],
        "answer": "Upper Moon, Lower Moon, Former Moon"
    },
    {
        "question": "Describe the historical and symbolic significance of the Wisteria flower in Demon Slayer lore.",
        "options": [
            "Signifies protection due to its poisonous properties against demons",
            "Represents fleeting happiness and lost loved ones",
            "Symbolizes the bond between Tanjiro and Nezuko",
            "Associated with the Demon Slayer Corps’ origin mythology"
        ],
        "answer": "Signifies protection due to its poisonous properties against demons"
    },
    {
        "question": "Outline Yushiro’s timeline from human to demon and explain how his creation differs from normal demons.",
        "options": [
            "Volunteered to become a demon; retains humanity via Tamayo’s medicine",
            "Forced transformation by Muzan; lacks regeneration capabilities",
            "Born a demon due to Muzan’s bloodline; can use sunlight",
            "Experimented on by Kagaya; gains unique breathing forms"
        ],
        "answer": "Volunteered to become a demon; retains humanity via Tamayo’s medicine"
    },
    {
        "question": "What exact event caused the Demon Slayer Corps to shift their hierarchy from Captains to Hashira?",
        "options": [
            "The emergence of the Upper Moons",
            "Kagaya Ubuyashiki’s reformations post World War I",
            "Death of the original twelve Pillars",
            "Tanjiro’s rise as a symbol of hope"
        ],
        "answer": "Kagaya Ubuyashiki’s reformations post World War I"
    },
    {
        "question": "In the lore, which classical Japanese myth is the Sun Breathing technique most closely related to?",
        "options": [
            "Amaterasu, the sun goddess",
            "Susanoo, god of storms",
            "Tsukuyomi, the moon god",
            "Yamato Takeru, the warrior prince"
        ],
        "answer": "Amaterasu, the sun goddess"
    },
    {
        "question": "What mental state must a Demon Slayer enter to activate the Transparent World and gain enhanced perception?",
        "options": [
            "Selfless State",
            "Perfect Focus State",
            "Total Concentration Breathing",
            "Breath of the Void"
        ],
        "answer": "Selfless State"
    },
    {
        "question": "How did Gyomei Himejima lose his sight according to manga lore?",
        "options": [
            "In a fierce battle with a demon",
            "Due to a childhood high fever",
            "Born blind",
            "Curse from Muzan"
        ],
        "answer": "Due to a childhood high fever"
    },
    {
        "question": "What dark history is connected to Daki’s original human name, Ume?",
        "options": [
            "Named after her mother’s illness",
            "Name means 'beautiful flower'",
            "Name bears a royal lineage",
            "Derived from a demon clan"
        ],
        "answer": "Named after her mother’s illness"
    },
    {
        "question": "What rare blood property does Sanemi Shinazugawa possess that is advantageous against demons?",
        "options": [
            "Marechi blood that makes demons dizzy",
            "Immunity to demon toxins",
            "Heals rapidly from injuries",
            "Enhanced regeneration"
        ],
        "answer": "Marechi blood that makes demons dizzy"
    },
    {
        "question": "What physical attribute do Muzan Kibutsuji and Sanemi Shinazugawa coincidentally share?",
        "options": [
            "Same height and weight",
            "Same eye color",
            "Identical scars",
            "Same hair color"
        ],
        "answer": "Same height and weight"
    },
    {
        "question": "What hidden family trait affects the Ubuyashiki lineage?",
        "options": [
            "Facial decay and shortened lifespan",
            "Blindness in male heirs",
            "Loss of voice in women",
            "Cursed with inability to use breathing"
        ],
        "answer": "Facial decay and shortened lifespan"
    },
    {
        "question": "What unique ability does Tanjiro Kamado’s mother possess in an unshown backstory?",
        "options": [
            "Defeated a wild boar by headbutting it",
            "Had the potential for Sun Breathing",
            "Created the first Nichirin Blade",
            "Was a Hashira before death"
        ],
        "answer": "Defeated a wild boar by headbutting it"
    },
    {
        "question": "How does the Blue Spider Lily contribute to the story’s lore regarding Muzan Kibutsuji?",
        "options": [
            "It blooms seldom and affects his immortality",
            "It is the source of demon power",
            "It is the key to demon regeneration",
            "It causes demon weakness to sunlight"
        ],
        "answer": "It blooms seldom and affects his immortality"
    },
    {
        "question": "What was the original purpose of the Kasugai Crows in the Demon Slayer Corps?",
        "options": [
            "Deliver mission instructions",
            "Serve as combat companions",
            "Form bonds with demon slayers",
            "Track demons’ locations"
        ],
        "answer": "Deliver mission instructions"
    },
    {
        "question": "Which creator concept involved Inosuke’s Kasugai Crow constantly hiding due to his aggressive nature?",
        "options": [
            "His crow tries to avoid being eaten by Inosuke",
            "The crow acts as a spy for Muzan",
            "It is invisible only to Inosuke",
            "It is the only crow controlled directly by Muzan"
        ],
        "answer": "His crow tries to avoid being eaten by Inosuke"
    },
    {
        "question": "What is the reason Sakonji Urokodaki hides his face behind a mask?",
        "options": [
            "Mocked by demons for his kind face",
            "Disfigured in battle",
            "Family tradition",
            "To hide his identity from Muzan"
        ],
        "answer": "Mocked by demons for his kind face"
    },
    {
        "question": "Which Upper Moon demons are siblings sharing a close bond and tragic fate?",
        "options": [
            "Gyutaro and Daki",
            "Akaza and Kokushibo",
            "Doma and Rui",
            "Hantengu and Gyokko"
        ],
        "answer": "Gyutaro and Daki"
    },
    {
        "question": "In the final battle, which demon possessed the ability to split their body into multiple clones?",
        "options": [
            "Upper Moon Four Hantengu",
            "Kokushibo",
            "Akaza",
            "Gyutaro"
        ],
        "answer": "Upper Moon Four Hantengu"
    },
    {
        "question": "What unique property allows Nezuko Kamado to defy demon rules about sunlight?",
        "options": [
            "Inherited immunity due to special blood",
            "Protected by a rare Wisteria flower toxin",
            "She is partially human",
            "Tamayo’s medicine effect"
        ],
        "answer": "Inherited immunity due to special blood"
    },
    {
        "question": "Who is known as the ‘Stone Hashira’ and is unique among demon slayers for his blindness and physical power?",
        "options": [
            "Gyomei Himejima",
            "Sanemi Shinazugawa",
            "Tengen Uzui",
            "Obanai Iguro"
        ],
        "answer": "Gyomei Himejima"
    },
    {
        "question": "What is the reason behind Zenitsu Agatsuma being mostly self-taught in Thunder Breathing?",
        "options": [
            "His master abandoned training",
            "He developed it after surviving a betrayal",
            "Training was cut short due to an injury",
            "It was passed down only orally"
        ],
        "answer": "He developed it after surviving a betrayal"
    },
    {
        "question": "Which breathing style’s musical theme inspired Tengen Uzui’s Sound Breathing?",
        "options": [
            "Traditional Japanese festival drumming",
            "Western classical music",
            "Modern pop music",
            "Nature sounds"
        ],
        "answer": "Traditional Japanese festival drumming"
    },
    {
        "question": "Who served as the inspiration and mentor for Tanjiro’s Water Breathing technique?",
        "options": [
            "Sakonji Urokodaki",
            "Giyu Tomioka",
            "Kyojuro Rengoku",
            "Zenitsu Agatsuma"
        ],
        "answer": "Sakonji Urokodaki"
    },
    {
        "question": "What is the name of the village where the Demon Slayer swordsmiths reside?",
        "options": [
            "Mount Natagumo",
            "Mount Sagiri",
            "Swordsmith Village",
            "Taisho Village"
        ],
        "answer": "Mount Natagumo"
    },
    {
        "question": "Which demon is notorious for his cult following and masochistic tendencies?",
        "options": [
            "Doma",
            "Akaza",
            "Kokushibo",
            "Gyutaro"
        ],
        "answer": "Doma"
    },
    {
        "question": "What hidden duality does Zenitsu Agatsuma’s boar mask wear signify?",
        "options": [
            "His wild and gentle nature",
            "Family lineage and rebellion",
            "Stealth and charge",
            "Fear and courage"
        ],
        "answer": "His wild and gentle nature"
    },
    {
        "question": "Which demon’s body was said to disintegrate peacefully due to acceptance rather than pain?",
        "options": [
            "Akaza",
            "Rui",
            "Doma",
            "Gyokko"
        ],
        "answer": "Akaza"
    },
    {
        "question": "What weapon does Gyomei Himejima wield that differs from other Hashira?",
        "options": [
            "Flail and axe chained together",
            "Dual katanas",
            "Spear and shield",
            "Bow and arrows"
        ],
        "answer": "Flail and axe chained together"
    },
    {
        "question": "Which Hashira holds the rank of the youngest ever introduced in the series?",
        "options": [
            "Muichiro Tokito",
            "Kanao Tsuyuri",
            "Zenitsu Agatsuma",
            "Inosuke Hashibira"
        ],
        "answer": "Muichiro Tokito"
    },
    {
        "question": "In the manga epilogue, which two characters reincarnate together in modern Japan?",
        "options": [
            "Obanai Iguro and Mitsuri Kanroji",
            "Tanjiro Kamado and Nezuko Kamado",
            "Giyu Tomioka and Shinobu Kocho",
            "Sanemi Shinazugawa and Genya"
        ],
        "answer": "Obanai Iguro and Mitsuri Kanroji"
    },
    {
        "question": "Who saved Kagaya Ubuyashiki’s daughters Hinaki and Nichika, strengthening their bond through adversity?",
        "options": [
            "Their mother",
            "Tanjiro Kamado",
            "Kagaya Ubuyashiki himself",
            "Gyomei Himejima"
        ],
        "answer": "Kagaya Ubuyashiki himself"
    },
    {
        "question": "What technique did Yoriichi Tsugikuni use that Muzan Kibutsuji famously could not counter?",
        "options": [
            "Thirteenth Form of Sun Breathing",
            "Transparent World",
            "Crimson Blade Slash",
            "Hinokami Kagura Final Form"
        ],
        "answer": "Thirteenth Form of Sun Breathing"
    },
    {
        "question": "Which demon kills Shinobu Kocho in the manga’s battle arcs?",
        "options": [
            "Doma",
            "Akaza",
            "Kokushibo",
            "Gyutaro"
        ],
        "answer": "Doma"
    },
    {
        "question": "What is the name of the rarity classification for humans with blood more appealing yet dizzying to demons, like Sanemi Shinazugawa?",
        "options": [
            "Marechi",
            "Himechi",
            "Kizuki",
            "Hashira Blood"
        ],
        "answer": "Marechi"
    },
    {
        "question": "Which Hashira is known for obsession with cleanliness and order, linked to his snake breathing style?",
        "options": [
            "Obanai Iguro",
            "Sanemi Shinazugawa",
            "Gyomei Himejima",
            "Tengen Uzui"
        ],
        "answer": "Obanai Iguro"
    },
    {
        "question": "What is the formal name given to the Demon Slayer Corps’ final rigorous test?",
        "options": [
            "Final Selection",
            "Hashira Trial",
            "Breath Challenge",
            "Night Hunt"
        ],
        "answer": "Final Selection"
    },
    {
        "question": "What rare flower blooms only for a few dozen minutes annually and factors into Muzan’s plans?",
        "options": [
            "Blue Spider Lily",
            "Wisteria",
            "Cherry Blossom",
            "Moon Lily"
        ],
        "answer": "Blue Spider Lily"
    },
    {
        "question": "Who originally developed Tamayo’s anti-demon medicine?",
        "options": [
            "Tamayo herself",
            "Yushiro",
            "Kagaya Ubuyashiki",
            "Sakonji Urokodaki"
        ],
        "answer": "Tamayo herself"
    },
    {
        "question": "What unique bond do Hashira Mitsuri Kanroji and Obanai Iguro share?",
        "options": [
            "Romantic relationship",
            "Siblings",
            "Teacher and student",
            "Fellow beasts at training"
        ],
        "answer": "Romantic relationship"
    },
    {
        "question": "Which Hashira wears the distinctive boar mask as a combat identity?",
        "options": [
            "Inosuke Hashibira",
            "Zenitsu Agatsuma",
            "Sanemi Shinazugawa",
            "Kanao Tsuyuri"
        ],
        "answer": "Inosuke Hashibira"
    },
    {
        "question": "What is the hidden cultural reference behind the Nishiran Blade color changes when wielded by different demon slayers?",
        "options": [
            "Connection to the wielder’s spirit and strength",
            "Symbolizing elemental affinity",
            "Random forged steel impurities",
            "Signify rank within the Corps"
        ],
        "answer": "Connection to the wielder’s spirit and strength"
    },
    {
        "question": "What is the origin of the ‘Dance of the Fire God’ technique Tanjiro uses?",
        "options": [
            "Passed down uniquely in Kamado family",
            "A lost form of Sun Breathing",
            "Derived from an ancient flame dance ceremony",
            "Learned from Kyojuro Rengoku"
        ],
        "answer": "A lost form of Sun Breathing"
    },
    {
        "question": "Who is the demon that controls the space and dimensions inside the Infinity Castle?",
        "options": [
            "Nakime",
            "Kokushibo",
            "Muzan Kibutsuji",
            "Gyutaro"
        ],
        "answer": "Nakime"
    },
    {
        "question": "Which form of breathing does not derive from Sun Breathing and stands uniquely?",
        "options": [
            "Mist Breathing",
            "Flame Breathing",
            "Love Breathing",
            "Serpent Breathing"
        ],
        "answer": "Mist Breathing"
    },
    {
        "question": "How many times did Yoriichi Tsugikuni confront Muzan Kibutsuji in combat?",
        "options": [
            "Once",
            "Twice",
            "Three times",
            "Never"
        ],
        "answer": "Twice"
    },
    {
        "question": "What ancient weapon is believed to be the inspiration behind Nichirin Blades?",
        "options": [
            "Katana forged using sunlight-infused ore",
            "Ancient legendary spear",
            "Sacred flame dagger",
            "Samurai ancestral blade"
        ],
        "answer": "Katana forged using sunlight-infused ore"
    },
    {
        "question": "What is the nature of demons’ inability to fully digest humans in Demon Slayer?",
        "options": [
            "They consume but later regurgitate humans",
            "They absorb only human blood",
            "They are allergic to human flesh",
            "They can only feed on demon corpses"
        ],
        "answer": "They consume but later regurgitate humans"
    },
    {
        "question": "What was the original inspiration for the naming of the Twelve Kizuki?",
        "options": [
            "Moon phases",
            "Twelve zodiac animals",
            "Twelve demon lords",
            "Twelve pillars of darkness"
        ],
        "answer": "Moon phases"
    },
    {
        "question": "Which breathing technique involves synchronizing heart rhythm with sword movements?",
        "options": [
            "Flame Breathing",
            "Sound Breathing",
            "Water Breathing",
            "Love Breathing"
        ],
        "answer": "Flame Breathing"
    },
    {
        "question": "Who is the mysterious character that taught the Hinokami Kagura dance to Tanjiro’s family?",
        "options": [
            "Tanjuro Kamado",
            "Urokodaki",
            "Kagaya Ubuyashiki",
            "Tamayo"
        ],
        "answer": "Tanjuro Kamado"
    },
    {
        "question": "Which demon slayer was known to have a secret habit of blowing soap bubbles in Butterfly Mansion?",
        "options": [
            "Kanao Tsuyuri",
            "Mitsuri Kanroji",
            "Shinobu Kocho",
            "Kagaya Ubuyashiki"
        ],
        "answer": "Kanao Tsuyuri"
    },
    {
        "question": "What unique ability does Zenitsu’s sparrow, Chuntaro, famously have?",
        "options": [
            "Warning him of danger",
            "Guiding him to enemies",
            "Delivering messages",
            "Disappearing when scared"
        ],
        "answer": "Warning him of danger"
    }
]


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
if "difficulty" not in st.session_state:
    st.session_state.difficulty = None


# Assign quiz based on difficulty selection, including advanced
if st.session_state.difficulty == "Easy":
    quiz = easy_quiz
elif st.session_state.difficulty == "Hard":
    quiz = hard_quiz
elif st.session_state.difficulty == "Advanced":
    quiz = advanced_quiz
elif st.session_state.difficulty == "GOD Level":
    quiz = god_level_quiz
else:
    quiz = []


correct_feedback = [
    "Good job, meow!",
    "Meow meow, that’s correct!",
    "Well done meow!",  
    "Nice one!",
    "Correct, nya.",
    "Keep it up, meow !",
    "You’re my favorite Kitty !!"
]

incorrect_feedback = [
    "Oops, Are you a muggle? Try again meow.",
    "Wrong meow..",
    "That’s muggle level..",
    "Nya meow",
    "Close, but not really meow..",
    "Muggle alert!",
    "EWW!"
]


def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False
    st.session_state.last_answer_correct = None
    st.session_state.show_feedback = False
    st.session_state.difficulty = None
    if "started" in st.session_state:
        del st.session_state.started


def select_difficulty():
    st.title("Select your Difficulty Level")
    options = ["Easy", "Hard", "Advanced", "GOD Level"]
    choice = st.radio("Choose difficulty level", options, index=0, key="difficulty_choice")
    st.session_state.difficulty = choice
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
    choice = st.radio("Choose:", q["options"], key=f"question_{idx}_{st.session_state.difficulty}")

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
            message = random.choice(correct_feedback)
            st.success(message)
        else:
            message = random.choice(incorrect_feedback)
            st.error(f"{message}  \n The correct answer is {q['answer']}.")

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
    total_questions = len(quiz)
    score = st.session_state.score

    st.markdown(f'<h1 style="color: #FF4500;">Your final score: {score} / {total_questions}</h1>', unsafe_allow_html=True)

    percent = (score / total_questions) * 100
    final_statements = [
        "Every kitty starts somewhere meow!",
        "Meow! You're learning steadily",
        "You're making good progress meow!",
        "You're almost like a clever cat meow!",
        "OMG meow, You're almost a Master Level! Looks like mating season is around the corner meow!",
        "Fur real ? You're the Bestest Kitty around! MEOW! I want to have your Kittens meow!"
    ]

    if percent < 20:
        message = final_statements[0]
    elif percent < 40:
        message = final_statements[1]
    elif percent < 60:
        message = final_statements[2]
    elif percent < 80:
        message = final_statements[3]
    elif percent < 95:
        message = final_statements[4]
    else:
        message = final_statements[5]

    st.markdown(f"### {message}")

    if st.button("Play Again"):
        restart_quiz()
        st.rerun()


# --- App Flow control ---
if "started" not in st.session_state or not st.session_state.started:
    select_difficulty()
elif not st.session_state.quiz_complete:
    show_question()
else:
    show_results()
