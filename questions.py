# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:32:10 2022

@author: ASUS
"""
import random

# Easy - levels 1-3
# Medium - levels 4-6
# Hard - levels 7-19
# VeryHard - level 10
level = [(("What is the date setting of the original Call of Duty?", "World War II",
           "a. World War II   b. World War I   c. World War III   d. The Vietnam War",
           "'Call of Duty' is set in World War II, and players can approach the game from the perspective an American, British or Russian soldier."),
          ("What classic videogame did Tony Stark catch a member of S.H.I.L.D. playing in the first 'Avengers' movie?",
           "Galaga", "a. Galaxian   b. Galaga   c. Space Invaders   d. Asteroids",
           "While aboard the Helicarrier, Tony Stark hilariously calls out a SHIELD employee for playing Galaga, making it one of the most-memorable moments in 'the Avengers'."),
          ("A pickaxe is a basic, commonly-used tool in which videogame?", "Minecraft",
           "a. Golden Axe   b. Minecraft   c. Lego the Hobbit   d. League of Legends",
           "Pickaxes, the basic tool for mining in 'Minecraft', are perhaps the most-commonly used instruments in the game."),
          ("Characters in videogames who cannot be outrightly controlled by players are acronymed as what?", "NPCs",
           "a. WoWs   b. NPCs   c. MMORPGs   d. RPGs",
           "Non-playable characters (NPCs) are those that players cannot control, though their actions can be influenced.")),
         (("What is the name of the circular object that is used to collect Pokémon?", "Poke Ball",
           "a. Poke Go   b. Poke Ball   c. Poke Orb   d. Poke Egg",
           "Poké balls are used to used to catch and store Pokémon to be later traded or used in battle."), (
          "The word 'Pokémon' is generally understood to be a translation of which phrase?", "Pocket Monsters",
          "a. Pocket Monsters   b. Catch Them All   c. Never Quit   d. Lovable Monsters",
          "'Pokémon' is a stylized contraction of 'Pocket Monsters', which the series was originally called in Japan."),
          ("How many players can compete against each other simultaneously in a 'Fortnite Battle Royale'?", "100",
           "a. 50   b. 100   c. 150   d. 200",
           "Up to 100 players can compete in a Battle Royale, with the last man (or woman) standing being the ultimate victor."),
          ("What are the professions of Mario and his brother Luigi?", "Plumbers",
           "a. Garbage men   b. Dancers   c. Heroes   d. Plumbers",
           "Since the release of the original 'Mario Bros.' in 1983, it has been established that Mario (and Luigi) is an Italian-American plumber.")),
         (("Dr. Light is the creator of which classic videogame character?", "Mega Men",
           "a. Samus   b. Mega Man   c. Sonic   d. Balloon Fighter",
           "Mega Man was created by the fictional Dr. Light, who despite being a pacifist sees the need for force when necessary."),
          ("The Nintendo Game Boy utilized which type of display system?", "LCD",
           "a. Plasma   b. OLED   c. LCD   d. Projection",
           "As with most handheld videogames from the classic days, the Game Boy used a liquid-crystal display (LCD)."),
          ("Which item made Mario invincible in 'Super Mario Bros.'?", "Starman",
           "a. Mushroom   b. Fire Flower   c. Starman   d. Yoshi Egg",
           "Starman not only makes Mario invincible but also his touch lethal to enemies.")),
         (("What is the name of the first videogame in the 'Warcraft' series?", "Orcs and Humans",
           "a. Reign of Chaos   b. Tides of Darkness   c. The Burning Crusade   d. Orcs and Humans",
           "The first Warcraft was called 'Orcs & Humans', and various aspects of the game, such as its multiplayer functionality and real-time strategy play, helped revolutionize the videogame industry."),
          (
          "In 2018, which videogame company did actor Alfonso Ribeiro sue for unethically capitalizing off content he created?",
          "Epic Games", "a. Blizzard Entertainment   b. Ubisoft   c. Epic Games   d. Electronic Arts",
          "Alfonso Ribeiro, former costar of 'the Fresh Prince of Belair', filed a lawsuit against Epic Games, Fortnite's developers, over an emote dance that can be purchased in the game appropriately called 'Fresh'."),
          (
          "What is the only videogame franchise originating in the 1970's to have thus far generated over $1 billion in revenue?",
          "Space Invaders", "a. Galaxian   b. Pong   c. Space Invaders   d. Asteroids",
          "Originating in 1978, as of the beginning of 2019 the 'Space Invaders' franchise has generated almost $14 billion in revenue.")),
         (("Approximately how many (in millions) PlayStation 4s have been sold as of the beginning of 2019?", "100",
           "a. 10   b. 50   c. 100   d. 150",
           "In early 2019 Sony stated that it has sold over 91.6 million PS4's, as well as almost 900 million games for the console."),
          ("Which popular videogame creatures come from the Howling Abyss?", "Poros",
           "a. Poros   b. Koopas   c. Sims   d. Pokemon",
           "The lovable and transformative Poros from 'World of Warcraft' originate front the Howling Abyss in Freljord."),
          (
          "A computer opponent's ability to adaptively challenge a player is known as what?", "Artificial Intelligence",
          "a. MMORPG   b. Mindcraft   c. Artificial Intelligence   d. Cutting",
          "Since classic games like 'Space Invaders', 'Galaxian' and 'Pac-Man' successfully implemented artificial intelligence decades ago, it was become a stable in the videogame industry.")),
         (("Which famous entertainer composed music for 'Sonic 3'?", "Michael Jackson",
           "a. Michael Jackson   b. Prince   c. Kanye West   d. Paul McCartney",
           "Michael Jackson contributed some music to 'Sonic 3 & Knuckles' though went uncredited after abandoning the project."),
          ("Which videogame is generally considered to be the original third-person shooter?", "Wolfenstein 3D",
           "a. GoldenEye 007   b. Duke Nukem   c. Wolfenstein 3D   d. Doom",
           "'Wolfenstein 3D' is credited with being the original first-person shooter, though games using a similar point-of-view date as far back as 1973 with a program called 'Maze Wars' developed for students of NASA."),
          ("What is the name of the alien alliance who are the main antagonist in the first trilogy of 'Halo' games?",
           "The Covenant", "a. The Horde   b. The Covenant   c. The Chozo   d. The Poros",
           "The Covenant deem it the will of their gods that they destroy the human race.")),
         (("What are the name of the cartoon-like interludes that interrupt videogame play to narrate the story?",
           "Cutscenes", "a. Chronicles   b. Commercials   c. Action break   d. Cutscenes",
           "A cutscene or event scene is a non-interactive break from gameplay, with the term being coined by the creator of the graphic-adventure game 'Maniac Mansion'."),
          (
          "What is the name of the peripheral device that can be plugged into a Nintendo 64 controller to make it vibrate?",
          "Rumble Pak", "a. Vibratron   b. Game Link   c. Rumble Pak   d. CD-ROM",
          "Nintendo also released the Rumble Pak for a number of its handheld game systems."), (
          "What is the name of the last videogame console Sega released in the United States?", "Dreamcast",
          "a. Advanced Pico Beena   b. Dreamcast   c. 32x   d. Sega Saturn",
          "Though released almost 20 years ago in 1999, the Dreamcast was the last home console Sega brought to foreign markets.")),
         (("In what year was 'Fortnite' released?", "2017",
           "a. Grand Theft Auto V   b. Final Fantasy VII   c. Star Wars: Old Republic   d. Kingdom Hearts III",
           "'Fortnite' was released in 2017 and since then has become such a resounding success that it's been called 'a cultural phenomenon'."),
          ("What is the name of the star system in which the 'Star Fox' universe takes place?", "Lylat",
           "a. Krystal   b. Lylat   c. Corneria   d. Aparoid",
           "The fictional Lylat System consists of 12 planets, including Corneria."), (
          "Who provides the voice of Pikachu in the 2019 'Pokémon: Detective Pikachu' movie?", "Ryan Reynolds",
          "a. Bobcat Goldthwaite   b. Paul Rudd   c. Adam Sandler   d. Ryan Reynolds",
          "The live-action 'Detective Pikachu' is voiced by none other than Ryan Reynolds, who also provided the character's facial movements."),
          ("Besides Sonic, which other Sega character was a playable character in 'Super Smash Bros. 4'?", "Bayonetta",
           "a. Shinobi   b. Bayonetta   c. Knuckles   d. Gilius Thunderhead",
           "Bayonetta, the titular character from the 'Bayonetta' series of videogames, is a property of the Sega Corporation.")),
         (("Which videogame holds the record for having the highest budget ever to produce?", "Grand Theft Auto V",
           "a. Grand Theft Auto V   b. Final Fantasy VII   c. Star Wars: Old Republic   d. Kingdom Hearts III",
           "With an estimated budget of $256 million, 'Grand Theft Auto V' cost more to make than many major motion films."),
          ("Which iconic videogame character originated as a simple placeholder?", "Kirby",
           "a. Kirby   b. Yoshi   c. Pikachu   d. Link",
           "As can probably be ascertained by his simple appearance, Kirby is the one that was original intended to be a circular placeholder for another character."),
          ("In 2018, which famous rapper released an official music video heavily-inspired by 'Minecraft'?",
           "Kanye West", "a. Travis Scott   b. Kanye West   c. Tekashi 6ix9ine   d. Jay-Z",
           "Kanye West and Lil Pump's 2018 duet 'I Love It' featured caricatures of the artists based on the hit videogame 'Minecraft'.")),
         (("Which pop media icon was recently memorialized in 'World of Warcraft' in late 2018?", "Stan Lee",
           "a. Stan Lee   b. Aretha Franklin   c. Michael Jackson   d. Penny Marshall",
           "Comic-book visionary Stan Lee, who passed away in 2018, is now featured as a NPC in 'World of Warcraft'."),
          ("The PlayStation prototype was designed by Sony in collaboration with which company?", "Nintendo",
           "a. Napster   b. Blockbuster   c. Nintendo   d. NEC Electronics",
           "The PlayStation was originally a CD-ROM add-on for the Super Nintendo. Nintendo pulling out of the deal in 1991 prompted Sony to eventually produce it on their own."),
          ("What is the highest level a player can reach in 'Pac-Man'?", "256", "a. 128   b. 364   c. 256   d. 52",
           "A glitch in the code of Pac-Man makes passing the 256th level impossible.")), ]


class question(object):
    def __init__(self, N):
        self.N = N

    def questionByLevel(self, state):
        qNum = random.randint(0, len(level[state]) - 1)
        # return level[0][0]
        return level[state][qNum]
