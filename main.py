import random
import threading
import time


#problems

# - Some events break if given an invalid action such as a mispelled word (might be fixed)
# - Blocking is absolutely useless
# - Poison isn't being calculated on healing or

#fixed and/or added

# - Skeleton and/or mimic is sometimes repeating or overlapping
# - Health was being calculated correctly, I just put in a wrong operation
# - Can no longer heal over max health, fixed by giving another parameter to stats[] called stats["maxHealth"]
# - I put classes in a loop that repeats until you type a valid class
# - Items and a shop was added
# - Evasion chance added
# - Evasion and gold made thief not useless
# - QTE is now an option for minotaur boss (real PAIN to code)
# - Random loot has been added (real PAIN to code)
# - Poison


#mechanics waiting

# - Might add new game+ / harder or easier difficulties
# - Levels and/or experience
# - More enemies and/or bosses
# - Random loot based on enemy
# - Multiple enemy fights
# - trap room
# - Cerberus
# - Snakes
# - Dragon
# - Beholder
# - Gargoyles
# - Consumables
# - Earthquake
# - Floating skulls
# - Non-attacking enemy that rewards lucky hits(high evasion)
# - Giant rat
# - Death worm
# - Golems
# - werewolves
# - shadows, survive until you give up

print(r"""
___  ___   ________   ___        ________      ___        ___   ________  _______            __________  ___  ___   ________   _______    _______      
|\  \|\  \ |\   __  \ |\  \      |\  _____\    |\  \      |\  \ |\  _____\|\  ___ \         |\___   ___\|\  \|\  \ |\   __  \ |\  ___ \  |\  ___ \     
\ \  \\\  \\ \  \|\  \\ \  \     \ \  \__/     \ \  \     \ \  \\ \  \__/ \ \   __/|        \|___ \  \_|\ \  \\\  \\ \  \|\  \\ \   __/| \ \   __/|    
 \ \   __  \\ \   __  \\ \  \     \ \   __\     \ \  \     \ \  \\ \   __\ \ \  \_|/__           \ \  \  \ \   __  \\ \   _  _\\ \  \_|/__\ \  \_|/__  
  \ \  \ \  \\ \  \ \  \\ \  \____ \ \  \_|      \ \  \____ \ \  \\ \  \_|  \ \  \_|\ \           \ \  \  \ \  \ \  \\ \  \\  \|\ \  \_|\ \\ \  \_|\ \ 
   \ \__\ \__\\ \__\ \__\\ \_______\\ \__\        \ \_______\\ \__\\ \__\    \ \_______\           \ \__\  \ \__\ \__\\ \__\\ _\ \ \_______\\ \_______\
    \|__|\|__| \|__|\|__| \|_______| \|__|         \|_______| \|__| \|__|     \|_______|            \|__|   \|__|\|__| \|__|\|__| \|_______| \|_______|
                                                                                                                                                       """)

name = input("Enter your name: ")
age = input("Enter your age: ")

i = 0
classChoice = True

playerInputTreasure = ["","",""]

tutorial = r"""
───────────────────────────────
──────────▄▄▄▄▄▄▄▄▄▄▄──────────
─────▄▄▀▀▀▀──────────▀▀▄▄──────
───▄▀───────────────────▀▀▄────
──█────────────────────────█───
─█─────────────────────▄▀▀▀▀▀█▄
█▀────────────────────█────▄███
█─────────────────────█────▀███
█─────▄▀▀██▀▄─────────█───────█
█────█──████─█─────────▀▄▄▄▄▄█─
█────█──▀██▀─█───────────────█─
█────█───────█──────────────▄▀─
█────▀▄─────▄▀──▄▄▄▄▄▄▄▄▄───█──
█──────▀▀▀▀▀────█─█─█─█─█──▄▀──
─█──────────────▀▄█▄█▄█▀──▄▀───
──█──────────────────────▄▀────
───▀▀▀▄──────────▄▄▄▄▄▄▀▀──────
────▄▀─────────▀▀──▄▀──────────
──▄▀───────────────█───────────
─▄▀────────────────█──▄▀▀▀█▀▀▄─
─█────█──█▀▀▀▄─────█▀▀────█──█─
▄█────▀▀▀────█─────█────▀▀───█─
█▀▄──────────█─────█▄────────█─
█──▀▀▀▀▀█▄▄▄▄▀─────▀█▀▀▀▄▄▄▄▀──
█───────────────────▀▄─────────

        You are an adventurer. Completing quests, slaying monsters, and drinking the night away commandeer most of your days.
    Tomorrow you will embark on a quest to explore a new dungeon. You are respected at the guild and as such you were the first
    person to be chosen for this daunting task. Because this dungeon has only just been discovered, it has not been mapped out
    and on one knows what lies within its deepest depths. Like most dungeons it will have minions and a final boss which when
    defeated, will signify your quest completion. Your dungeon delving will require choices. Treasures may be locked or worse.
    Enemies are different where when fighting, you can either attack, block or heal. Blocking reduces damage but takes up your
    turn to attack. Healing may be vital but some enemies aren't just going to stand there while you chug a potion. With that
    you are ready to start your adventure. Good luck......you'll most likely need it.
"""


start = """
______________$$$$$$$$$$____________________
_____________$$__$_____$$$$$________________
_____________$$_$$__$$____$$$$$$$$__________
____________$$_$$__$$$$$________$$$_________
___________$$_$$__$$__$$_$$$__$$__$$________
___________$$_$$__$__$$__$$$$$$$$__$$_______
____________$$$$$_$$_$$$_$$$$$$$$_$$$_______
_____________$$$$$$$$$$$$$_$$___$_$$$$______
________________$$_$$$______$$$$$_$$$$______
_________________$$$$_______$$$$$___$$$_____
___________________________$$_$$____$$$$____
___________________________$$_$$____$$$$$___
__________________________$$$$$_____$$$$$$__
_________________________$__$$_______$$$$$__
________________________$$$_$$________$$$$$_
________________________$$$___________$$$$$_
_________________$$$$___$$____________$$$$$$
__$$$$$$$$____$$$$$$$$$$_$____________$$$_$$
_$$$$$$$$$$$$$$$______$$$$$$$___$$____$$_$$$
$$________$$$$__________$_$$$___$$$_____$$$$
$$______$$$_____________$$$$$$$$$$$$$$$$$_$$
$$______$$_______________$$_$$$$$$$$$$$$$$$_
$$_____$_$$$$$__________$$$_$$$$$$$$$$$$$$$_
$$___$$$__$$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$__
$$_$$$$_____$$$$$$$$$$$$________$$$$$$__$___
$$$$$$$$$$$$$$_________$$$$$______$$$$$$$___
$$$$_$$$$$______________$$$$$$$$$$$$$$$$____
$$__$$$$_____$$___________$$$$$$$$$$$$$_____
$$_$$$$$$$$$$$$____________$$$$$$$$$$_______
$$_$$$$$$$hg$$$____$$$$$$$$__$$$____________
$$$$__$$$$$$$$$$$$$$$$$$$$$$$$______________
$$_________$$$$$$$$$$$$$$$__________________

        After readying your belongings, you head out. The dungeon isn't too far but it's not exactly close so you steel yourself
    and say a small goodbye which you think could be your last. You walk along the road and veer off into the woods until you
    reach the aforementioned dungeon. It's small by most accounts but that could be misleading as it could go underground or have
    monsters packed to every corner like clown car. It's getting late however so you setup camp outside and rest for the night.
"""

events = [
"""
    While you were asleep a slime decided your tent was a prime source of delicious cloth and had eaten most of it before you were
woken up the the sound of sloshing.
""", #  - 0
"""                                                            
The slime was easy to kill but don't get cocky......it was literally just a slime.""", #  - 1
"""
    Hearing light footsteps coming closer you ready your weapon. Out of the shadows walks a small green creature. It is no more than a
few feet tall being at eye level to your waist. It is holding a small shortsword and snarling at you.
""", #  - 2
"""
The goblin was pretty easy but there was only one this time. You got lucky; goblins usually travel in packs. Be careful.""", #  - 3
"You enter a room where there is nothing but empty space and a chest at the end of the room.", #  - 4
"""
    You decided to leave it alone. It could be empty or it could be a trap. There are bound to be more oportunities to satiate
your greed anyhow so don't let your trip end here.
""", #  - 5
"""
    Against your 100% BETTER judgement, you decide to open a random chest, in a random room, in a monster infested dungeon.
    Congratulations! You are now missing a limb! You managed to find a mimic! A horrifying grotesque monster that disguises itself
    as a chest to lure in greedy prey. Have fun killing something covered in metal.
""", #  - 6
"""
    Mimics are quite rare but somehow you managed to find one and kill it. It may have almost taken a couple limbs off and scared
you half to death but who knows, maybe the experience is worth it......hopefully.
""", #  - 7
r"""
    .-.    
   (o.o)   
    |=|    
   __|__   
 //.=|=.\\ 
// .=|=. \\
\\ .=|=. //
 \\(_=_)// 
  (:| |:)  
   || ||   
   () ()   
   || ||   
   || ||   
  ==' '==  
    The rattling of bones fills the corridor as a skeleton walks towards you. It notices you.....you think. You're really unsure as the
skeleton have eyes but it raises its scimitar and round shield and grinds its teeth in your direction.
""", #  - 8
"""
    Skeletons are a pretty usual occurance in dungeons but that doesn't make killing them any easier. They don't feel emotions or
pain and you have to destroy the skull to kill them completely.You better hope you don't find one with intelligence or actual
combat prowess.
""", #  - 9
r"""
                                            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                    
                                          ▓▓▒▒░░░░░░░░▒▒▒▒▓▓▓▓                                
                                        ▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒                              
                                      ▓▓▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒░░                            
                                      ▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░                          
                                      ▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓                          
                                      ▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓                          
                                    ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒                        
                                    ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░██░░▒▒▒▒                        
                                    ▒▒▒▒░░░░░░░░░░██░░░░░░░░░░██▓▓▒▒▒▒                        
                                    ▒▒▒▒▒▒░░░░░░▒▒██  ░░░░░░  ████▓▓▓▓                        
                                    ▒▒▒▒▒▒░░░░░░██████░░░░░░████▓▓████                        
                                    ▒▒▒▒▒▒░░░░░░████████░░░░████░░████                        
                                    ▒▒▒▒░░░░░░░░████████░░░░░░██░░░░▒▒                        
                                  ▓▓▒▒▒▒░░░░░░░░████████░░░░░░░░░░████▓▓                      
                                  ▒▒▒▒░░░░░░░░░░░░████░░░░██▓▓▓▓▓▓████▒▒                      
                                  ▒▒▒▒░░░░░░░░░░░░▓▓▓▓░░░░████████████▓▓                      
                                ▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░██████▓▓▓▓▓▓████                      
                                ▒▒▒▒░░░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓██▓▓                        
                              ▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓██▓▓                          
                            ░░▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░████▓▓▓▓██▓▓░░                          
                          ▓▓▒▒▒▒░░  ▓▓▓▓▓▓▓▓██░░░░░░████▓▓▓▓██▓▓                              
                          ▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒████▓▓▓▓████                              
                          ▒▒▒▒░░░░░░░░░░░░░░░░░░  ████▓▓▓▓▓▓████                              
                        ▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░██████▓▓▓▓██████▓▓                            
                        ▓▓▒▒░░░░░░░░░░░░░░░░░░░░██████▓▓▓▓▓▓██░░▓▓                            
                      ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░██████▓▓▓▓▓▓██░░▒▒▒▒▒▒▒▒                      
                    ▓▓▒▒▒▒░░░░░░██░░░░░░░░░░░░██████████▓▓▓▓▓▓████░░░░░░▓▓                    
                    ▒▒▒▒░░░░░░▓▓▓▓░░░░░░░░░░░░██████████████▓▓▓▓██▓▓▓▓░░░░▒▒                  
                    ▒▒▒▒░░░░░░▓▓  ░░░░░░░░░░░░████████████████▓▓▓▓████░░░░▓▓                  
              ▒▒▒▒▒▒▒▒░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░████████████████░░░░░░░░▓▓                
              ▒▒▒▒░░░░░░░░░░░░▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░████  ░░░░░░░░░░░░██              
            ▒▒▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓              
      ▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░  ▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░██▓▓▓▓▓▓▓▓        
    ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██▓▓▒▒░░░░░░▓▓▓▓    
  ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓  
  ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
  ▒▒░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓
  ▓▓░░░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓  
      ██████▓▓░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
            ░░▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒      
                        ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                
                            ▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓                    
                                    ██░░░░░░░░░░░░░░░░░░░░░░████████                          
                                    ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░                          
    As you walk allow the lengthy hallway you notice the walls are covered in a thick layer of what looks like mucus. You'd find out
for sure but no sane person would bring a hand near the substance. While pondering over what could have left such an obscure substance
the universe answers for you as what can only be decribed as an abomination of a creature squelches its way towards you. You'd throw
up but the monster is about to touch you so that'll have to wait.
""", #  - 10
"""
    The abomination is dead but what has transpired will haunt you at night. Making it through that was no easy feat and you feel as
though you are losing sanity by the second but on the bright side, no other monster will every be able to hurt you the way that
thing did.
""", #  - 11
"You found a dead end, good job. Have fun backtracking a dimly lit, monster infested labyrinth :) "
".",# - 12
r"""
              ,,))))))));,
           __)))))))))))))),
\|/       -\(((((''''((((((((.
-*-==//////((''  .     `)))))),
/|\      ))| o    ;-.    '(((((                                  ,(,
         ( `|    /  )    ;))))'                               ,_))^;(~
            |   |   |   ,))((((_     _____------~~~-.        %,;(;(>';'~
            o_);   ;    )))(((` ~---~  `::           \      %%~~)(v;(`('~
                  ;    ''''````         `:       `:::|\,__,%%    );`'; ~
                 |   _                )     /      `:|`----'     `-'
           ______/\/~    |                 /        /
         /~;;.____/;;'  /          ___--,-(   `;;;/
        / //  _;______;'------~~~~~    /;;/\    /
       //  | |                        / ;   \;;,\
      (<_  | ;                      /',/-----'  _>
       \_| ||_                     //~;~~~~~~~~~
           `\_|                   (,~~  -Tua Xiong
                                   \~\
                                    ~~
    You stop walking abrubtly as you see the floor is coated with a layer of sticky thread. You know what's coming. You really really
wish you didn't but you do. You try your best to brace yourself for the mental onslaught of fear you are about to face fighting this
creature. You think hell spawn is a better term but it doesn't matter because even if it was called a fluffy rainbow unicorn you
still wouldn't want to fight it.

""", #  - 13
"""It died a long time ago but your fears persisted so you ended up stabbing it another 67 times just to make sure it was dead. You
almost wished there were more spiders because killing them felt like a gift to humanity but that thought didn't last long because
then you would have to fight them again.
""", #  - 14
"You delve further into the dungeon", #  - 15
"""
    As you continue down the hall a shady figure is seen standing in your way. He turns but his face is nearly covered and he
speaks in a low voice, "You seem to be in need of some things, I've got what you need.....for a price.
""", #  - 16
"""
    Maniacal laughter fills the halls as a twitching fellow walks towards you. He looks like a mage.
""", #  - 17
"""The maniac is dead but his laughter still haunts you. You'll hear that in your dreams. *Shiver*.
""", #  - 18
"""
    You come upon a massive door the size of a house. As you approach they rumble open shaking the entire dungeon.
You know that it may not be the best idea to go ahead but that is your whole reason for being here. You enter the door.
""", #  - 19
"""
    Through the door is a large circular room made of marble and stone with an enormous chair at the other end.
Sitting in the chair is a minotaur. It tilts its head up from the ground and stares you down with its red piercing eyes.
It will most likely attack very slowly giving you ample time to attack or heal multiple times. This however means that
when the time comes, blocking may be your only chance for survival. You're in for one hell of a fight with this thing.
""", #  - 20
"You've done it! It seemed impossible for one lone adventurer to do but you did. Congratulations! Go home and enjoy the spoils.", #  - 21
"""
    After opening a door that has seen better days, you stumble upon a room with a small water fountain in the middle. There
is a lever next to the fountain. Pulling it required quite a bit of force but after you did water flowed freely out of the
fountain. You take a long needed drink and rest.
""", #  - 22
"""
    Through the door is a large circular room made of marble and stone with an enormous chair at the other end.
Sitting in the chair is a minotaur. It tilts its head up from the ground and stares you down with its red piercing eyes.
It will most likely attack very slowly giving you ample time to attack or heal multiple times. When it comes time for
that thing to attack, you better be ready to take action quickly. You're in for one hell of a fight with this thing.

"""
    , #  - 23
"You know, one goblin isn't really a formidable opponent, but 3! Well. Let's just see how this goes...", # - 24
"""
    You open a door into a bigger room. Lumbering around the room seems to be a troll. They are well known. Really
hard to take down but ooga booga intelligence. As you are pondering what to do it turns around and notices you. It
scratches its head for a second and then shrugs. You feel a little insulted considering its intelligence.
""", # - 25
"""With and ending strike the hulking beast is taken down. It took a solid amount of effort but it was a large and
stationary target so beggars can't be choosers.
""", # - 26
"""
    Zombies are very misunderstood. Not in the flesh-eating part of course but many of them are vampire minions; they
are mindless and blood-thirsty. Speaking of which, here comes one now. Isn't it beautiful with its fangs and decaying flesh?
No? Why don't you test it against your weapon then.
""", # - 27
"That was gross but at least it's dead. You may need to clean your sword though, really.", # - 28
"""
    While taking a leak you happened to look up only to be met with large glowing red eyes and an unholy screech. You'd
be afraid but that will have to wait until after you are done. Just pee on it if it really can't wait.
""", # - 29
"""Finally one of your swings knocks the bat out of the air and you finish it off. It was more annoying than intense to fight
as it was harder to hit than a fly and had the agility of a bird. It's dead but your exhausted.
""" # - 30
]

#Enemies

slime = {
    "Health" : 10,
    "Attack" : 5,
    "Defence" : 1,
    "mEvasion" : [0]
    }
goblin = {
    "Health" : 20,
    "Attack" : 10,
    "Defence" : 1.5,
    "mEvasion" : [1]
    }
skeleton = {
    "Health" : 40,
    "Attack" : 15,
    "Defence" : 1.5,
    "mEvasion" : [1, 2]
    }
abomination = {
    "Health" : 50,
    "Attack" : 25,
    "Defence" : 2,
    "mEvasion" : [0]
    }
spider = {
    "Health" : 40,
    "Attack" : 20,
    "Defence" : 2,
    "mEvasion" : [1, 2, 3]
    }
mimic = {
    "Health" : 30,
    "Attack" : 20,
    "Defence" : 4,
    "mEvasion" : [1]
    }
maniac = {
    "Health" : 30,
    "Attack" : 40,
    "Defence" : 2,
    "mEvasion" : [1, 2]
    }
troll = {
    "Health" : 70,
    "Attack" : 20,
    "Defence" : 3,
    "mEvasion" : [0]
    }
zombie = {
    "Health" : 80,
    "Attack" : 10,
    "Defence" : 1,
    "mEvasion" : [1, 2]
    }
vampBat = {
    "Health" : 30,
    "Attack" : 10,
    "Defence" : 1,
    "mEvasion" : [1, 2, 3, 4, 5]
    }
giantRat = {
    "Health" : 30,
    "Attack" : 10,
    "Defence" : 1,
    "mEvasion" : [1, 2]
    }
minotaurBoss = {
    "Health" : 100,
    "Attack" : 100,
    "Defence" : 3

    }


loot = { # - added reg. potion, speed boots, and hermes' boots to loot ; (for evasion, use [-1] to use last item)
    "Basic weapon" : 5, # - 10% chance
    "Advanced weapon" : 10, # - 5% chance
    "Legendary weapon" : 20, # - 1% chance
    "Max potion" : 20, # - 5% chance
    "Basic armor" : 0.5, # - 10% chance
    "Advanced armor" : 0.75, # - 5% chance
    "Legendary armor" : 1, # - 1% chance
    }



# Classes
while classChoice == True:
    playerClass = input("Who would you like to be?: Warrior, Thief, or Mage? : ")
    if playerClass.lower() == "warrior":
        stats = {
            "Health" : 100,
            "Attack" : 20,
            "Defence" : 3.5,
            "maxHealth" : 100,
            "potions" : 4,
            "gold" : 50,
            "Evasion" : [1]
            }
        classChoice = False
    elif playerClass.lower() ==  "thief":
        stats = {
            "Health" : 80,
            "Attack" : 30,
            "Defence" : 2.5,
            "maxHealth" : 80,
            "potions" : 5,
            "gold" : 200,
            "Evasion" : [1, 2, 3]
            }
        classChoice = False
    elif playerClass.lower() == "mage":
        stats = {
            "Health" : 70,
            "Attack" : 40,
            "Defence" : 2,
            "maxHealth" : 70,
            "potions" : 6,
            "gold" : 100,
            "Evasion" : [1, 2]
            }
        classChoice = False
    else:
        print ("You were literally given three choices and you chose none of them, try again.")
        continue

def looting():
    lootChance = random.randint(1, 10)
    if lootChance <= 5:

        lootChance2 = random.randint(1, 3)

        if lootChance2 == 1:
            print ("Your found a basic weapon! Your attack has been increased by 5!")
            stats["Attack"] += loot["Basic weapon"]
            print ("Your attack is now " + str(int(stats["Attack"])) + "!")
        elif lootChance2 == 2:
            print ("Your found basic armor! Your defence has been increased by 0.5!")
            stats["Defence"] += loot["Basic armor"]
            print ("Your defence is now " + str(stats["Defence"]) + "!")
        elif lootChance2 == 3:
            print ("You found a health potion!")
            stats["potions"] += 1
            print ("You now have " + str(int(stats["potions"])) + " potions!")

    lootChance3 = random.randint(1, 100)
    ev = stats["Evasion"][-1] + 1

    if lootChance3 == 1:
        print ("WOW, you found a legendary weapon! Your attack has been incresed by 20!")
        stats["Attack"] += loot["Legendary weapon"]
        print ("Your attack is now " + str(int(stats["Attack"])) + "!")
    elif lootChance3 <= 6 and lootChance3 != 1:
        print ("Nice, your found an advanced weapon! Your attack has been increased by 10!")
        stats["Attack"] += loot["Advanced weapon"]
        print ("Your attack is now " + str(int(stats["Attack"])) + "!")
    elif lootChance3 == 100:
        print ("WOW, you found a legendary armor! Your defence has been incresed by 1!")
        stats["Defence"] += loot["Legendary armor"]
        print ("Your defence is now " + str(stats["defence"]) + "!")
    elif lootChance3 >= 94 and lootChance3 != 100:
        print ("Nice, your found advanced armor! Your defence has been increased by 0.75!")
        stats["Defence"] += loot["Advanced armor"]
        print ("Your defence is now " + str(stats["Defence"]) + "!")
    elif lootChance3 > 6 and lootChance3 < 12:
        print ("You found a max potion!")
        stats["maxHealth"] += 20
        print ("Your max health is now " + str(int(stats["maxHealth"])) + "!")
    elif lootChance3 < 94 and lootChance3 > 88:
        print ("You found speed boots! Your evasion chance has risen by 10%!")
        stats["Evasion"].append(ev)
    elif lootChance3 == 88:
        stats["Evasion"].append(ev)
        stats["Evasion"].append(ev)
        print ("WOW, you found Hermes' boots! Your evasion chance has risen by 20%!")
    else:
        print ("You found no more loot.")

#monster funtions



def attackEvent(event1, event2, monster):
    print (event1)
    playerInput = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    res = 0
    pCount = 0
    isPoisoned = False
    while monster["Health"] > 0:
        evasionChance = random.randint(1, 10)
        evasionChanceM = random.randint(1, 10)
        playerInput[0] = input("Would you like to attack(a), block(b) or heal(h)? : ")
        playerInput[0] = playerInput[0].lower()
        if playerInput[0] == "a":
            print ("You attack the monster with all your might.")
            if evasionChanceM not in monster["mEvasion"]:
                monster["Health"] -= int(stats["Attack"] / monster["Defence"])
                print ("You deal " + str(int(stats["Attack"] / monster["Defence"])) + " damage to the monster")
                if monster["Health"] < 0:
                    monster["Health"] = 0
                print ("The monster has " + str(int(monster["Health"])) + " health left.")

            elif evasionChanceM in monster["mEvasion"]:
                print ("You missed!")

            if monster["Health"] > 0 and evasionChance in stats["Evasion"] and monster != spider:
                print ("The monster attacks you!")
                print ("The monster missed!")

            elif monster["Health"] > 0 and evasionChance not in stats["Evasion"]:
                stats["Health"] -= int(monster["Attack"] / stats["Defence"])
                print ("The monster attacks you!")
                print ("The monster deals " + str(int(monster["Attack"] / stats["Defence"])) + " damage to you!")
                print ("Your current health is " + str(int(stats["Health"])))
                if stats["Health"] <= 0:
                    print ("You died!")
                    break

            elif monster["Health"] > 0 and monster == spider and evasionChance in stats["Evasion"]:
                stats["Health"] -= int(monster["Attack"] / stats["Defence"])
                print ("The monster attacks you!")
                print ("The monster deals " + str(int(monster["Attack"] / stats["Defence"])) + " damage to you!")
                print ("Your current health is " + str(int(stats["Health"])))
                if stats["Health"] <= 0:
                    print ("You died!")
                    break

            if monster == spider and isPoisoned != True:
                poisonChance = random.randint(1, 5)
                if poisonChance == 5:
                    isPoisoned = True
                    pCount = 1
                    print ("You are poisoned!")
                    stats["Health"] -= 5
                    print ("You took 5 poison damage!")
                    print ("Your current health is " + str(int(stats["Health"])))
                    continue
            if isPoisoned == True and pCount < 5:
                stats["Health"] -= 5
                pCount += 1
                print ("You took 5 poison damage!")
                print ("Your current health is " + str(int(stats["Health"])))
            elif isPoisoned == True and pCount >= 5:
                isPoisoned = False
                pCount = 0

            if monster == troll and troll["Health"] > 0:
                print ("The troll is regenerating!")
                print ("The troll healed for 5 health!")
                troll["Health"] += 5




        elif playerInput[0].lower() == "b":
            playerInput.remove("b")
            damage = int((monster["Attack"] - stats["Defence"]) * .2)
            stats["Health"] -= damage
            print ("Your brace yourself for the incoming attack.")
            print ("The monster did " + str(damage) + " damage to you!")
            print ("Your current health is " + str(int(stats["Health"])))
            if stats["Health"] <= 0:
                print ("You died!")
                break

        elif playerInput[0] == "h":
            playerInput.remove("h")
            if stats["potions"] > 0 and monster != maniac:
                stats["potions"] -= 1
                stats["Health"] += 30
                if stats["Health"] > stats["maxHealth"]:
                    stats["Health"] = stats["maxHealth"]
                print ("You healed for 30 hp")
                print ("Your current health is " + str(int(stats["Health"])))
                print ("You have " + str(stats["potions"]) + " potions left.")
                if evasionChance in stats["Evasion"]:
                    print ("The monster attacks you!")
                    print ("The monster missed!")
                    continue

                elif evasionChance not in stats["Evasion"]:
                    stats["Health"] -= int(monster["Attack"] / stats["Defence"])
                    print ("The monster did " + str(int(monster["Attack"] / stats["Defence"])) + " damage to you!")
                    print ("Your current health is " + str(int(stats["Health"])))
                    continue

            elif stats["potions"] > 0 and monster == maniac:
                print ("You tried to heal but your oppenent is a lunatic and slapped the potion out of your hand!")
                print ("They also poked you in the eye! Well that wasn't very nice.")
                stats["Health"] -= int(monster["Attack"] / stats["Defence"])
                print ("The monster did " + str(int(monster["Attack"] / stats["Defence"])) + " damage to you!")
                print ("Your current health is " + str(int(stats["Health"])))
                continue

            elif stats["potions"] == 0:
                print ("You have no more potions!")

        else:
            print ("That is not a valid action!")
            continue

            if stats["Health"] <= 0:
                print(r"""
 ███████████████████████████  
 ███████▀▀▀░░░░░░░▀▀▀███████  
 ████▀░░░░░░░░░░░░░░░░░▀████  
 ███│░░░░░░░░░░░░░░░░░░░│███  
 ██▌│░░░░░░░░░░░░░░░░░░░│▐██  
 ██░└┐░░░░░░░░░░░░░░░░░┌┘░██  
 ██░░└┐░░░░░░░░░░░░░░░┌┘░░██  
 ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██  
 ██▌░│██████▌░░░▐██████│░▐██  
 ███░│▐███▀▀░░▄░░▀▀███▌│░███  
 ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██  
 ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██  
 ████▄─┘██▌░░░░░░░▐██└─▄████  
 █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████  
 ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████  
 █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████  
 ███████▄░░░░░░░░░░░▄███████  
 ██████████▄▄▄▄▄▄▄██████████  
 ███████████████████████████
                You died!""")
                break

        if monster["Health"] <= 0 and monster != zombie:
            del playerInput [:]
            print ("""
 ███████████████████████████  
 ███████▀▀▀░░░░░░░▀▀▀███████  
 ████▀░░░░░░░░░░░░░░░░░▀████  
 ███│░░░░░░░░░░░░░░░░░░░│███  
 ██▌│░░░░░░░░░░░░░░░░░░░│▐██  
 ██░└┐░░░░░░░░░░░░░░░░░┌┘░██  
 ██░░└┐░░░░░░░░░░░░░░░┌┘░░██  
 ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██  
 ██▌░│██████▌░░░▐██████│░▐██  
 ███░│▐███▀▀░░▄░░▀▀███▌│░███  
 ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██  
 ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██  
 ████▄─┘██▌░░░░░░░▐██└─▄████  
 █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████  
 ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████  
 █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████  
 ███████▄░░░░░░░░░░░▄███████  
 ██████████▄▄▄▄▄▄▄██████████  
 ███████████████████████████
You killed the monster!""")
            randomGold = random.randint(20, 60)
            print ("The monster had " + str(randomGold) + " gold!")
            stats["gold"] += randomGold
            looting()
        elif monster["Health"] <= 0 and monster == zombie:
            res += 1
            if res > 1:
                break
            else:
                print ("The zombie resurrected!")
                monster["Health"] = 80
                continue

            print ("Your current health is " + str(int(stats["Health"])))
            print(event2)
            print (events[15])
            break















def mimicAttack():
    print (events[6])
    playerInput = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    stats["Health"] /= 2
    print ("Your current health is " + str(stats["Health"]))
    while mimic["Health"] > 0:
        evasionChance = random.randint(1, 10)
        playerInput[0] = input("Would you like to attack, block or heal? : ")
        playerInput[0] = playerInput[0].lower()
        if playerInput[0] == "a":
            mimic["Health"] -= int(stats["Attack"] / mimic["Defence"])
            playerInput.remove("a")
            print ("You attack the monster with all your might.")
            print ("You deal " + str(int(stats["Attack"] / mimic["Defence"])) + " damage to the monster")
            print ("The monster has " + str(int(mimic["Health"])) + " health left.")
            if mimic["Health"] > 0 and evasionChance in stats["Evasion"]:
                print ("The monster attacks you!")
                print ("The monster missed!")
                continue

            elif mimic["Health"] > 0 and evasionChance not in stats["Evasion"]:
                stats["Health"] -= int(mimic["Attack"] / stats["Defence"])
                print ("The monster attacks you!")
                print ("The monster deals " + str(int(mimic["Attack"] / stats["Defence"])) + " damage to you!")
                print ("Your current health is " + str(int(stats["Health"])))
                if stats["Health"] <= 0:
                    print ("You died!")
                    break

        elif playerInput[0] == "b":
            playerInput.remove("b")
            damage = int((mimic["Attack"] - stats["Defence"]) * .2)
            stats["Health"] -= damage
            print ("Your brace yourself for the incoming attack.")
            print ("The monster did " + str(damage) + " damage to you!")
            print ("Your current health is " + str(int(stats["Health"])))
            if stats["Health"] <= 0:
                print ("You died!")
                break

        elif playerInput[0] == "h":
            playerInput.remove("h")
            if stats["potions"] > 0:
                stats["potions"] -= 1
                stats["Health"] += 30
                if stats["Health"] > stats["maxHealth"]:
                    stats["Health"] = stats["maxHealth"]
                print ("You healed for 30 hp")
                print ("Your current health is " + str(int(stats["Health"])))
                print ("You have " + str(stats["potions"]) + " potions left.")
                if evasionChance in stats["Evasion"]:
                    print ("The monster attacks you!")
                    print ("The monster missed!")
                    continue

                elif evasionChance not in stats["Evasion"]:
                    stats["Health"] -= int(mimic["Attack"] / stats["Defence"])
                    print ("The monster did " + str(int(mimic["Attack"] / stats["Defence"])) + " damage to you!")
                    print ("Your current health is " + str(int(stats["Health"])))
                    continue
            else:
                print ("You have no more potions!")

        else:
            print ("That is not a valid action!")
            continue

        if mimic["Health"] <= 0:
            playerInput *= 0
            print ("You killed the mimic!")
            print ("The mimic had 300 gold!")
            stats["gold"] += 300
            lootChance = random.randint(1, 10)
            if lootChance <=5:

                lootChance2 = random.randint(1, 3)

                if lootChance2 == 1:
                    print ("Your found a basic weapon! Your attack has been increased by 5!")
                    stats["Attack"] += loot["Basic weapon"]
                    print ("Your attack is now " + str(int(stats["Attack"])) + "!")
                elif lootChance2 == 2:
                    print ("Your found basic armor! Your defence has been increased by 0.5!")
                    stats["Defence"] += loot["Basic armor"]
                    print ("Your defence is now " + str(int(stats["Defence"])) + "!")
                elif lootChance2 == 3:
                    print ("You found a health potion!")
                    stats["potions"] += 1
                    print ("You now have " + str(int(stats["potions"])) + " potion(s)!")

                lootChance3 = random.randint(1, 100)
                ev = stats["Evasion"][-1] + 1

                if lootChance3 <= 5:
                    print ("WOW, you found a legendary weapon! Your attack has been incresed by 20!")
                    stats["Attack"] += loot["Legendary weapon"]
                    print ("Your attack is now " + str(int(stats["Attack"])) + "!")
                elif lootChance3 >= 6 and lootChance3 <= 15:
                    print ("Nice, your found an advanced weapon! Your attack has been increased by 10!")
                    stats["Attack"] += loot["Advanced weapon"]
                    print ("Your attack is now " + str(int(stats["Attack"])) + "!")
                elif lootChance3 >= 96:
                    print ("WOW, you found a legendary armor! Your defence has been incresed by 1!")
                    stats["Defence"] += loot["Legendary armor"]
                    print ("Your defence is now " + str(int(stats["Defence"])) + "!")
                elif lootChance3 <=95 and lootChance3 >=86:
                    print ("Nice, your found advanced armor! Your defence has been increased by 0.75!")
                    stats["Defence"] += loot["Advanced armor"]
                    print ("Your defence is now " + str(int(stats["Defence"])) + "!")
                elif lootChance3 >= 16 and lootChance3 <= 25:
                    print ("You found a max potion!")
                    stats["maxHealth"] += 20
                    print ("Your max health is now " + str(int(stats["maxHealth"])) + "!")
                elif lootChance3 <= 85 and lootChance3 >= 76:
                    print ("You found speed boots! Your evasion chance has risen by 10%!")
                    stats["Evasion"].append(ev)
                elif lootChance3 <= 75 and lootChance3 >=71:
                    stats["Evasion"].append(ev)
                    stats["Evasion"].append(ev)
                    print ("WOW, you found Hermes' boots! Your evasion chance has risen by 20%!")
            else:
                print ("You found no loot.")

            print ("Your current health is " + str(int(stats["Health"])))
            print(events[7])
            print (events[15])
            break

def treasureRoom():
    print (events[4])
    playerInputTreasure = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    treasureChoice = True
    while treasureChoice == True:
        playerInputTreasure[0] = input("Would you like to OPEN the chest or LEAVE? : ")
        playerInputTreasure[0] = playerInputTreasure[0].lower()
        if playerInputTreasure[0] == "open":
            playerInputTreasure.remove("open")
            chance = random.randint(1, 3)
            if chance == 3:
                print ("You got Lucky! You found 200 gold!")
                stats["gold"] += 200
                print ("You got lucky this time but next you could lose something instead of gaining.")
            elif chance < 3:
                mimicAttack()
                treasureChoice = False
                break
        elif playerInputTreasure[0] == "leave":
            playerInputTreasure.remove("leave")
            print (events[5])
            print (events[15])
            treasureChoice = False
        else:
            print ("Try again.")
            continue


def shop():
    print (events[16])
    print ("You have " + str(stats["gold"]) + " gold.")
    maybeShop = True
    while maybeShop == True:
        choice = input ("Would you like to shop? : ")
        if choice == "yes" and stats["gold"] >= 0:
            shopping = True
            while shopping == True:
                choice2 = input ("""What would you like to buy?

    Weapon - 1000 gold
    Max Potion - 500 gold
    Talisman - 1000 gold
    Health Potion - 200 gold

Or would you like to leave? : """)
                choice2 = choice2.lower()
                if choice2 == "weapon" and stats["gold"] >= 1000:
                    stats["gold"] -= 1000
                    print ("You bought a weapon! Your attack has been increased by 10!")
                    stats["Attack"] += 10
                    stats["Attack"] = int(stats["Attack"])
                    print ("\"Good choice\" he says.")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "weapon" and stats["gold"] < 1000:
                    print ("\"Sorry but you don't have enough gold to buy that.\"")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "maxpotion" or choice2 == "max potion" and stats["gold"] >= 500:
                    stats["gold"] -= 500
                    print ("You bought a potion! Your max health has been increased by 20!")
                    stats["maxHealth"] += 20
                    print ("Your max health is now " + str(stats["maxHealth"]) + "!")
                    print ("\"Good choice\" he says.")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "maxpotion" or choice2 == "max potion" and stats["gold"] < 500:
                    print ("\"Sorry but you don't have enough gold to buy that.\"")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "talisman" and stats["gold"] >= 1000:
                    stats["gold"] -= 1000
                    print ("You bought a talisman! Your defence has increased by 1!")
                    stats["Defence"] += 1
                    stats["Defence"] = int(stats["Defence"])
                    print ("\"Good choice\" he says.")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "talisman" and stats["gold"] < 1000:
                    print ("\"Sorry but you don't have enough gold to buy that.\"")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "healthpotion" or choice2 == "health potion" or choice2 == "health" and stats["gold"] >= 200:
                    stats["gold"] -= 200
                    print ("You bought a health potion! You can never be too careful.")
                    stats["potions"] += 1
                    print ("You have " + str(stats["potions"]) + " potions now.")
                    print ("\"Good choice\" he says.")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "healthpotion" or choice2 == "health potion" and stats["gold"] < 200:
                    print ("\"Sorry but you don't have enough gold to buy that.\"")
                    print ("You have " + str(stats["gold"]) + " gold left.")
                    continue
                elif choice2 == "leave":
                    shopping = False
                    break
                else:
                    print ("\"I don't have anything like that in stock.\"")
                    continue

        elif choice == "no":
            print ("\"Suit yourself\" he says sliding back into the darkness.")
            print (events[15])
            break

        elif choice == "yes" and stats["gold"] <= 0:
            print ("Your only have " + str(stats["gold"]) + " gold!")
            print ("\"Looks like you don't have enough. Why don't you go find some? Hehehehe\"")
            break

        else:
            print ("\"What language are you trying to speak?\"")
            continue

def minotaurAttack():
    print (events[19])
    input ("Press enter to continue.")
    print (events[20])
    playerInput = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    turn = 0
    while minotaurBoss["Health"] > 0:
        chance = random.randint(1, 2)
        if chance == 1:
            attackDirection = "l"
            attackDirection = attackDirection.lower()
        elif chance == 2:
            attackDirection = "r"
            attackDirection = attackDirection.lower()
        playerInput[0] = input("Would you like to attack(a) or heal(a)? : ")
        playerInput[0] = playerInput[0].lower()
        if playerInput[0] == "a":
            minotaurBoss["Health"] -= int(stats["Attack"] / minotaurBoss["Defence"])
            playerInput.remove("a")
            print ("You attack the monster with all your might.")
            print ("You deal " + str(int(stats["Attack"] / minotaurBoss["Defence"])) + " damage to the monster")
            print ("The monster has " + str(minotaurBoss["Health"]) + " health left.")
            if minotaurBoss["Health"] <= 0:
                break
            turn += 1

        elif playerInput[0] == "h":
            playerInput.remove("h")
            if stats["potions"] > 0:
                stats["potions"] -= 1
                stats["Health"] += 30
                if stats["Health"] > stats["maxHealth"]:
                    stats["Health"] = stats["maxHealth"]
                print ("You healed for 30 hp")
                print ("Your current health is " + str(int(stats["Health"])))
                print ("You have " + str(stats["potions"]) + " potions left.")
                turn += 1

            else:
                print ("You have no more potions!")

        else:
            print ("That is not a valid action!")
            continue

        if turn == 3:
            print ("It's attacking!")
            blockChoice = input ("Should you prepare to block left(L) or right(R)? : ")
            blockChoice = blockChoice.lower()
            if blockChoice == attackDirection:
                print("Success! You defended the correct direction!")
                turn = 0
                continue
            elif blockChoice != attackDirection:
                print ("Incorrect! You didn't block the correct direction!")
                stats["Health"] -= int(minotaurBoss["Attack"] / stats["Defence"])
                print ("The monster did " + str(int(minotaurBoss["Attack"]) / stats["Defence"]) + " damage to you!")
                print ("Your current health is " + str(stats["Health"]) + ".")
                turn = 0
                continue

        if minotaurBoss["Health"] <= 0:
            break

        if stats["Health"] <= 0:
            print (r""" you died""")
            break

# - Variation of boss where its attacks are quick time events
def QTEminotaurAttack():
    print (events[19])
    input ("Press enter to continue.")
    print (events[23])
    playerInput = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    turn = 0
    while minotaurBoss["Health"] > 0:
        chance = random.randint(1, 2)
        if chance == 1:
            attackDirection = "left"
            attackDirection = attackDirection.lower()
        elif chance == 2:
            attackDirection = "right"
            attackDirection = attackDirection.lower()
        playerInput[0] = input("Would you like to attack or heal? : ")
        playerInput[0] = playerInput[0].lower()
        if playerInput[0] == "attack":
            minotaurBoss["Health"] -= int(stats["Attack"] / minotaurBoss["Defence"])
            playerInput.remove("attack")
            print ("You attack the monster with all your might.")
            print ("You deal " + str(int(stats["Attack"] / minotaurBoss["Defence"])) + " damage to the monster")
            print ("The monster has " + str(minotaurBoss["Health"]) + " health left.")
            turn += 1

        elif playerInput[0] == "heal":
            playerInput.remove("heal")
            if stats["potions"] > 0:
                stats["potions"] -= 1
                stats["Health"] += 30
                if stats["Health"] > stats["maxHealth"]:
                    stats["Health"] = stats["maxHealth"]
                print ("You healed for 30 hp")
                print ("Your current health is " + str(int(stats["Health"])))
                print ("You have " + str(stats["potions"]) + " potions left.")
                turn += 1

            else:
                print ("You have no more potions!")

        else:
            print ("That is not a valid action!")
            continue

        if turn == 3:
            turn = 0
            print ("It's attacking!")
            def warning():
                print ("Get Ready!")
                time.sleep(1)
                print ("3")
                time.sleep(1)
                print ("2")
                time.sleep(1)
                print ("1")
                time.sleep(1)
                print ("Go!")
                time.sleep(1)

            QTE_inputs = ["left", "right", "up", "down", "forward", "backward", "dodge", "block", "parry", "deflect", "riposte", "slide", "flip", "twirl"]

            def QTE():
                print ("Not fast enough!")
                stats["Health"] -= int(minotaurBoss["Attack"] / stats["Defence"])
                print ("The monster did " + str(int(minotaurBoss["Attack"]) / stats["Defence"]) + " damage to you!")
                print ("Your current health is " + str(stats["Health"]) + ".")
            z = 0
            stop = False
            warning()
            timer = threading.Timer(12, QTE)
            timer.start()

            while z < 5:

                while timer.is_alive() == True and stop == False:
                    if z == 5:
                        break
                    QTE_choice = random.choice(QTE_inputs)
                    print (QTE_choice)
                    choice = input ("")
                    choice = choice.lower()
                    if z == 5:
                        break
                    if choice == QTE_choice and timer.is_alive() == True:
                        print ("Correct!")
                        z += 1
                        continue
                    elif choice != QTE_choice and timer.is_alive() == True:
                        timer.cancel()
                        print ("Incorrect!")
                        stats["Health"] -= int(minotaurBoss["Attack"] / stats["Defence"])
                        print ("The monster did " + str(int(minotaurBoss["Attack"] / stats["Defence"])) + " damage to you!")
                        print ("Your current health is " + str(stats["Health"]) + ".")
                        stop = True
                        break

                if timer.is_alive() == False:
                    break

            if z == 5:
                timer.cancel()
                print ("You successfully avoided all of the minotaurs attack! .......for now.")
                continue

        if minotaurBoss["Health"] <= 0:
            break
        elif minotaurBoss["Health"] > 0:
            continue

        if stats["Health"] <= 0:
            print ("You died!")
            break


def fountain():
    print (events[22])
    print ("You feel rejuvenated! You are now at max health!")
    stats["Health"] = stats["maxHealth"]

# start here



print (tutorial)
input ("Press Enter to continue!")
print (start)

input("Press Enter to start!")

if random.randint(1, 10) > 5:
    attackEvent(events[0], events[1], slime)
else:
    print ("After a peaceful sleep you pack up camp. You regather all of your belongings and head into the dungeon. ")

input ("Press Enter to continue!")

while stats["Health"] > 0 and i <= 30:
    chance = random.randint(1, 11)
    if chance == 1:
        attackEvent(events[2], events[3], goblin)
        goblin["Health"] = 20
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 2:
        attackEvent(events[8], events[9], skeleton)
        skeleton["Health"] = 40
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 3:
        attackEvent(events[10], events[11], abomination)
        abomination["Health"] = 50
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 4:
        attackEvent(events[13], events[14], spider)
        spider["Health"] = 40
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 5:
        treasureRoom()
        mimic["Health"] = 30
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 6:
        print (events[12])
        input ("Press Enter to continue!")

    elif chance == 7:
        shop()
        input ("Press Enter to continue!")

    elif chance == 8:
        attackEvent(events[17], events[18], maniac)
        maniac["Health"] = 30
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 9:
        fountain()
        input ("Press Enter to continue!")

    elif chance == 10:
        attackEvent(events[25], events[26], troll)
        troll["Health"] = 70
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 10:
        attackEvent(events[27], events[28], zombie)
        zombie["Health"] = 80
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

    elif chance == 11:
        attackEvent(events[29], events[30], vampBat)
        vampBat["Health"] = 30
        input ("Press Enter to continue!")
        i += 1
        if stats["Health"] <= 0:
            break

if i == 31:
    minotaurAttack()
#   QTEminotaurAttack()
    print (events[21])
    i += 1
    input ("Press Enter to continue!")

if i == 32:
    print ("You win!")



