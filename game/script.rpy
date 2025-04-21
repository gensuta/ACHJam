# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rose", color="#F785B1")
define j = Character("Jade", color ="#31c493")
define p = Character("Pearl", color="#FFF9EB")
define ol = Character("Old Lady")
define c = Character("Cat")

define v = Character("Voice")

define i = Character("Ice-cream man")
define oo = Character("Optometrist")
define n = Character("Neighbour")
define d = Character("Ron the Dog")
define js = Character("Jasper")
define l = Character("Library patron")
define e = Character("Employee")



# The variables below are for minigames! Please ignore and do not touch!! -Geneva
default calmCounts = 0
default currentCount = 0 
default isDistracted = False
default clicked_one = False
default clicked_two = False
default clicked_three = False
default clicked_four = False #note to self, I don't think we need this? - gen
default is_counting_up = True
default current_diary_page = 0 # helps to show specific colors!
default emotion_names = [] # these are two variables to help with the diary entry! 
default emotion_colors = []
# End of minigame variables!

#custom transforms! Please ignore -Geneva
transform shaking_text:
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2 
            linear 0.1 xoffset 3 yoffset -3 
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat
#End of custom transforms

#colors for transform below- geneva
# figured out courtesy of this reddit thread (https://www.reddit.com/r/RenPy/comments/18nyqvu/how_do_i_add_colour_to_greyscale_images/)
transform red:
    matrixcolor TintMatrix("#c98484") * SaturationMatrix(1.0)

transform blue:
    matrixcolor TintMatrix("#4c68c2") * SaturationMatrix(1.0)

transform lightblue:
    matrixcolor TintMatrix("#7ab9dd") * SaturationMatrix(1.0)

transform darkgreen:
    matrixcolor TintMatrix("#386134") * SaturationMatrix(1.0)

transform lightgreen:
    matrixcolor TintMatrix("#7db877") * SaturationMatrix(1.0)

transform yellow:
    matrixcolor TintMatrix("#f5e9ae") * SaturationMatrix(1.0)

transform gold:
    matrixcolor TintMatrix("#ffce47") * SaturationMatrix(1.0)
    
transform purple:
    matrixcolor TintMatrix("#bc7bda") * SaturationMatrix(1.0)

transform violet:
    matrixcolor TintMatrix("#9f7bda") * SaturationMatrix(1.0)

transform lightorange:
    matrixcolor TintMatrix("#ecaa7a") * SaturationMatrix(1.0)

transform darkorange:
    matrixcolor TintMatrix("#eb985c") * SaturationMatrix(1.0)

transform pink:
    matrixcolor TintMatrix("#f1b6de") * SaturationMatrix(1.0)

transform beige:
    matrixcolor TintMatrix("#e4c9a8") * SaturationMatrix(1.0)


# The game starts here.


label start:

    #OPTOMETRY CLINIC SCENE

    scene bg optometry

    show rose ng at left with dissolve
    show optometrist at right with dissolve


    oo "Okay, we’re almost done with the optometric evaluation. Now look at me. What do you see?"

    r "Everything’s still in black and white, as it’s always been."

    oo "Well, this confirms it then, emotional blindness."

    r "What does it mean?"

    oo "As you know… although not from experience, given your condition… human beings express their emotions through coloration changes." 
    
    oo "So, if you see a person coloring yellow you know they’re… well, I guess you wouldn’t know, would you?"

    r "..."

    oo "Challenges in recognizing, expressing, feeling and describing emotions are all symptoms of emotional blindness."

    oo "That’s where the glasses come in, they’re designed to help people with your condition see colors, your own as well as other people’s."

    oo "Recognizing emotions will also help you flexibly respond to your own emotional states and will improve your interactions with others."

    #Here the game should fade to black (done!)
   
    scene bg optometry with fade 
    show rose blank at left with dissolve
    show optometrist at right with dissolve

    oo "How are the glasses? Anything?"

    show rose talking at left

    r "...nothing different."

    oo "Well, that’s never happened before… these glasses are the gold standard for emotional blindness."

    show rose blank at left

    oo "In any case, keep them on at all times, I’m sure you just need to get used to them and they’ll start working soon."


    #Here the game should fade to black (done!)


    #TOWN SCENE 
     

    scene bg jade home outside with fade
    show rose blank at center with dissolve

    play music "music/mail delivering.mp3"

    r "{i}It’s been three months, but my world hasn’t changed.{/i}"

    r "{i}I still don’t know what it means to see a color…{/i}"

    r "{i}…and I have no idea how I’m feeling most of the time.{/i}"

    r "{i}But I know I’m good at my job and, although it might seem boring or lonely on the outside, I think it suits me.{/i}"

    stop music fadeout 1.0

    #Here the game should fade to black (done!)


    #JADE'S HOUSE SCENE (OUTSIDE)

    play music "music/Reading the letter.mp3"

    scene bg letter with Fade(0.5,0.0,0.5) #Why doesn't it show up? (It wasn't showing up because it was being quickly replaced by jade's home! Fixed it by adding a pause)
    pause 2.5


    scene bg jade home outside
    show rose blank at left

    r "Strange… it looks like the name doesn’t match the resident."


    stop music fadeout 1.0

    #CHOICE: Sound the doorbell / Leave the letter in the mailbox anyway (done!)

    menu:
        "Sound the doorbell":
            jump sound_doorbell #we're jumping to what happens after we ring the doorbell!
        "Leave the letter in the mailbox anyway":
            jump leave_letter #we're jumpint to what happens after we ring the doorbell



label sound_doorbell:
    #SOUND THE DOORBELL 

    #Here the game should fade to black (done!)
    scene bg jade home outside with fade
    show rose blank at left with dissolve

    v "Hello? Ah, hold on, don't leave just yet!"

    show rose talking at left

    r "I haven’t moved."

    v "Okay, I’m nearly at the door-"

    jump jades_house
   

label leave_letter:
    #LEAVE THE LETTER IN THE MAILBOX

    #Here the game should fade to black (done!)

    scene bg jade home outside with fade
    show rose blank at left with dissolve

    r "Well… It's addressed to here. They can sort it out."

    v "Miss? Excuse me, Miss?"
    jump jades_house


label jades_house:

    #JADE'S HOUSE SCENE 2 (OUTSIDE) 
    
    #Following both choices

    #Here the game should fade to black (done!)

    scene bg jade home outside with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    play music "music/anticipation.mp3"

    j "Hello, forgive my lateness, I had headphones on."

    r "Only been a few seconds. Anyway, I have a letter-"

    show jade talking at center

    j "Oh, wow, it's all engraved and pretty. It would be a crime to tear it open."

    show rose talking at left

    r "Please, hold on a second-"

    show jade blank at center

    j "Still, there's boxes unopened, maybe mum put my letter opener in there…"

    r "No, no. It's not your letter- I mean, this letter is addressed to the previous occupant, one “Pearl” at this address."

    show jade talking at center
    show rose blank at left
   
    j "Hm? Oh… Oh my goodness, I am so sorry! Almost committed a crime. I could go to jail!"

    r "It's fine…"

    j "Fine? I can pay for that. How much, ten? Twenty?"

    show rose talking at left

    r "It is fine. Synonymous with “alright”. No crime committed. Now, by chance, do you know their current location?"

    show jade blank at center
    show rose blank at left 

    j "Uhm…"

    r "No, then?"

    j "Yes to the no."

    r "Very well. Undelivered it is."

    show jade talking at center

    j "What now? You've got computers for this?"

    r "Only cabinets. Full of paperwork."

    show jade talking at center

    j "Wait-wait. I can help, I can help!"

    r "...?"

    j "Ah. Uh… Ah! It's only been a month since I got here. Nooks and crannies yet to clean - especially the cupboards - maybe a clue might be lying about in the apartment."

    show rose talking at left
    
    r "Clue?"

    show jade blank at center
    show rose blank at left

    j "You know, old pamphlets to locales or-or childhood photos of happy places… oooooh I can smell the adventure. Let's have a look around!"

    r "I might just ask neighbours…"

    j "That too! I can take notes. I've a pen and paper on my desk. Oh, and I'm Jade, BTW, but you probably already know, with the name at the door."

    show rose talking at left
   
    r "Rose… good to meet you."

    stop music fadeout 1.0

    #CHOICE: Ask the neihgbour / Look inside Jade's apartment for clues 
    menu:
        "Ask the neighbor":
            jump ask_neighbor_first
        "Look inside Jade's apartment for clues":
            jump check_apartment_first
   

   
label ask_neighbor_first:
    #ASK THE NEIGHBOUR AS FIRST CHOICE 
    #Here the game should fade to black (done)

    scene bg jade home outside with fade
    show rose blank at left with dissolve
    show jade blank l at center with dissolve

    j "Excuse me. Hello? Anyone there?"

    v "Don't you dare knock again. I just got the little blighter down for his nap."

    show rose talking at left 

    r "Noted. And it’s me-"

    show rose blank at left

    v "Oh, it’s you. You're a day early, this time. Did Lily have something going on?"

    r "No care package today, I don’t know what Lily is up to. Can we ask some questions?"

    show jade talking l at center

    j "Forgive her rudeness, we’re just here to sort something out. Something to do with your old neighbour - I’m your new neighbour by the way, Jade, but yeah."

    v "Alright, alright, very pleased to meet you. Now, you were saying…"

    show jade blank l at center
    show rose talking at left

    r "Sorry, no care package delivery today. Your calorie count remains true. As she has said, we need a word about your old neighbour."

    show rose blank at left 

    v "Old neighbour… ah, who was it? Darned if I can remember their name."

    show rose talking at left

    r "Anything you can tell us…"

    show rose blank at left

    v "She was one of those artist types I think, you know. Always in something she made herself. Once tried talking to ‘er, but she disappeared just round the corner. It was a lovely outfit out of an old duvet cover, pair of shades glimmering just like that stone…"
    
    v "What was it? Found at the sea - Opal, that was her name."

    r "It says “Pearl” on the letter."

    show jade talking l at center

    j "Maybe it’s like my mum and my big bro’s letters. He’s in Korea, South Korea, and his letters still arrive at mum’s house. Right? So maybe this Opal could be a clue to reaching Pearl?"

    r "Any idea where Opal could be?"

    show jade blank l at center

    v "Last I saw, she was down by the cafè. If that's all you need of me, then good luck with you. I think I hear him start to stir."

    show jade blank at center
   
    j "Artist... hmm."

    r "Another lead?"

    j "I believe so, leading right back home…"

    #Here the game should fade to black (done)

    scene bg jade home inside with fade
    show rose blank at left with dissolve
    show jade blank at right with dissolve

    play music "music/letter painting.mp3"

    j "The moment I heard “artist”, it hit me, just like that! Right against the back of the cupboard…"

    r "Lots of other stuff from the old tenant."

    j "No… that’s me."

    show rose talking at left

    r "A lot of worn down baseballs. Were you an athlete?"

    j "No, just holding onto them for a friend. Ah, here we are."

    scene bg portrait 1 with Fade(0.5,0.0,0.5) 
    pause 2.5

    scene bg jade home inside
    show rose blank at left
    show jade blank at right


    r "It’s nice. Such a cute cat."

    j "Indeed, indeed, but look at the signature in the corner."

    show rose talking at left

    r "Opal… But I thought Pearl lived here?"

    show rose blank at left
    show jade talking at right

    j "Maybe it was a gift, or a personal commission. But the bottom line is clear: we find Opal, we find Pearl."

    show rose talking at left
    
    r "How certain are you?"

    show jade blank at right

    j "Roughly ninety-percent, as sure as the shape of my eyes."

    show rose blank at left

    r "If you say so. We could take this, in case anyone has seen this work."

    j "And click. Onto the phone, and the weight of a canvas off our shoulders."

    stop music fadeout 1.0

    jump cafe


label check_apartment_first:
    #JADE'S APARTMENT AS FIRST CHOICE

    #Here the game should fade to black (done)
    scene bg jade home inside with fade
    show rose blank at left with dissolve
    show jade blank at right with dissolve

    play music "music/letter painting.mp3"

    j "Come on, where are you? I know you’re stocked up somewhere…"

    show rose talking at left

    r "Very… organised."

    j "Hardly, most of it is taking refuge in my bedroom. Open the door and we’d be buried in a landslide of books and - ah ha! Got you, and... behold."

    scene bg portrait 1 with Fade(0.5,0.0,0.5) 
    pause 2.5

    scene bg jade home inside
    show rose blank at left
    show jade blank at right

    r "A painting. Of a cat."

    j "Indeed, and what can you see on it?"

    show rose talking at left

    r "... brush strokes?"

    show jade talking at right

    j "Uhm, yes. But, beyond the brush, we may find - pause for effect - a name!"

    show rose blank at left

    r "It says “Opal” not “Pearl”."

    j "True, but it was found {i}inside{/i} of Pearl’s old home. Which means, a connection."

    r "What kind, though?"

    show jade blank at right

    j "Hm. That, we need to find out. Any ideas, partner?"

    show rose talking at left

    r "Partner?"

    j "Yeah, partners, solving a mystery!"
    
    r "We could try the neighbour next door?"

    j "Excellent. Click! And a photo of the portrait for the road. Can’t have us lugging that precious article around town with a risk of rain or breaking."

    show rose blank at left
   
    r "Clever."

    j "Ah, thank you. Now, onwards!"

    stop music fadeout 1.0

    #Here the game should fade to black (done)


    scene bg jade home outside with fade
    show rose blank at left with dissolve
    show jade blank l at center with dissolve

    r "Best you let me sort this one out. They prefer a certain way of alerting them."

    r "{i}*whistles like a bird*{/i}"

    v "Ah, you’re early this week. Any news of Lily’s care package?"

    r "No care package, only a question. If you could look through the peep-hole…"

    v "My eye is up here. Ha ha. Oh, you’ve got a partner in crime I see."

    r "No, still working solo."

    show jade talking l at center

    j "Oh, hello, I’m Jade - your new neighbour - and uhm, tell us, do you know anything about who painted - hold on, just got to unlock my phone - who painted this?"

    v "Hmmm, I think I recognise the style - wait, Opal? I hadn’t realised she actually left."

    j "I just told you I’m your new neighbour."

    show rose talking at left

    r "But the letter said “Pearl”, not “Opal”."

    j "Maybe it’s like my mum and my big bro’s letters. He’s in South Korea, and his letters still arrive at mum’s house. Right? So Opal could still be a clue in reaching Pearl?"

    r "I suppose… any idea where Opal could be?"

    v "Last I saw, she was down by the cafè. Well, either way, best of luck to you two."

    show rose blank at left
    show jade blank at center

    r "Thank you."

    j "So what do ya’ think?"

    r "Of what?"

    j "Opal giving the painting to Pearl."

    r "Was the painting a gift?"

    j "I like to think so. A parting present, of memories shared, a moment crystallised into an immortal image."

    show rose talking at left

    r "Of a cat?"

    j "For that was the shape of Pearl’s soul to Opal."

    r "You’re just making this up, aren’t you?"

    j "Well, we need some dramatics in this quest."

    jump cafe


label cafe:
    #Here the game should fade to black (done)
    #CAFE SCENE 
    play music "music/cafe.mp3"
    scene bg cafe with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve


    j "What a cosy little place."

    r "It is."

    j "You come here often?"

    r "Yes."

    j "Well then, mind me seeing what the town has to offer?"

    r "No, thank you, we’ve got the painting to find-"

    r "{i}*stomach growls*{/i}"

    show jade talking at center

    j "We can talk about that over lunch, on me!"

    show rose talking at left

    r "They work by table numbers. Remember the number, walk up to the counter, and place your order."

    j "I appreciate the clarity."

    r "They have pictures on the menus too."

    j "I meant… actually, oh, this is actually a good spread: jewelled salad, chicken noodle soup with croutons - steak and kidney pie with fries and gravy!? I’ve not had that in ages. We’ve got to have some."

    r "No thank you? Not my favourite dish."

    show jade blank at center

    j "Hmmm, alright then, what’s your favourite?"

    show rose blank at left

    r "Homemade burger with coleslaw."

    show jade happy at center

    j "And it’s got a special side of onion rings and curly fries. That is awesome!"

    r "Is it?"

    show jade sad at center

    j "...is everything okay? Oh heck, is this about something I did?"

    r "Not your fault."

    j "Then what?"

    r "Nothing, really. I’m just not a talkative person."

    show jade talking at center

    j "...okay. Looks like a pretty big line. I ain’t standing for minutes on end just fidgeting, so..."

    j "... seen any good shows? Blergh, so cliche a starter…"

    show rose talking at left

    r "I recently watched “Tower of Phantometer” cutscenes online, if that counts."

    j "Phantometer? Oh, yeah, the videogame? With the cute critter in the armour?"

    r "Action-Platformer where you played as Luna. Ascending up the Tower of Phantometer to reach the stars, in the hope that one of them is the spirit of her loved one, whose identity depended upon the questions you answered at the start."

    show jade blank at center
    
    j "Yeah… that one."

    r "Watched playthroughs of it when I was younger. The music helped me sleep. Story was well-written. Still holds up. Still wish I could play it. Too expensive then, too rare now."

    j "I’ve got a copy!"

    show rose blank at left

    r "Hmm?"

    j "Yeah, original manual and everything. If ever you have a day off..."

    r "Thank you."

    show jade sad at center

    j "Huh, with all those details, I’d figured you’d be more… ecstatic."

    show rose talking at left

    r "Ecstatic?"

    show jade talking at center

    j "A chance at playing that game that eluded your grasp, isn’t that exciting?"

    show rose blank at left

    r "I’m not sure…"

    show jade blank at center

    j "When I’m excited about something, I can’t stop talking about it. I can’t even sit still, it’s like-too much for my body to hold, if that makes sense?"

    r "I guess-I guess I did feel something, when we were talking about Phantometer. A weird sensation in my chest. My heart beating faster? I’m just never sure if it means I’m excited or nervous… and I’d rather not think about it right now."

    j "Well, to be fair, we got other fish to fry, so no need to dwell. And speaking of food, looks like the line’s shortened. Figured out your order?"

    
    #CHOICE: Safe food/New food
    menu:
        "Choose your safe food":
            jump safe_food
        "Choose something new":
            jump new_food

label safe_food:
    #SAFE FOOD
    #Here the game should fade to black (done)
    scene bg cafe with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    r "Double burger with coleslaw, please."

    j "Stick to what you know, fair enough."

    #Here the game should fade to black (done)
    scene bg cafe with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    j "He he he. Now look at the crispy flakiness of that pastry. It feels like a crime to tear it open. How about your burger?"

    r "It’s well put together."

    show jade talking at center

    j "Well put together?! That wooden stake is keeping that monster in check. You got to slay it before it falls apart!"

    r "Not until the fries are eaten with the coleslaw."

    show jade blank at center

    j "Okay, but you’ll be way behind once I’ve cleaned the gravy from the plate."

    j "Oh, blimey, need a breather. But I ain’t getting defeated by beef. You with me?"

    r "Beef defeated."

    j "Holy! That was fast. Are you sure you had time to chew?"

    r "You sound like my granddad. He said he’d always buy me a burger."

    j "Sounds like a good grandpa."

    show rose talking at left

    r "Joked he only did so to see if I unhinged my jaw before I ate. I’d hiss every time I saw him. People stared. But granddad always smiled. Wasn’t sure if he actually found it funny."

    j "You must hold those memories very dear."

    r "It does feel good to relive them. I feel… calmer, somehow."

    show jade talking at center
    
    j "I get it. And my grandpa always bought me lunch too, even if I had the cash. He and I would buy the cheapest thing the cafe had {i}*chuckles*{/i} I’ll give you three guesses."

    show rose blank at left
   
    r "Hm…"

    j "It’s literally served on a platter for you."

    r "No, not the pie and fries?"

    r "Wait-Look behind you. Actually, could you get your phone out?"

    jump the_painting

label new_food:
    #NEW FOOD
    #Here the game should fade to black (done)
    scene bg cafe with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    r "I’ll have what you’re having."

    j "Prepare for a wonderful food sensation!"

    #Here the game should fade to black (done)
    scene bg cafe with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    j "So… how is it?"

    r "It’s nice."

    j "That’s all?"

    r "Is that not all there is to it?"

    show jade talking at center

    j "But what about- what about the smell? The sound? Heck, have you even smelt it?"

    r "It smells… warm."

    j "“Warm”? Nothing more? Fine. Let's start with the finer points of pie enjoyment. Take your fries - or chips, as they’re known in some places - onto your fork."

    r "Okay…"

    j "Now, with the knife in hand, get all that beautiful gravy onto the fork. Yep, good, good. And finally, top with a piece of the pastry."

    r "M-okay"

    j "Now let it settle on the palate. The crispy flakes drawing in the other flavours like a sponge. How easily it binds together with the carrots and peas, further sweetened by the jamminess of the onions."

    r "..."

    j "And what of the chips? Can you feel the texture, the salty crispiness, now melting away within the gravy, a gentle cloudiness at the tongue. The warmth of the meal, it descends like a comet into your stomach, turning it into a furnace and-" 
    
    show jade blank at center
    
    j "Eh he he, got carried away there, didn’t I?"

    r "A bit."

    j "I just think some experiences need to be savored, right? You never know how happy you are until you truly pay attention to it."

    j "Plus focusing on what I enjoy helps me block out the stuff that annoys me."

    show jade angry at center
    
    j "Like this godawful smell, for example! What do you think it is?"

    r "Hmm, maybe… vinegar?"

    j "Ugh."

    show jade talking at center
    
    j "Anyway, I used to take cooking classes with my friends... The chef was always like that. The “poet” sort of cook, but their enthusiasm was so contagious I-"

    show rose talking at left
   
    r "I’m sorry to interrupt, but does that look familiar to you?"

    jump the_painting

label the_painting:
    #THE PAINTING 

    #Here the game should fade to black (done)
    #Following both choices

    scene bg portrait 2 with fade
    pause 2.0 #making sure it doesn't get skipped over like the letter! (Geneva)

    scene bg cafe with fade
    show rose blank at left with dissolve
    show jade talking l at center with dissolve

    j "Is that…?"

    r "Opal’s cat."

    j "Only now it’s staring lovingly at a sunset."

    r "It looks familiar."

    j "Certainly evokes post-impressionism, especially the focus on light."

    r "The way the sunlight goes through it."

    j "Definitely an early attempt at the style. Sorry, I took some classes, and it’s so rare I get to talk shop on art history, especially around-"

    show rose talking l at left
    
    r "The bench!"

    j "What bench!?"

    r "In the park."

    j "The park in town?"

    r "The park in town."

    j "How far is it?"

    r "Just across the road."

    show jade happy l at center

    j "Ready to go?"

    #Here the game should fade to black (done!)

    #PARK SCENE 
    stop music fadeout 1.5
    scene bg park with fade
    show rose blank at center with dissolve
    show jade blank at right with dissolve


    j "Should we ask somebody if they remember seeing our mystery lady around here?"
   
    r "Hmm, I know that dog…"

    show jade sad at center

    j "Uh, right,  well… the ice-cream man looks like a more promising lead to me. Being at the park all the time and all."

    #CHOICE: Ask the ice-cream man / Ask the man on the bench
    menu:
        "Ask the ice-cream man":
            jump ask_icecream_man
        "Ask the man on the bench":
            jump ask_bench_man


label ask_icecream_man:
    #Here the game should fade to black (done!)
    scene bg icecream with fade
    show rose blank at left with dissolve
    show jade blank l at center with dissolve
    show icecream man at right with dissolve

    play music "music/ice cream kiosk.mp3"

    r "Excuse us?"

    i "Oh, it's you, we finally meet."

    r "P-pardon?"

    i "Haven’t seen you in a while, I was beginning to worry about you."

    show jade talking l at center

    j "Hang on, hang on. Rosie, you know this person?"

    i "Hm? Ah, my mistake, but the way you were standing there… no… you’re definitely much younger and taller than her… must be the clothes. I’m sorry, just a bit of rambling on my part. Hope you have a good day."

    j "We haven’t even asked yet."

    i "Oh right, one scoop or two?"

    j "We mean… uhm, Rosie, you want anything?"

    r "{i}*nods and holds up two fingers*{/i}"

    show jade happy l at center

    j "Very well. Good sir, we shall take two of the finest scoops of your ice cream. In exchange, mind telling us of “Opal” and her bench-sitting ways?"

    show jade blank l at center
    
    i "Opal? So that was her name. Truth be told, we never actually talked. She’d be sitting right there on the bench. But on the dot, every day before the walkers came round. I could time my work hours just by her presence alone. My human timepiece, ha."
    
    i "At least, that was how it was until a few weeks ago. Then she was gone, and her little cat, too."

    r "Cat?"

    j "Just like in the picture. Any other notable features? Hair colour, hair style, facial features, maybe a cool iconic item?"

    i "Mmm, unfortunately none spring to mind. She was well covered for winter, no matter the season. Honestly I’m surprised she didn’t melt."

    show jade sad l at center
    
    j "Dang. Guess we’re back to square one, then."

    show rose talking at left

    r "Not yet. Did Opal always leave the park the same way?"

    show rose blank at left

    i "Off towards that direction, right to the –"

    j "The bench!"

    i "Yes, in that general direction…"

    stop music fadeout 1.0


    #Here the game should fade to black (done)

    scene bg bench with fade
    show rose blank at left with dissolve
    show jade sad l at center with dissolve
    show jasper at right with dissolve

    r "Uhm, excuse me, I-"

    d "Bark-bark-bark-bork!"

    j "Ah... good dog, nice dog…"

    js "Now look what you bloody done, Ron, hush up. Hang on a second."

    r "Sorry for disturbing your peace, we just needed to-"

    js "Rose! I thought I recognised that voice. Well, no wonder Ron got all excited. Never thought I’d see you out of the routes, unless this is some premium service I don’t know a thing ‘bout."

    show rose talking at left
    
    r "Good day Jasper. Enjoying the scenery?"

    d "{i}*whines*{/i}"

    show rose blank at left

    j "Actually, we’re looking for someone. You wouldn’t have happened to have seen anyone on this bench before you-"

    js "Still haven’t found that Opal yet, then?"

    j "How do you know…?"

    js "Forgetful aren’t we, do I need to remind you you’re my new neighbour?"

    j "Oh, I didn’t recognize your voice!"

    js "The fine scenery is why I’m here, Rose, just look at that sunshine through the leaves!"

    r "It is nice. Anything you can tell us about Opal?"

    js "Sorry, lass, haven’t seen anyone else here for the past month. Especially with Ron, here, barking at his own shadow."

    scene bg bench with dissolve
    show rose blank at left
    show jasper at right
    show jade very sad l at center 

    j "Hmm… sorry, I-I need a moment."

    r "I’ll join you in a minute...I wish to talk more to Jasper."

    j "Wha’? Oh yeah, yeah."

    scene bg bench
    show rose blank at left
    show jasper at right
    hide jade sad l with dissolve
  
    r "Please excuse my … friend, she seems quite shy around... I’m not sure what she’s feeling, as usual."

    js "Indeed, a funny friend you’ve found, how long you’ve known ‘em?"

    r "Just today… not sure we're friends yet."

    js "Looks like it to me. But what do I know? If not, then let the pieces play out."

    r "Hm?"

    js "Fine though I be in that house, solitude can bite away at even the greatest hermits."

    r "..."

    js "No shade upon your stoicisms and the like. But hear me out, for all the moments you’ve planned, a funny friend colours the emptiness between them all the brighter."

    d "{i}*whines*{/i}"

    js "Not sure how I’d spend my days without this wee bounder and his chatterings. Probably just waiting every day for the next care package from Lily. Sometimes one just isn’t enough."

    r "Still not sure about that."

    js "Well, whatever, it’s down to you and that lass, not I, or anyone else. All I can do is provide a bit of wisdom. First step, catching up with her."

    r "Oh, right. See you next round of post, with Lily’s care package."

    js "Until then. Take care, Rose, and if you see that cat-walker, Opal, give ‘em my regards."

    show rose talking at left

    r "Cat?"

    js "Aye, the shiest little thing, moment Ron so much as jostled, it would be tugging at the leash to go."

    d "{i}*whines*{/i}"

    js "Oh, here come the dog walkers…"

    jump pond

label ask_bench_man:


    #Here the game should fade to black (done)
    scene bg bench with fade
    show rose blank at left with dissolve
    show jade sad l at center with dissolve
    show jasper at right with dissolve

    r "Uhm, excuse me, I-"

    d "Bark-bark-bark-bork!"

    j "Ah... good dog, nice dog…"

    js "Now look what you bloody done, Ron, hush up. Hang on a second."

    r "Sorry for disturbing your peace, we just needed to-"

    js "Rose! I thought I recognised that voice. Well, no wonder Ron got all excited. Never thought I’d see you out of the routes, unless this is some premium service I don’t know a thing ‘bout."

    r "Sorry, no package today, just enjoying the scenery."

    d "{i}*whines*{/i}"

    j "Actually, we’re looking for someone. You wouldn’t have happened to have seen anyone on this bench before you-"

    js "Don’t apologise for enjoying the fine scenery. Heck, the scenery’s why I’m here, just look at this view!"

    r "It is nice. Anything you can tell us?"

    j "An old lady?Possibly carrying some art supplies?"

    js "Sorry, lass, haven’t seen anyone else here for the past month. Especially with Ron, here, barking at his own shadow."
     

    scene bg bench
    show rose blank at left
    show jasper at right
    show jade very sad l at center with dissolve

    j "Hmm… sorry, I-I need a moment."

    r "Jade, can you get to the kiosk? I’ll join you in a minute."

    show jade sad l at center

    j "Wha’? Oh yeah, yeah. How could I forget? I’ll see to the ice cream, you take the big guy."

    show rose talking at left

    r "I’ll keep a brave face."

    j "Sweet scoops will be our rewards."

    scene bg bench
    show rose blank at left
    show jasper at right
    hide jade sad l with dissolve

    r "Please excuse my … friend, she seems quite shy around... I’m not sure what she’s feeling, as usual."

    js "Indeed, a funny friend you’ve found, how long you’ve known ‘em?"

    r "Just today. I’ll catch up with her. See you next round of post."

    js "Until then. Take care, Rose, and if you see that cat-walker, give ‘em my regards."

    show rose talking at left

    r "Cat?"

    js "Aye, the shiest little thing, moment Ron so much as jostled, it would be tugging at the leash to go."

    scene bg bench
    show rose blank at left
    show jasper at right
    show jade blank l at center  with dissolve

    j "I got the ice creams! And a lead. The ice-cream man remembered where Opal used to walk to."

    d "{i}*whines*{/i}"

    show jade sad l at center

    js "Ron, now, that’s not for you or me. Wait until we get back, there’s delicious beef back at - Oh, aye, here come the dog walkers…"

    jump pond

label pond:

    #POND SCENE 

    #Following both choices
    #Here the game should fade to black (done)
    scene bg park with fade
    show rose blank at left with dissolve
    show jade very sad at center with dissolve
    

    r "Hello dog, hello dog, hello dog…"

    j "..."

    r "The dogs have passed. Everything’s okay."

    j "..."

    r "Right?"

    j "Yeah… Well, actually {i}*inhales*{/i} Can I… have a minute?"

    r "S-sure."
    
    j "Over there? By the ducks?"

    r "If that is what helps."

    j "I think so."

    #Here the game should fade to black (done)

    scene bg pond with fade
    show rose blank at left with dissolve
    show jade very sad at center with dissolve

    play music "music/pond talk.mp3"

    j "She would have loved to live here. If she were here, geese would be flying…"

    r "Your dog?"

    j "Yeah… Me and my pooch… Libby."

    r "Nice?"

    j "The best. Considered herself more person than dog."

    r "Any tricks?"

    j "Like I said, thought herself more a person than a dog."

    r "Oh… How long ago?"

    j "...not sure anymore. A couple months. She was fifteen years old… I hope she’s somewhere nice now."

    r "She must have been well cared for. Isn’t that how it goes?"

    j "…like she was just falling asleep, ready to dream some good dreams."

    r "Then she must have had a great day."

    j "The best. Even with her aching joints, I moved her along like a wheel-barrow. In spite of the pains, her tail still wagged, I had bruises on my arms, but I didn't hold it against her, even as I held in the waters…"
    
    j "I could see the sky in her eyes… her own little vision of heaven."

    #JADE COLORS BLUE (done)
    show jade very sad at right, blue # will be in the doc, but adding this in case i forget somehow. choose the color put it after the location. so like how I did right, blue - Geneva
    show rose surprised at center
    
    r "Oh,  I… I can see you-I mean, your color. I-I’ve never seen a color before, it’s so…"

    #EMOTIONS - SADNESS 
    $ emotion_names.append("Sadness")
    $ emotion_colors.append("#4c68c2")
    show screen pencil

    show rose blank at center
    hide jade very sad
    show jad sad at right

    j "Oh, I noticed your glasses, but I thought it might be a sensitive topic {i}*sniffs*{/i}."

    r "Do you need a tissue?"

    j "Nah {i}*sniffs*{/i} I’m alright. Moment’s passed. Words were said, the pages turn {i}*inhales*{/i}, our quest continues."

    r "Right. In that direction."

    stop music fadeout 1.0
    hide jade sad
    hide screen pencil
    show jade blank at right

    j "And by the way, thanks for listening. More and more, you’re proving yourself to be friend material."

    r "Hm?" 

    show rose surprised at center
    show jade talking at right

    j "What is it? Did the big dogs scratch anything? Infection? Bleeding?"

    r "My pulse went up. So odd. Then again, we have been running a lot…"

    show jade blank at right

    j "Me especially, sorry about that."

    show rose talking at center

    r "No worries. Our quest goes on, at a reasonable pace…"

    j "Onwards, ever onwards towards… what's over there?"

    r "Train station."

    #JADE COLORS YELLOW

    show jade happy at right,yellow

    j "{i}*gasps*{/i} Trains? Trains? An adventure to span the lands!"

    #EMOTIONS MINIGAME - JOY
    $ emotion_names.append("Joy")
    $ emotion_colors.append("#f5e9ae")
    $ current_diary_page = 1
    show screen pencil
    r "We’ll see."


    #Here the game should fade to black (done)


    #ADD TRAIN SCENE 
    hide screen pencil
    scene bg jade train with Fade(0.5,0.0,0.5)
    pause 2.5

    #TRAIN STATION SCENE 


    scene bg train station with fade
    show rose angry at left with dissolve
    show jade surprised at right, violet with dissolve

    j "Oh my God. Oh my god… I almost… Oh my God…"

    #EMOTIONS MINIGAME - FEAR
    $ emotion_names.append("Fear")
    $ emotion_colors.append("#9f7bda")
    $ current_diary_page = 2
    show screen pencil

    j "Oh my God."

    j "I almost died to get this letter back, oh my God!"

    scene bg train station
    show rose angry at left
    show jade surprised at right, lightgreen

    j "Oh ground, I could kiss you if you weren't covered in feet!"


    #EMOTIONS MINIGAME - RELIEF
    $ emotion_names.append("Relief")
    $ emotion_colors.append("#7db877")
    $ current_diary_page = 3
    show screen pencil
    play sound "music/Rose Panic.mp3" # playing as a sound because it's a one off stinger
    r "{i}*gasping*{/i} What is - What is happening?"

    scene bg train station
    show rose angry at left
    show jade sad at center, purple

    j "Rose? Something up?"

    #EMOTIONS MINIGAME - WORRY
    $ emotion_names.append("Worry")
    $ emotion_colors.append("#bc7bda")
    $ current_diary_page = 4
    show screen pencil
    play music "music/rose hyperventilating.mp3"
    r "{i}Everything’s getting louder. Pulse is - Why am I… Why am I shaking so much?{/i}"

    j "Rose?"
    hide screen pencil
    r "{i}Like ants are crawling up and down my sleeves. So much sweat…{/i}"

    j "Rosie, are you okay?"

    r "{i}Please stop talking-{/i}"

    j "Rose, please, just answer me!"

    r "NO!"

    j "Okay, okay…"

    r "I’m - I’m sorry. My head, my chest - it feels like dough is on my ribcage and lungs. There’s no other trains coming, why is it getting so noisy?"

    j "It’s just a bit of an overload. Nothing to fear. There’s a bench not too far away, let’s get you there, can you still walk?"

    j "Now I see, that was a stupid question. One step at a time. There we go."

    r "Th-thank you, but still too loud."

    j "Way ahead of you. Brought a spare pair of these bad boys. Headphones. Fully charged up. Just put those on and -"

    stop music fadeout 1.5
    show rose blank at left

    r "They work…"

    show jade blank at center

    j "Like magic. Now, do you need a minute to yourself?"

    r "Only if you’re still here?"

    j "{i}*nods*{/i}"

    #Here the game should fade to black (done)

    #TRAIN STATION CLUES SCENE
    play music "music/Ice cream kiosk.mp3"
    scene bg train station with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    j "Well, aside from a couple of antique cars, nothing else for hints. The tracks run cold, least in the open. Appears we must bite the bullet, and see to the… ticket office."

    r "Okay…"

    j "Onwards!"

    r "And… thank you for your headphones. I never really tried headphones like these before."

    scene bg train station
    show rose blank at left
    show jade happy at center,yellow
    show screen pencil
    $ current_diary_page = 1
    j "They are wonderful, and think nothing of it."

    r "Despite my… stress."

    j "Believe me, I’ve been there, and I’ll gladly stay here with you."

    r "Hm…. Thank you again."
    hide screen pencil
    show jade blank at center

    j "Again, no worries."


    #Here the game should fade to black (done)
    

    #TICKET OFFICE SCENE 

    scene bg ticket office with fade
    show rose blank at left with dissolve
    show jade sad at center with dissolve

    j "Now then, here stands the ticket office, aaaand, it’s closed. Drag."

    show jade sad at center, darkgreen
    #EMOTIONS MINIGAME - Disappointment
    $ emotion_names.append("Disappointment")
    $ emotion_colors.append("#386134")
    $ current_diary_page = 5
    show screen pencil

    j "The track is well and truly cold as steel now."

    j "Well, at least we’ve got the painting, sure we could post it somewhere online and do these little search phenomena… but what’s the legality of that? Does everyone here go on social media?"

    show rose blank at left
    hide jade sad
    hide screen pencil
    show jade blank at center   #I see her darkgreen here for some reason??

    j "Guess we won’t know until we hit the information highway."

    r "Jade."

    j "Onwards towards a wifi hotspot!"

    show rose talking at left

    r "Jade, hold on. Look through the glass…"

    show jade talking at center

    j "Knick-knacks and assorted time-wasting tools? Oooooh, a newton’s cradle. And it’s still clacking!"

    r "And behind that, a newspaper clipping, an old one…"

    j "A clue?"

    r "Not per se, but potentially..."

    j "Exactly how so - oooooh. Our Opal’s been here a long time, hasn’t she?"

    show jade blank at center
    show rose blank at left

    r "And this town is small."

    j "So it’d stand to reason, she could’ve ended up on a newspaper, say, as a renowned artist respected amongst the towns?"

    show rose talking at left
    
    r "Exactly. Onward to the library!"

    j "Onwards!"

    #Here the game should fade to black (done)

    #LIBRARY SCENE 

    scene bg library with fade
    show rose blank at left with dissolve
    show jade blank at right with dissolve
    play music "music/cafe.mp3"
    r "Okay, the screen is on, and now, we just have to search by the-"

    v "{i}*cough*{/i}"

    r "By a few years, maybe a decade given her possible age-"

    v "Excuse me, whoever’s supposed to be at the desk, can you pleeeaaase get over here! {i}*burp*{/i}. I pay my taxes, I deserve some service here."

    scene bg library
    show rose blank at left
    show jade angry at right, red
    stop music fadeout 1.0
    #EMOTIONS MINIGAME - Annoyance
    $ emotion_names.append("Annoyance")
    $ emotion_colors.append("#c98484")
    $ current_diary_page = 6
    show screen pencil
    r "Everything okay?"

    j "Yeah, yeah."

    show rose talking at left

    r "You want me to tell them to be quiet?"

    j "No, no. I won’t sacrifice your nerves to that human migraine."

    r "We can come back later…"

    show jad very angry at right, red

    j "No times three to that. I can power through. {i}*fidgets*{/i}"

    show rose talking at left

    r "Are you certain? You appear upset."

    v "Don’t pretend I’m not here. I can see you in the back rooms. I can wait."
    hide screen pencil
    r "Doesn’t it hurt?"

    j "Like there’s a heated weight in my chest, working its way up to my shoulders, then my neck, until it’s like my brain’s replaced by a heavy rock, and I wanna throw it right at ‘em."

    r "Then what’s stopping you?"

    j "Why should I? What’s rampant flailing going to get me aside from a bad rep round town?"

    v "You ain’t better than the rest of us, you know. Everybody knocks on my door, but are too intimidated to stay. I’m respected, dammit!"

    r "But how do you stop the weight from crushing you?"

    j "Breathe, just breathe… let’s do it together."

    #BREATHING MINIGAME 
    jump stressed_breathing
    

label stressed_breathing:
    play music "music/rose hyperventilating.mp3"
    scene bg void with dissolve
    call screen stressed_breathing

label post_breathing:
    stop music fadeout 1.5
    scene bg library with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    j "Feel better?"

    r "I think."

    v "Don’t you close the door on me, I have a reputation to uphold. Know what, fine, I’m not coming here again. You lost a most valuable customer."

    j "And the lughead leaves."

    #Here the game should fade to black (done)

    scene bg library with fade
    show rose blank at left with dissolve
    show jade sad at center with dissolve

    r "Two decades back in time, nothing."

    j "{i}*sigh*{/i}"

    scene bg library
    show rose blank at left
    show jade sad at center, beige

    r "Something wrong?"

    j "I’m no good with the waiting game."

    r "Just be patient. The reward becomes sweeter with each passing day."

    j "Please let it not take days! I mean… You’re doing the heavy lifting at this stage, whilst I’m just here. I need to do something to fill in the spaces."

    r "Hmmm. I’ll be right back."

    j "Not too long, I hope."

    r "Okay, let me see…"
    play music "music/cafe.mp3"
    scene bg library
    show rose blank at left


    #CHOICE: Fantasy novel / Zoology book / Horror novel
    menu:
        "Fantasy novel":
            jump fantasynovel
        "Zoology book":
            jump zoologybook
        "Horror novel":
            jump horrornovel

label fantasynovel:
    #FANTASY NOVEL

    scene bg library
    show rose blank at left
    show jade blank at center

    r "Found this, not sure if it’s any good, it’s called-"

    j "I know that cover. The elvish brooding, the silver hair lost in the roaring winds of limbo..."

    show jade surprised at center, darkorange
    
    j "“Champions of the Infinite”!"

    #EMOTIONS MINIGAME - surprise 
    $ emotion_names.append("Surprise")
    $ emotion_colors.append("#eb985c")
    $ current_diary_page = 6
    show screen pencil

    r "Oh, you’ve read it, I’ll try another…"

    hide jade surprised
    show jade talking at center

    j "Don’t you dare. May I take a closer look? Just as I thought, an omnibus edition. Does it include? “Sails Across Destiny’s Seas”?"
    hide screen pencil
    show jade happy at center, yellow

    j "Yeeees!"

    r "Is that the one you’ve not read?"

    j "Read nine times, soon to be ten!"

    r "But if you’ve read it already, then why?"

    j "Because it’s great. The kind where you realise something new each time you look at it."

    j "Did Aelfreida truly know her nature as a Champion of Infinite? What if it’s all just one grand play by the Bolted Duchess to cope with the loss of her old life in the simulated providence?"

    j "I remember this one time, I was chatting with a friend of mine online about… about how, about how Libby was just like Eraint, the silver wolf."

    r "We can talk more about it once we’re done here."

    j "Deal. Expect plenty of lore on Ereint and their silver paw!"

    jump libraryclue

label zoologybook:
    #ZOOLOGY BOOK 

    scene bg library
    show rose blank at left
    show jade blank at center

    j "Rose, get a load of this critter, the “binturong”, it’s supposed to smell like popcorn, and it’s an ugly sort of cute."

    r "Remember the page for me as you move on-"

    show jade sad at center, blue

    j "{i}*slams book shut*{/i}"

    r "...!"

    j "... sorry, just got bored…"

    r "I’m sorry."

    j "What for? You didn’t know the following pages couldn’t beat the binturong factoid. I’ll see if there are any other zoological wonders about…"

    r "Don’t go too far."
    
    scene bg library
    show rose blank at left
    
    r "{i}*looks at binturong*{/i} It is kind of cute."

    show rose talking at left
    
    r "And on the next page… Canids… oh."

    jump libraryclue

label horrornovel:

    #HORROR NOVEL 

    scene bg library
    show rose blank at left
    show jade blank at center


    r "I found this, not sure if it’s your thing…"

    j "“The Midnight Lands”, oh, I heard great stuff about this one!"

    show jade happy at center, lightorange

    j "A friend of mine online said it had them leave the lights on for three nights straight!"

    #EMOTIONS MINIGAME - Anticipation 
    $ emotion_names.append("Anticipation")
    $ emotion_colors.append("#ecaa7a")
    $ current_diary_page = 7
    show screen pencil

    r "Are you sure? I can find something else…"

    j "Not in your life, this is my jam!"

    r "What about your friend?"

    show jade talking at center, lightorange

    j "To be fair, they’ll jump at anything spooky; they had a similar reaction to “Bear in the Machinery” and “The Poppy Bites”, which were nothing but a string of jumpscares, for me at least."

    j "Don’t get me wrong, I enjoy jumpscares, but only if they build it up juuust right: as you read each line, word for word, you spy the mark. You know they're behind the next page, listening, hearing the crisp fluttering of your heart and the page."

    j "You can’t stop yourself, as you turn it, and no matter how slowly, you’ll meet them on the other side… and then… Boo!"

    show rose talking at left
   
    r "OH! Please don’t do that again…"
    hide screen pencil

    hide jade talking
    show rose happy at left
    
    r "{i}*ahem*{/i} We’re still in the library."

    j "Sorry… got a bit ahead of myself… but, you are smiling?"

    show jade happy at center, yellow

    r "I am? Oh, I am… why?"

    j "The relief that it’s over, goodness how I love it."

    jump libraryclue

label libraryclue:
    #LIBRARY CLUE SCENE 
    #Following all three choices

    #Here the game should fade to black (done)
    scene bg library with fade
    show rose blank at left with dissolve
    show jade blank at right with dissolve


    j "Looks to have been a slow news day. That's pretty much everyday where I last lived, but with squirrels instead."

    r "It’s a small town. Been two years and people still talk about how the train broke down... Many theories. Anyway, look at the picture-"

    scene bg newspaper with Fade(0.5,0.0,0.5)
    pause 2.5

    scene bg library
    show rose blank at left
    show jade blank at right

    j "Aww, they’re covered in cheese and ham. Toasty."

    r "Beside the feline in cheeses and deli meats, does that look familiar to you?"
    
    if "Suprise" not in emotion_names:
        $ emotion_names.append("Surprise")
        $ emotion_colors.append("#eb985c")
        $ current_diary_page = 7
        show screen pencil

    show jade surprised at right, darkorange

    j "Opal’s Painting!"

    r "And that grocery store, I know where it’s located."

    hide jade surprised
    show jade blank at right

    j "And I’ve got the article on my phone camera. To the places where money can be exchanged for goods and services!"


    #Here the game should fade to black (done)


    #GROCERY STORE SCENE
    play music "music/grocery.mp3"
    scene bg grocery store with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    j "Alright, possibly second to last leg of the journey. One small step through these gates, and we are potentially golden."

    r "Stay focused. Look for old employees."

    show jade talking at center 

    j "Gotcha! My eyes will be coasting along every aisle for - look, they're selling mini cheesecakes!"

    r "..."

    j "I know, I know. Refocused, starting… NOW!"

    r "Appreciated."

    show employee at right

    e "Pardon me."

    show rose blank at left
    show jade blank l at center
    show employee at right

    j "Oh, goodness. Sorry, didn't mean to cause an uproar."

    e "Oh no, I was just going to say: there's whole cheesecakes on offer if you're interested."

    show jade surprised l at center, lightorange

    j "{i}*shakes*{/i} ooooh, thankyouthankyou!"

    hide jade surprised l
    show jade blank l at center

    e "Don't thank me, thank the blighter that mucked up storage. Several years, they're still finding ways in. Blast the nine lives of that blooming cat!"

    r  "...!"

    j "What is it? Oh… Ooooh. A cat. Any chance you’ve seen a cat like- like this one on my phone?"

    e "Well, I'll be battered. Spitting image and everything!"

    j "You must know Opal, then?"

    e "Opal? Oh ho ho, haven't heard that name in a dog’s age. Yes, yes, I know of Opal. Last one of the old guard, her and I. Surprised she's still kicking."

    j "Where exactly do her soles be flying?"

    e "Last I checked, not too far. Down Little Lane, can't miss the thing. And with that, I'll leave you, I've got shelves to restock."

    if "Anticipation" not in emotion_names:
        $ emotion_names.append("Anticipation")
        $ emotion_colors.append("#ecaa7a")
        $ current_diary_page = 8
        show screen pencil
    show jade happy l at center, lightorange
    show rose happy at left

    j "Rose!"

    r "Jade!"

    j "This Is It!"

    r "ONWARDS!"

    show jade surprised at center, darkorange

    j "Rose?!"

    r "Ah - Sorry, I'm sorry."

    show jade happy at center, yellow

    j "Don’t be. Let's turn that power to propulsion. Onwards!"

    r "Onwards!"

    stop music fadeout 1.5
    #Here the game should fade to black (done)

    #OUTSIDE OF PEARL'S HOME SCENE 

    scene bg pearl home with fade
    show rose blank at left with dissolve
    show jade blank at center with dissolve

    j "This is it, the final dungeon - I mean, final boss?"

    r "Final leg?"

    j "That’s it. The journey has been long and arduous, paved with conquered food, battlefield of escaped canines, the forest of books, and the ancient sage."

    j "Now, all that stands between us, is a door, thus our quest is complete."

    r "Would you care to knock?"

    j "Me? No, no, it must be you, it’s your call, your undelivered letter."

    r "A letter I would not have delivered without you. So please, give it a knock."

    show jade blank l at center

    j "Aye-aye. {i}*knock knock*{/i}"

    v "Hello?"

    r "Hello, we have something for Opal."

    v "O-Opal… I'm sorry but…"

    j "...! No…"

    show jade sad l at center, darkgreen

    v "I'm sorry, I do not know how you know her, but Opal has been gone for-"

    j "No… No, no, no, no…"


    v "I'm coming out. No! Don't go!"

    scene bg pearl home
    show rose very sad at left

    r "Jade!"
    
    r "Im sorry, ma'am, I'll be right back to explain."

    v "I didn't mean, oh, where are you running off to?"

    scene bg pearl home
    show rose very sad l at center  
    show jade angry at left, darkgreen

    r "Jade, please wait. This isn’t the end of the world."

    j "Nothing! It was all for nothing. Don’t you get it? We lost. Everything - meaningless. I-I almost died… I almost got run down by a train!"

    show jade very angry at left, darkgreen
    
    j "I nearly bit it on this stupid choice! All for your stupid letter of your stupid job!"

    r "Please, it isn’t over. It’s just- it’s just. {i}Heartbeat at my neck. Heat rising to my head. Remember, breathe.{/i} Just stupid… that, after everything, you’d call it that."

    r "This is not stupid, not the letter, not my job, not our choice to see this through. I have not regretted a single thing today. Even now, I can’t find a single feeling of regret. So please, don’t call it all stupid!"

    show jade very sad at left, lightblue
    #EMOTIONS MINIGAME - REMORSE
    $ emotion_names.append("Remorse")
    $ emotion_colors.append("#7ab9dd")
    $ current_diary_page = 8
    show screen pencil

    r "{i}*sighs*{/i}"

    show jade very sad l at left, lightblue

    j "Oh my goodness- what have I-? Rose, I am so sorry. I’m sorry, I’m sorry for being such a thoughtless- I’m sorry, I’m sorry, I’m sorry!"

  

    r "Jade, please, it’s alright. I know it sucks. But that’s just how it goes."

    show rose blank l at center

    j "But… why?"

    show rose talking l at center

    r "People pass away. People move on. Some things are just out of our control."

    show jade sad l at left, pink
    show rose blank l at center

    #EMOTIONS MINIGAME - SHAME
    $ emotion_names.append("Shame")
    $ emotion_colors.append("#f1b6de")
    $ current_diary_page = 9
    show screen pencil
    j "No, not that, {i}*sniffs*{/i} I’m someone you just met."

    show rose talking l at center

    r "You stayed with me at the train station. You helped me through the overload, you sacrificed your headphone’s full charge. Heck, you’re the one who got us on this adventure."

    r "Why would I leave this quest after such a small outburst?"

    show jade happy at left, gold
    #EMOTIONS MINIGAME - Gratefulness
    $ emotion_names.append("Gratefulness")
    $ emotion_colors.append("#ffce47")
    $ current_diary_page = 10
    show screen pencil

    j "Rose… I… You’re too good for me."

 
    r "It’s okay, let it out… is that you purring?!"

    j "What? {i}*laughs*{/i} I’m a dog person, not a cat person, and… uhm, Rose, look at your legs."

    hide screen pencil
   
    scene bg pearl home
    show cat at right
    show jade blank l at center
    show rose blank at left

    r "Hello cat. I think I know you from further up the road. So this is where you wandered off to."

    j "This is your kitty-cat?"

    r "No, no, but I used to see them from time to time, round your neighbourhood…"

    r "Hold on- come here, pspspsps, there we go. Little tufts at the side, strong headbutt to my palm. This is the one. Go on, try."

    j "You sure? They look fierce."

    r "Just don’t force the pet, let them do the work."

    scene bg pearl home
    show jade blank l at center
    show rose blank at left
    show pearl blank at right 

    ol "So this is where you wandered off to."

    r "Oh, my apologies, we were just admiring your kitty-cat."

    ol "She’s not mine, just an old acquaintance, so to speak. She just showed up the other day, scuttling about for a morsel of something."

    ol "I gave her a piece of steak and kidney pie and, next day, there she was, asking if she could have some more."

    j "Sounds like a handful."

    ol "Hardly! When you’ve dealt with a hellraiser like mine, even the toughest tabby is a catwalk on a cakewalk. Dear, I hope I’m not taking time away from your work."

    r "Just finished today, actually."

    show jade talking l at center

    j "And besides, we could do with a bit of a chuckle. What kind of Hell did they raise?"

    ol "All sorts. She’d be darting across the room. Jumping onto my old projects, just as I’d finished stitching up the last time she wounded them in battle."

    show jade blank l at center
    
    ol "She’d be my shadow, but the next moment I turned around, she’d practically leap so high in shock, we’d see eye to eye. At times, part of me wonders if she still thought we were at the shop."

    r "Shop, like the grocery store?"

    ol "That’s right. Oh I fought tooth and nail to get her down from the shelves. Now that I think about it… That’s how we first met."

    ol "Needed the extra job to buy new supplies - I was close to painting on grease paper over a placemat."

    ol "Honestly, I was raking in just enough for canvas. But alas, nothing to show for it… I had sent out dozens of submissions, but at that point, I couldn’t even muster a paintstroke."

    ol "One day, I’m carrying this basket of cookies and biscuits and cakes, when I hear something. Meowing? I try to ignore it, thinking it a betrayal of the senses, a crumb of cheese and all that."
    
    ol "But I hear it again, mewling. Finally, I get some of my co-workers. Nothing. Slowly, we look up, and there, where corners’ cross, a pair of shiny eyes."

    ol "From the shelves, sacks of flour flew, sugar pelted like sand falls with waterfalls of milk and juice."

    r "Woah..."
    
    ol "As everything calmed down, and everyone had quieted down after the chase, we all looked at the culprit. We were ready to swing them out the window, glass be darned. I myself volunteered to do the deed. At least, until I saw it."

    r "What?"

    ol "That spark in her eyes, like staring into the northern lights. So much soul, in so frail a little creature."

    ol "In that light, they struck me: that courage for freedom, and yet, at the same time, if I didn’t take care of her, who would? And so, well, I don’t know how, but the next minute, I quit the shop, marching out with a cat in arms."

    ol "Oh the ribbing I got afterwards, “Trading a good job for a little bit of fur, you must be mad”, well, cut off my ears and call me Van Gogh, cause I was unstoppable: hours without slumber, days painting, all thanks to my muse. Then... She was gone."

    show jade sad l at center
    
    j "I’m sorry. We didn’t mean to open up old wounds, there."

    ol "Quite alright… Just… if only I hadn’t lost her painting… my cat with her dazzling coat…"

    show jade talking l at center

    j "Wait… are you the Opal on this canvas? {i}*shows phone*{/i}"

    ol "Oh my, where was that?"

    show rose talking at left

    r "In your previous residence. Now, apologies for our bluntness, but are you indeed Opal?"

    ol "My goodness, no, Opal was my inspiration. I’m-"

    show jade surprised l at center, darkorange
    show rose surprised at left

    j "PEARL!?"

    p "Goodness!"

    r "I’m sorry, forgive our volume, but… I - we…"

    j "It has been quite a day…"

    hide jade surprised l
    show jade blank l at center 
    show rose blank at left

    p "I searched high and low for that painting amidst the moving boxes. I'm surprised you managed to find me with just that."

    r "There was also your painting in the cafè."

    show jade talking l at center

    j "And I nearly got hit by a train."

    p "My word, it sounds like it’s been quite a day, indeed."

    r "So, your letter."

    p "Ah yes, the macguffin which started your little quest."

    j "Can we watch you open it?"

    r "...?"

    j "We’ve spent so long with it. I can’t live my life not knowing."

    p "It is only fair, then. Let me preface, however, it may well just be rubbish: a coupon for a car I don’t have, a subscription, or goodness forbid, a brochure for some cockamamy - !"

    show pearl rainbow troubled at right 
    play music "music/pond talk.mp3"
    show jade sad l at center

    r "Something wrong?"

    p "Acceptance…"

    j "Of what?"

    p "Art school."

    j "Oh!"

    show rose talking at left

    r "That was what the submissions were for…"

    p "All this time… I-I… everything - The hours… the first piece Opal inspired… Oh, if she were here now!"

    r "Ma'm, are you alright?"

    p "And what if it's too late? What if I fail? Oh, I've been dreaming about this for so long, I can't believe it!"

    show rose sad at left
    show jade talking at center

    j "What about you, Rose? Your eyes are running a storm."

    r "Hm? So they are. May I trouble you for a tissue?"

    j "Got you covered."

    p "{i}*chuckles*{/i} She’d be mewling for dinner. That's what she'd do."

    c "{i}*meow*{/i}"

    p "And you, Amber, all the work you'll be subject to in the coming days. And you two, thank you, bless you. Thank you and bless you for reigniting that spark!"
    stop music fadeout 1.0

    #Here the game should fade to black  (done)
    play music "music/mail delivering.mp3"
    scene bg jade home outside with fade
    show rose blank at left with dissolve
    show jade happy at center, yellow with dissolve

    r "Well… I guess that’s our quest done." 
    
    r "...see you on the next delivery route?"

    j "Oh ho ho no, you’re not getting away that easily."

    r "Hm?"

    j "Today’s adventure may be over, but there’s no chance I’m letting that be the only one with you."

    j "I’ve been here for only a couple months, but not once, not once, has someone really drawn me out to the sights."
    
    j "I’m sorry, Rosie, but you're officially my muse."

    show rose talking at left

    r "I-I’ve been here my whole life, but-I’ve never had someone to show the sights to."

    r "I have work in the morning, though."

    j "Then we make it lunch. Like I said, Rosie, I’m all in for this. Deal?"

    show rose blank at left

    r "...deal."

    j "And I’m paying. Well, I’ll be seeing you tomorrow then, on the dot, and that’s a promise, cause that’s what friends do."

    show rose happy at left, yellow

    r "...that's what friends do..."



    # This ends the game.

    return

# silly test thing by geneva below
label gwee:
    "gweeee"
    "My count is [currentCount]"