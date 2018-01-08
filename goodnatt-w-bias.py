"""
goodnatt-tradition

generates a sequence of wholesome emojis randomly,
has bias so some emojis are used more than the others
"""

import random

def goodnatt(emojis, n_emojis):
    'Generates a sequence of n_emoji length with emojis list of emoji names'
    #Initialize the string list that we will be adding emojis to
    goodnatt_s = []

    #Add a random emoji to our string list for n_emojis number of iterations
    for i in range(n_emojis):
        #Select a random value between 0 and 1
        choice = random.uniform(0, 1)
        #Append a random emoji from the emojis list if choice is equal
        #to or lower than 0.8, this equates to an 80% chance of choosing a completely random
        #emoji
        if choice <= 0.8:
            goodnatt_s.append(random.choice(emojis))
        else:
            #In the other case, which is 20%, use our select emoji
            goodnatt_s.append("gay_pride_flag")
        #You can add different conditional statements to add even more
        #biased emojis (this can be a lil coding challenge for you)

    #Join every emoji with a :: and enclose the emojis in a : so that it will work on Discord
    return ':' + '::'.join(goodnatt_s) + ':'

#Default emoji list we feed to the function
emoji_list = [  
                "gay_pride_flag", "rainbow", "kiss_ww","couple_ww", "family_wwb", "family_wwbb", "family_wwg", "family_wwgb", 
                "family_wwgg", "sparkling_heart", "heart", "blue_heart", "purple_heart", "ok_woman", "star2",
                "hamburger", "peach", "shaved_ice", "unicorn", "bee", "dragon", "four_leaf_clover", "hibiscus", "maple_leaf",
                "lizard", "sunflower", "white_flower", "wilted_rose", "fallen_leaf", "cherry_blossom", "tulip", "blossom",
                "blossom", "cherry_blossom", "hibiscus", "sun_with_face", "two_hearts"
            ]

#Print our goodnatt string
print(goodnatt(emoji_list, 10))