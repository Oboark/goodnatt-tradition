"""
goodnatt-tradition

generates a sequence of wholesome emojis randomly,
no bias so all emojis are chosen randomly
"""

import random

def goodnatt(emojis, n_emojis):
    'Generates a sequence of n_emoji length with emojis list of emoji names'
    #Initialize the string list that we will be adding emojis to
    goodnatt_s = []

    #Add a random emoji to our string list for n_emojis number of iterations
    for i in range(n_emojis):
        goodnatt_s.append(random.choice(emojis))

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