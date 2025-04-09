# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rose")
define j = Character("Jade")
define i = Character("Ice-cream man")

define v = Character("Voice")


define m = Character("Mistery man")
# To be deleted when actual character sprites are ready


# The variables below are for minigames! Please ignore and do not touch!! -Geneva
default currentCount = 0 
default isDistracted = False

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

# The game starts here.


label start:


    #OPTOMETRY CLINIC SCENE

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg optometry

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show rose ng at left
    show mistery man at right

    # These display lines of dialogue.

    m "Okay, we’re almost done with the optometric evaluation. Now look at me. What do you see?"

    r "Everything’s still in black and white, as it’s always been."

    m "Well, this confirms it then, emotional blindness."

    r "What does it mean?"

    m "As you know… although not from experience, given your condition… human beings express their emotions through coloration changes." 
    
    m "So, if you see a person coloring yellow you know they’re… well, I guess you wouldn’t know, would you?"

    r "..."

    m "Challenges in recognizing, expressing, feeling and describing emotions are all symptoms of emotional blindness."

    m "That’s where the glasses come in, they’re designed to help people with your condition see colors, your own as well as other people’s."

    m "Recognizing emotions will also help you flexibly respond to your own emotional states and will improve your interactions with others."

    #GENEVA 
    #Here the game should fade to black 

   
    scene bg optometry
    show rose blank at left 
    show mistery man at right 

    m "How are the glasses? Anything?"

    r "...nothing different."

    m "Well, that’s never happened before… these glasses are the gold standard for emotional blindness."

    m "In any case, keep them on at all times, I’m sure you just need to get used to them and they’ll start working soon."


    #Here the game should fade to black 


    # TOWN SCENE 

    #GENEVA
    #Is it possible to somehow show that she's thinking and not talking? Having the text in italic for example?

    scene bg mistery
    show rose blank at center 

    r "It’s been three months, but my world hasn’t changed."

    r "I still don’t know what it means to see a color…"

    r "… and I have no idea how I’m feeling most of the time."

    r "But I know I’m good at my job and, although it might seem boring or lonely on the outside, I think it suits me."


    #Here the game should fade to black 


    #JADE'S HOUSE SCENE (OUTSIDE)

    scene bg mistery
    show rose blank at left

    r "Strange… it looks like the name doesn’t match the resident."


    #CHOICE: Sound the doorbell / Leave the letter in the mailbox anyway

    #Here the game should fade to black 


    #SOUND THE DOORBELL 

    "Choose to sound the doorbell"


    scene bg mistery
    show rose blank at left

    v "Hello? Ah, hold on, don't leave just yet!"

    r "I haven’t moved."

    v "Okay, I’m nearly at the door-"


    #Here the game should fade to black 


    #LEAVE THE LETTER IN THE MAILBOX

    "Choose to leave the letter in the mailbox"

    scene bg mistery
    show rose blank at left

    r "Well… It's addressed to here. They can sort it out."

    show jade blank at right

    j "Miss? Excuse me, Miss?"


    #Here the game should fade to black 


    #JADE'S HOUSE SCENE 2 (OUTSIDE) 
    #Following both choices

    scene bg mistery
    show rose blank at left
    show jade blank at center

    j "Hello, forgive my lateness, I had headphones on."

    r "Only been a few seconds. Anyway, I have a letter-"

    j "Oh, wow. It's all gilded and yellow. It would be a crime to tear it open."

    r "Please, hold on a second-"

    j "Still, there's stuff unopened, maybe mum put my letter opener in there…"

    r "No, no. It's not your letter- I mean, this letter is addressed to the previous occupant, one “Pearl” at this address."

    j "Hm? Oh… Oh my goodness, I am so sorry! Almost committed a crime. I could go to jail!"

    r "It's fine…"

    j "Fine? I can pay for that. How much, ten? Twenty?"

    r "It is fine. Synonymous with “alright”. No crime committed. Now, by chance, do you know their current location?"

    j "Uhm…"

    r "No, then?"

    j "Yes to the no."

    r "Very well. Undelivered it is."

    j "What now? You've got computers for this?"

    r "Only cabinets. Full of paperwork."

    j "Wait-wait. I can help, I can help!"

    r "...?"

    j "Ah. Uh… Ah! It's only been a month since I got here. Nooks and crannies yet to clean - especially the cupboards -,  maybe a clue might be lying about in the apartment."

    r "Clue?"

    j "You know, old pamphlets to locales or-or childhood photos of happy places… oooooh I can smell the adventure. Let's have a look around!"

    r "I might just ask neighbours…"

    j "That too! I can take notes. I've a pen and paper on my desk. Oh, and I'm Jade, BTW, but you probably already know, with the name at the door."

    r "Rose… good to meet you."


    #CHOICE: Ask the neihgbour / Look inside Jade's apartment for clues 

    #Here the game should fade to black 


    #ASK THE NEIGHBOUR AS FIRST CHOICE 

    "Choose to ask the neighbour"

    scene bg mistery
    show rose blank at left
    show jade blank l at center

    j "Excuse me. Hello? Anyone there?"

    v "Don't you dare knock again. I just got the little blighter down for his nap."

    r "Noted. And it’s me-"

    v "Oh, it’s you. You're a day early, this time. Did Lily have something going on?"

    r "No care package today, I don’t know what Lily is up to. Can we ask some questions?"

    j "Forgive her rudeness, we’re just here to sort something out. Something to do with your old neighbour - I’m your new neighbour by the way, Jade, but yeah."

    v "Alright, alright, very pleased to meet you. Now, you were saying…"

    r "Sorry, no care package delivery today. Your calorie count remains true. As she has said, we need a word about your old neighbour."

    v "Old neighbour… ah, who was it? Darned if I can remember their name."

    r "Anything you can tell us…"

    v "She was one of those artist types I think, you know. Always in something she made herself. Once tried talking to ‘er, but she disappeared just round the corner. It was a lovely outfit out of an old duvet cover, pair of shades glimmering just like that stone… What was it? Found at the sea - Opal, that was her name."

    r "It says “Pearl” on the letter."

    j "Maybe it’s like my mum and my big bro’s letters. He’s in Korea, South Korea, and his letters still arrive at mum’s house. Right? So maybe this Opal could be a clue to reaching Pearl?"

    r "Any idea where Opal could be?"

    v "Last I saw, she was down by the cafè. If that's all you need of me, then good luck with you. I think I hear him start to stir."

    j "Artist... hmm."

    r "Another lead?"

    j "I believe so, leading right back home…"

    #Here the game should fade to black 

    scene bg mistery
    show rose blank at left
    show jade blank at right

    j "The moment I heard “artist”, it hit me, just like that! Right against the back of the cupboard…"

    r "Lots of other stuff from the old tenant."

    j "No… that’s me."

    r "A lot of worn down baseballs. Were you an athlete?"

    j "No, just holding onto them for a friend. Ah, here we are."

    r "It’s nice. Such a cute cat."

    j "Indeed, indeed, but look at the signature in the corner."

    r "Opal… But I thought Pearl lived here?"

    j "Maybe it was a gift, or a personal commission. But the bottom line is clear: we find Opal, we find Pearl."

    r "How certain are you?"

    j "Roughly ninety-percent, as sure as the shape of my eyes."

    r "If you say so. We could take this, in case anyone has seen this work."

    j "And click. Onto the phone, and the weight of a canvas off our shoulders."

    #Here the game should fade to black 



    #JADE'S APARTMENT AS FIRST CHOICE

    "Choose to look inside Jade's apartment for clues"


    scene bg mistery
    show rose blank at left
    show jade blank at right

    j "Come on, where are you? I know you’re stocked up somewhere…"

    r "Very… organised."

    j "Hardly, most of it is taking refuge in my bedroom. Open the door and we’d be buried in a landslide of books and - ah ha! Got you, and... behold."

    r "A painting. Of a cat."

    j "Indeed, and what can you see on it?"

    r "... brush strokes?"

    j "Uhm, yes. But, beyond the brush, we may find - pause for effect - a name!"

    r "It says “Opal” not “Pearl”."

    j "True, but it was found INSIDE of Pearl’s old home. Which means, a connection."

    r "What kind, though?"

    j "Hm. That, we need to find out. Any ideas, partner?"

    r "Partner?"

    j "Yeah, partners, solving a mystery!"
    
    r "We could try the neighbour next door?"

    j "Excellent. Click! And a photo of the portrait for the road. Can’t have us lugging that precious article around town with a risk of rain or breaking."

    r "Clever."

    j "Ah, thank you. Now, onwards!"

    #Here the game should fade to black 


    scene bg mistery
    show rose blank at left
    show jade blank l at center

    r "Best you let me sort this one out. They prefer a certain way of alerting them."

    r "*whistles like a bird*"

    v "Ah, you’re early this week. Any news of Lily’s care package?"

    r "No care package, only a question. If you could look through the peep-hole…"

    v "My eye is up here. Ha ha. Oh, you’ve got a partner in crime I see."

    r "No, still working solo."

    j "Oh, hello, I’m Jade - your new neighbour - and uhm, tell us, do you know anything about who painted - hold on just, got to unlock my phone - who painted this?"

    v "Hmmm, I think I recognise the style - wait, Opal? I hadn’t realised she actually left."

    j "I just told you I’m your new neighbour."

    r "But the letter said “Pearl”, not “Opal”."

    j "Maybe it’s like my mum and my big bro’s letters. He’s in South Korea, and his letters still arrive at mum’s house. Right? So Opal could still be a clue in reaching Pearl?"

    r "I suppose… any idea where Opal could be?"

    v "Last I saw, she was down by the cafè. Well, either way, best of luck to you two."

    r "Thank you."

    j "So what do ya’ think?"

    r "Of what?"

    j "Opal giving the painting to Pearl."

    r "Was the painting a gift?"

    j "I like to think so. A parting present, of memories shared, a moment crystallised into an immortal image."

    r "Of a cat?"

    j "For that was the shape of Pearl’s soul to Opal."

    r "You’re just making this up, aren’t you?"

    j "Well, we need some dramatics in this quest."

    #Here the game should fade to black 



    #CAFE SCENE 

    scene bg mistery
    show rose blank at left
    show jade blank at center


    j "What a cosy little place."

    r "It is."

    j "You come here often?"

    r "Yes."

    j "Well then, mind me seeing what the town has to offer?"

    r "No, thank you, we’ve got the painting to find-"

    r "*stomach growls*"

    j "We can talk about that over lunch, on me!"

    r "They work by table numbers. Remember the number, walk up to the counter, and place your order."

    j "I appreciate the clarity."

    r "They have pictures on the menus too."

    j "“I meant… actually, oh, this is actually a good spread: jewelled salad, chicken noodle soup with croutons - steak and kidney pie with fries and gravy!? I’ve not had that in ages. We’ve got to have some."

    r "No thank you? Not my favourite dish."

    j "Hmmm, alright then, what’s your favourite?"

    r "Homemade burger with coleslaw."

    j "And it’s got a special side of onion rings and curly fries. That is awesome!"

    r "Is it?"

    j "...is everything okay? Oh heck, is this about something I did?"

    r "Not your fault."

    j "Then what?"

    r "Nothing, really. I’m just not a talkative person."

    j "...okay. Looks like a pretty big line. I ain’t standing for minutes on end just fidgeting, so..."

    j "... seen any good shows? Blergh, so cliche a starter…"

    r "I recently watched “Tower of Phantometer” cutscenes online, if that counts."

    j "Phantometer? Oh, yeah, the videogame? With the cute critter in the armour?"

    r "Action-Platformer where you played as Luna. Ascending up the Tower of Phantometer to reach the stars, in the hope that one of them is the spirit of her loved one, whose identity depended upon the questions you answered at the start."

    j "Yeah… that one."

    r "Watched playthroughs of it when I was younger. The music helped me sleep. Story was well-written. Still holds up. Still wish I could play it. Too expensive then, too rare now."

    j "“I’ve got a copy!"

    r "Hmm?"

    j "Yeah, original manual and everything. If ever you have a day off..."

    r "Thank you."

    j "Huh, with all those details, I’d figured you’d be more… ecstatic."

    r "Ecstatic?"

    j "A chance at playing that game that eluded your grasp, isn’t that exciting?"

    r "I’m not sure…"

    j "When I’m excited about something, I can’t stop talking about it. I can’t even sit still, it’s like-too much for my body to hold, if that makes sense?"

    r "I guess-I guess I did feel something, when we were talking about Phantometer. A weird sensation in my chest. My heart beating faster? I’m just never sure if it means I’m excited or nervous… and I’d rather not think about it right now."

    j "Well, to be fair, we got other fish to fry, so no need to dwell. And speaking of food, looks like the line’s shortened. Figured out your order?"


    #Here the game should fade to black 

    
    #CHOICE: Safe food/New food

    "Choose the safe food"


    #SAFE FOOD

    scene bg mistery
    show rose blank at left
    show jade blank at center

    r "Double burger with coleslaw, please."

    j "Stick to what you know, fair enough."

    #Here the game should fade to black 

    j "He he he. Now look at the golden flakiness of that pastry. It feels like a crime to tear it open. How about your burger?"

    r "It’s well put together."

    j "Well put together?!. That wooden stake is keeping that monster in check. You got to slay it before it falls apart!"

    r "Not until the fries are eaten with the coleslaw."

    j "Okay, but you’ll be way behind once I’ve cleaned the gravy from the plate."

    j "Oh, blimey, need a breather. But I ain’t getting defeated by beef. You with me?"

    r "Beef defeated."

    j "Holy! That was fast. Are you sure you had time to chew?"

    r "You sound like my granddad. He said he’d always buy me a burger."

    j "Sounds like a good grandpa."

    r "Joked he only did so to see if I unhinged my jaw before I ate. I’d hiss every time I saw him. People stared. But granddad always smiled. Wasn’t sure if he actually found it funny."

    j "You must hold those memories very dear."

    r "It does feel good to revive them. I feel… calmer, somehow."
    
    j "I get it. And my grandpa always bought me lunch too, even if I had the cash. He and I would buy the cheapest thing the cafe had *chuckles* I’ll give you three guesses."

    r "Hm…"

    j "It’s literally served on a platter for you."

    r "No, not the pie and fries?"

    r "Wait-Look behind you. Actually, could you get your phone out?"

    #Here the game should fade to black 


    #NEW FOOD

    "Choose to try a new food"

    scene bg mistery
    show rose blank at left
    show jade blank at center

    r "I’ll have what you’re having."

    j "Prepare for a wonderful food sensation!"

    #Here the game should fade to black 

    j "So… how is it?"

    r "It’s nice."

    j "That’s all?"

    r "Is that not all there is to it?"

    j "But what about- what about the smell? The sound? Heck, have you even smelt it?"

    r "It smells… warm."

    j "“Warm”? Nothing more? Fine. Let's start with the finer points of pie enjoyment. Take your fries - or chips, as they’re known in some places - onto your fork."

    r "Okay…"

    j "Now, with the knife in hand, get all that beautiful gravy onto the fork. Yep, good, good. And finally, top with a piece of the pastry."

    r "M-okay"

    j "Now let it settle on the palate. The golden flakes drawing in the other flavours like a sponge. How easily it binds together with the carrots and peas, further sweetened by the jamminess of the onions."

    r "..."

    j "And what of the chips? Can you feel the texture, the once salt-crispiness, now melting away within the gravy, a gentle cloudiness at the tongue. The warmth of the meal, it descends like a comet into your stomach, turning it into a furnace and - eh he he, got carried away there, didn’t I?"

    r "A bit."

    j "I just think some experiences need to be savored, right? You never know how happy you are until you truly pay attention to it."

    j "Plus focusing on what I enjoy helps me block out the stuff that annoys me. Like this godawful smell, for example! What do you think it is?"

    r "Hmm, maybe… vinegar?"

    j "Ugh. Anyway, I used to take cooking classes with my friends... The chef was always like that. The “poet” sort of cook, but their enthusiasm was so contagious I-"

    r "I’m sorry to interrupt, but does that look familiar to you?"



    #THE PAINTING 

    scene bg mistery
    show rose blank at left
    show jade blank l at center

    j "Is that…?"

    r "Opal’s cat."

    j "Only now it’s staring lovingly at a sunset."

    r "It looks familiar."

    j "Certainly evokes post-impressionism, especially the focus on light."

    r "The way the sunlight goes through it."

    j "Definitely an early attempt at the style. Sorry, I took some classes, and it’s so rare I get to talk shop on art history, especially around-"

    r "The bench!"

    j "What bench!?"

    r "In the park."

    j "The park in town?"

    r "The park in town."

    j "How far is it?"

    r "Just across the road."

    j "Ready to go?"




    #PARK SCENE 

    scene bg park
    show rose blank at left
    show jade blank at right


    j "Should we ask somebody if they remember seeing our mystery lady around here?"
   
    r "Hmm, I know that dog…"

    j "Uh, right,  well… the ice-cream man looks like a more promising lead to me. Being at the park all the time and all."


    #CHOICE: Ask the ice-cream man / Ask the man on the bench


    "You choose to ask the ice-cream man"


    scene bg icecream
    show rose blank at left
    show jade blank l at center
    show icecream man at right

    r "Excuse us?"

    i "Oh, it's you, we finally meet."

    r "P-pardon?"

    i "Haven’t seen you in a while, I was beginning to worry about you."

    j "Hang on, hang on. Rosie, you know this person?"

    i "Hm? Ah, my mistake, but the way you were standing there… no… you’re definitely much younger and taller than her… must be the clothes. I’m sorry, just a bit of rambling on my part. Hope you have a good day."

    j "We haven’t even asked yet."

    i "Oh right, one scoop or two?"

    j "We mean… uhm, Rosie, you want anything?"

    r "*nods and holds up two fingers*"

    j "Very well. Good sir, we shall take two of the finest scoops of your ice cream. In exchange, mind telling us of “Opal” and her bench-sitting ways?"

    i "Opal? So that was her name. Truth be told, we never actually talked. She’d be sitting right there on the bench. But on the dot, every day before the walkers came round. I could time my work hours just by her presence alone. My human timepiece, ha. At least, that was how it was until a few weeks ago. Then she was gone, and her little cat, too."

    r "Cat?"

    j "Just like in the picture. Any other notable features? Hair colour, hair style, facial features, maybe a cool iconic item?"

    i "Mmm, unfortunately none spring to mind. She was well covered for winter, no matter the season. Honestly I’m surprised she didn’t melt."

    j "Dang. Guess we’re back to square one, then."

    r "Not yet. Did Opal always leave the park the same way?"

    i "Off towards that direction, right to the –"

    j "The bench!"

    i "Yes, in that general direction…"


    #Here the game fades to black

    scene bg bench
    show rose blank at left
    show jade blank l at center
    show mystery man at right

    r "Uhm, excuse me, I-"




    # This ends the game.

    return


label gwee:
    "gweeee"
    "My count is [currentCount]"