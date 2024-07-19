# Author: Ishita Agarwal

# List of words used in the game
words = ["apple", "banana", "cherry", "dates", "egg plant", "figs", "grapes", "honey", "ice cream", "jack fruit", "kiwi", "lemon", "melon", "mango", "nectar", "olive", "orange", "pear", "papaya", "pepper", "pineapple", "quince", "raisins", "rose", "strawberry", "tomato", "umbrella", "plum", "watermelon", "zucchini", "apricots", "avocado", "butterscotch", "vanila", "chocolate", "river", "hills", "mountains", "fish", "animals", "ocean", "sea", "sky", "flower", "spaghetti", "pasta", "pizza", "identity", "nationalism", "wired", "ripens", "strands", "hair", "moustache", "nut", "dive", "blink", "whole", "sculpture", "culprit", "criminal", "friend", "befriend", "life", "death", "space", "universe", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Bolivia", "Bosnia", "Herzegovina", "Botswana", "Brazil", "Croatia", "Cuba", "Cyprus", "Czechia", "Chad", "Chile", "China", "Colombia", "Denmark", "Djibouti", "Dominica", "Ecuador", "Egypt", "El Salvador", "Fiji", "Finland", "France", "Greece", "Germany", "Hawaii", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Korea", "Kuwait", "Kyrgyzstan", "Lithuania", "Luxembourg", "Latvia", "Lebanon", "Libya", "Madagascar", "Malaysia", "Maldives", "Micronesia", "Mexico", "Mongolia", "Morocco", "Nepal", "Netherlands", "New Zealand", "Nigeria", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Korea", "Congo", "Sudan", "Sweden", "Switzerland", "Syria", "Serbia", "Slovenia", "Somalia", "Slovakia", "Spain", "South Africa", "Sri Lanka", "Tajikistan", "Tanzania", "Thailand", "Uganda", "Ukraine", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Washington DC", "Yemen", "Zambia", "Zimbabwe"]

# Dictionary of words as keys and a list of their hints as the values, which are randomly shown in the game
words_dict = {
    "apple": ["Red or green fruit", "Keeps the doctor away", "Popular pie ingredient"],
    "banana": ["Yellow tropical fruit", "Monkeys love it", "Rich in potassium"],
    "cherry": ["Small red fruit", "Often on desserts", "Stone fruit"],
    "dates": ["Sweet Middle Eastern fruit", "Grows on palm trees", "Brown and wrinkly"],
    "egg plant": ["Purple vegetable", "Often used in lasagna", "Called aubergine in UK"],
    "figs": ["Sweet fruit", "Often dried", "Fig Newtons"],
    "grapes": ["Vine fruit", "Used to make wine", "Can be green or red"],
    "honey": ["Bee product", "Sweet and sticky", "Used in tea"],
    "ice cream": ["Frozen dessert", "Comes in many flavors", "Often in a cone"],
    "jack fruit": ["Large tropical fruit", "Can be a meat substitute", "Spiky outside"],
    "kiwi": ["Brown fuzzy fruit", "Green inside", "Tart and sweet"],
    "lemon": ["Yellow citrus fruit", "Very sour", "Used in lemonade"],
    "melon": ["Large, sweet fruit", "Includes cantaloupe", "Watery and refreshing"],
    "mango": ["Tropical stone fruit", "Sweet and juicy", "Orange flesh"],
    "nectar": ["Sweet liquid", "Produced by flowers", "Attracts bees"],
    "olive": ["Mediterranean fruit", "Used for oil", "Green or black"],
    "orange": ["Citrus fruit", "Juicy and sweet", "High in vitamin C"],
    "pear": ["Sweet, bell-shaped fruit", "Soft and juicy", "Often green"],
    "papaya": ["Tropical fruit", "Orange flesh", "Many black seeds"],
    "pepper": ["Spicy vegetable", "Used in cooking", "Can be green or red"],
    "pineapple": ["Tropical fruit", "Spiky and sweet", "Used in piña coladas"],
    "quince": ["Hard, yellow fruit", "Often made into jelly", "Not eaten raw"],
    "raisins": ["Dried grapes", "Often in cereals", "Sweet and chewy"],
    "rose": ["Flower with thorns", "Symbol of love", "Often red"],
    "strawberry": ["Red berry", "Sweet and juicy", "Has tiny seeds"],
    "tomato": ["Red fruit", "Used in salads", "Often mistaken as vegetable"],
    "umbrella": ["Rain protector", "Opens and closes", "Held by handle"],
    "plum": ["Purple or red fruit", "Sweet and juicy", "Stone fruit"],
    "watermelon": ["Large, green fruit", "Red flesh with seeds", "Very refreshing"],
    "zucchini": ["Green summer squash", "Often grilled", "Similar to cucumber"],
    "apricots": ["Small, orange fruit", "Sweet and tart", "Often dried"],
    "avocado": ["Green, creamy fruit", "Used in guacamole", "High in healthy fats"],
    "butterscotch": ["Sweet, buttery flavor", "Often in candies", "Golden color"],
    "vanila": ["Popular flavor", "Used in baking", "From orchid pods"],
    "chocolate": ["Sweet treat", "Made from cocoa", "Loved by many"],
    "river": ["Flowing water body", "Has banks", "Feeds into lakes"],
    "hills": ["Small elevations", "Lower than mountains", "Often green"],
    "mountains": ["Tall landforms", "Snow-capped peaks", "Great for hiking"],
    "fish": ["Aquatic animal", "Has fins", "Lives in water"],
    "animals": ["Living creatures", "Can be pets", "Various species"],
    "ocean": ["Large saltwater body", "Covers most of Earth", "Home to fish"],
    "sea": ["Smaller than ocean", "Salty water", "Connected to ocean"],
    "sky": ["Above us", "Blue and vast", "Clouds float in it"],
    "flower": ["Colorful plant part", "Blooms in spring", "Attracts bees"],
    "spaghetti": ["Long, thin pasta", "Often with sauce", "Italian cuisine"],
    "pasta": ["Italian staple", "Comes in shapes", "Made from wheat"],
    "pizza": ["Baked flatbread", "Topped with cheese", "Often has pepperoni"],
    "identity": ["Who you are", "Personal traits", "Sense of self"],
    "nationalism": ["Patriotic feeling", "Loyal to country", "Can be extreme"],
    "wired": ["Connected with wires", "Electronic devices", "Can be messy"],
    "ripens": ["Fruit matures", "Becomes sweeter", "Ready to eat"],
    "strands": ["Thin pieces", "Often of hair", "Many together"],
    "hair": ["Grows on head", "Can be styled", "Comes in colors"],
    "moustache": ["Facial hair", "Above upper lip", "Groomed or natural"],
    "nut": ["Hard-shelled fruit", "Often edible", "Includes almonds"],
    "dive": ["Jump into water", "Go underwater", "Swimming action"],
    "blink": ["Close eyes briefly", "Quick movement", "Involuntary action"],
    "whole": ["Complete, not part", "Full, entire", "Not broken"],
    "sculpture": ["Art in 3D", "Carved or molded", "Often in museums"],
    "culprit": ["One at fault", "Guilty party", "Blamed for crime"],
    "criminal": ["Lawbreaker", "Commits crimes", "Punished by law"],
    "friend": ["Close companion", "Trusted person", "Not a foe"],
    "befriend": ["Make a friend", "Form friendship", "Become close"],
    "life": ["Living existence", "Opposite of death", "Full of experiences"],
    "death": ["End of life", "Permanent cessation", "Final event"],
    "space": ["Universe expanse", "Outer cosmos", "Astronauts explore"],
    "universe": ["All of space", "Contains galaxies", "Infinitely vast"],
    "Afghanistan": ["Asian country", "Kabul capital", "War-torn history"],
    "Albania": ["Balkan nation", "Tirana capital", "Adriatic coast"],
    "Algeria": ["North Africa", "Algiers capital", "Largest African country"],
    "Andorra": ["Tiny country", "Between France, Spain", "Pyrenees mountains"],
    "Angola": ["Southern Africa", "Luanda capital", "Oil-rich nation"],
    "Antigua and Barbuda": ["Caribbean islands", "St. John's capital", "Tourist destination"],
    "Argentina": ["South American country", "Buenos Aires capital", "Famous for tango"],
    "Armenia": ["Caucasus region", "Yerevan capital", "Ancient culture"],
    "Australia": ["Island continent", "Canberra capital", "Known for outback"],
    "Austria": ["Central Europe", "Vienna capital", "Famous for Alps"],
    "Bahrain": ["Island nation", "Manama capital", "Middle East"],
    "Bangladesh": ["South Asia", "Dhaka capital", "Dense population"],
    "Barbados": ["Caribbean island", "Bridgetown capital", "Famous for beaches"],
    "Belarus": ["Eastern Europe", "Minsk capital", "Landlocked nation"],
    "Belgium": ["Western Europe", "Brussels capital", "Known for chocolate"],
    "Belize": ["Central America", "Belmopan capital", "Barrier reef"],
    "Bolivia": ["South America", "Sucre capital", "High-altitude nation"],
    "Bosnia and Herzegovina": ["Balkan country", "Sarajevo capital", "Historic conflict"],
    "Botswana": ["Southern Africa", "Gaborone capital", "Known for safaris"],
    "Brazil": ["South America", "Brasilia capital", "Amazon rainforest"],
    "Croatia": ["Balkan country", "Zagreb capital", "Adriatic coast"],
    "Cuba": ["Caribbean island", "Havana capital", "Communist state"],
    "Cyprus": ["Island nation", "Nicosia capital", "Mediterranean Sea"],
    "Czechia": ["Central Europe", "Prague capital", "Formerly Czechoslovakia"],
    "Chad": ["Central Africa", "N'Djamena capital", "Landlocked nation"],
    "Chile": ["South America", "Santiago capital", "Long coastal country"],
    "China": ["East Asia", "Beijing capital", "Most populous country"],
    "Colombia": ["South America", "Bogotá capital", "Known for coffee"],
    "Denmark": ["Northern Europe", "Copenhagen capital", "Part of Scandinavia"],
    "Djibouti": ["Horn of Africa", "Djibouti capital", "Strategic location"],
    "Dominica": ["Caribbean island", "Roseau capital", "Natural beauty"],
    "Ecuador": ["South America", "Quito capital", "Equator passes through"],
    "Egypt": ["North Africa", "Cairo capital", "Pyramids and Sphinx"],
    "El Salvador": ["Central America", "San Salvador capital", "Smallest mainland country"],
    "Fiji": ["Pacific island nation", "Suva capital", "Famous for resorts"],
    "Finland": ["Northern Europe", "Helsinki capital", "Land of thousand lakes"],
    "France": ["Western Europe", "Paris capital", "Eiffel Tower"],
    "Greece": ["Southern Europe", "Athens capital", "Ancient civilization"],
    "Germany": ["Central Europe", "Berlin capital", "Known for beer"],
    "Hawaii": ["US state", "Honolulu capital", "Islands in Pacific"],
    "Hungary": ["Central Europe", "Budapest capital", "Danube River"],
    "Iceland": ["North Atlantic", "Reykjavik capital", "Land of fire and ice"],
    "India": ["South Asia", "New Delhi capital", "Second most populous"],
    "Indonesia": ["Southeast Asia", "Jakarta capital", "Thousand islands"],
    "Iran": ["Middle East", "Tehran capital", "Persian culture"],
    "Iraq": ["Middle East", "Baghdad capital", "Tigris and Euphrates"],
    "Ireland": ["Island nation", "Dublin capital", "Emerald Isle"],
    "Israel": ["Middle East", "Jerusalem capital", "Holy Land"],
    "Italy": ["Southern Europe", "Rome capital", "Known for pasta"],
    "Jamaica": ["Caribbean island", "Kingston capital", "Reggae music"],
    "Japan": ["East Asia", "Tokyo capital", "Land of the rising sun"],
    "Jordan": ["Middle East", "Amman capital", "Petra ancient city"],
    "Kazakhstan": ["Central Asia", "Nur-Sultan capital", "Former Soviet republic"],
    "Kenya": ["East Africa", "Nairobi capital", "Famous for safaris"],
    "Korea": ["East Asia", "Seoul or Pyongyang", "North and South"],
    "Kuwait": ["Middle East", "Kuwait City capital", "Oil-rich nation"],
    "Kyrgyzstan": ["Central Asia", "Bishkek capital", "Mountainous country"],
    "Lithuania": ["Baltic state", "Vilnius capital", "Former Soviet republic"],
    "Luxembourg": ["Small European country", "Luxembourg City capital", "Rich European nation"],
    "Latvia": ["Baltic state", "Riga capital", "Former Soviet republic"],
    "Lebanon": ["Middle East", "Beirut capital", "Mediterranean coast"],
    "Libya": ["North Africa", "Tripoli capital", "Desert country"],
    "Madagascar": ["Island nation", "Antananarivo capital", "Unique wildlife"],
    "Malaysia": ["Southeast Asia", "Kuala Lumpur capital", "Peninsular and Borneo"],
    "Maldives": ["Island nation", "Malé capital", "Indian Ocean"],
    "Micronesia": ["Pacific islands", "Palikir capital", "Small island states"],
    "Mexico": ["North America", "Mexico City capital", "Known for tacos"],
    "Mongolia": ["East Asia", "Ulaanbaatar capital", "Genghis Khan"],
    "Morocco": ["North Africa", "Rabat capital", "Sahara desert"],
    "Nepal": ["South Asia", "Kathmandu capital", "Himalayan mountains"],
    "Netherlands": ["Western Europe", "Amsterdam capital", "Known for canals"],
    "New Zealand": ["Oceania", "Wellington capital", "Land of Kiwis"],
    "Nigeria": ["West Africa", "Abuja capital", "Most populous in Africa"],
    "Norway": ["Northern Europe", "Oslo capital", "Fjords and Vikings"],
    "Oman": ["Middle East", "Muscat capital", "Arabian Peninsula"],
    "Pakistan": ["South Asia", "Islamabad capital", "Indus Valley"],
    "Panama": ["Central America", "Panama City capital", "Famous canal"],
    "Papua New Guinea": ["Oceania", "Port Moresby capital", "Diverse cultures"],
    "Peru": ["South America", "Lima capital", "Machu Picchu"],
    "Philippines": ["Southeast Asia", "Manila capital", "Archipelago nation"],
    "Poland": ["Central Europe", "Warsaw capital", "Former communist state"],
    "Portugal": ["Southern Europe", "Lisbon capital", "Famous for port wine"],
    "Qatar": ["Middle East", "Doha capital", "Rich in natural gas"],
    "Romania": ["Eastern Europe", "Bucharest capital", "Transylvania region"],
    "Russia": ["Largest country", "Moscow capital", "Spans Europe and Asia"],
    "Congo": ["Central Africa", "Brazzaville or Kinshasa", "Two countries with similar names"],
    "Sudan": ["North Africa", "Khartoum capital", "Nile River"],
    "Sweden": ["Northern Europe", "Stockholm capital", "Known for ABBA"],
    "Switzerland": ["Central Europe", "Bern capital", "Famous for neutrality"],
    "Syria": ["Middle East", "Damascus capital", "Ongoing conflict"],
    "Serbia": ["Balkan nation", "Belgrade capital", "Former Yugoslavia"],
    "Slovenia": ["Central Europe", "Ljubljana capital", "Known for lakes"],
    "Somalia": ["Horn of Africa", "Mogadishu capital", "Pirate activity"],
    "Slovakia": ["Central Europe", "Bratislava capital", "Formerly Czechoslovakia"],
    "Spain": ["Southern Europe", "Madrid capital", "Known for flamenco"],
    "South Africa": ["Southern Africa", "Pretoria capital", "Diverse cultures"],
    "Sri Lanka": ["Island nation", "Colombo capital", "Indian Ocean"],
    "Tajikistan": ["Central Asia", "Dushanbe capital", "Mountainous terrain"],
    "Tanzania": ["East Africa", "Dodoma capital", "Serengeti and Kilimanjaro"],
    "Thailand": ["Southeast Asia", "Bangkok capital", "Known for temples"],
    "Uganda": ["East Africa", "Kampala capital", "Source of Nile"],
    "Ukraine": ["Eastern Europe", "Kyiv capital", "Former Soviet republic"],
    "Uruguay": ["South America", "Montevideo capital", "Small coastal country"],
    "Uzbekistan": ["Central Asia", "Tashkent capital", "Silk Road history"],
    "Venezuela": ["South America", "Caracas capital", "Oil-rich nation"],
    "Vietnam": ["Southeast Asia", "Hanoi capital", "Vietnam War"],
    "Washington DC": ["US capital", "White House", "Located in District of Columbia"],
    "Yemen": ["Middle East", "Sana'a capital", "Ongoing conflict"],
    "Zambia": ["Southern Africa", "Lusaka capital", "Victoria Falls"],
    "Zimbabwe": ["Southern Africa", "Harare capital", "Known for ruins"],
}
