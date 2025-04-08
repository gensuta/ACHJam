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

    scene bg mistery

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
    #Here should be the first fading 

   
    scene bg mistery
    show rose blank at left 
    show mistery man at right 

    m "How are the glasses? Anything?"

    r "...nothing different."

    m "Well, that’s never happened before… these glasses are the gold standard for emotional blindness."

    m "In any case, keep them on at all times, I’m sure you just need to get used to them and they’ll start working soon."


    # TOWN SCENE 

    #GENEVA
    #Is it possible to somehow show that she's thinking and not talking? Having the text in italic for example?

    scene bg mistery
    show rose blank at center 

    r "It’s been three months, but my world hasn’t changed."

    r "I still don’t know what it means to see a color…"

    r "… and I have no idea how I’m feeling most of the time."

    r "But I know I’m good at my job and, although it might seem boring or lonely on the outside, I think it suits me."



    #JADE'S HOUSE SCENE (OUTSIDE)

    scene bg mistery
    show rose blank at left

    r "Strange… it looks like the name doesn’t match the resident."


    #GENEVA 
    #CHOICE: Sound the doorbell / Leave the letter in the mailbox anyway


    #SOUND THE DOORBELL 

    scene bg mistery
    show rose blank at left

    v "Hello? Ah, hold on, don't leave just yet!"

    r "I haven’t moved."

    v "Okay, I’m nearly at the door-"


    #LEAVE THE LETTER IN THE MAILBOX

    scene bg mistery
    show rose blank at left

    r "Well… It's addressed to here. They can sort it out."

    show jade blank at right

    j "Miss? Excuse me, Miss?"


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


    #ASK THE NEIGHBOUR AS FIRST CHOICE 

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




    #JADE'S APARTMENT AS FIRST CHOICE

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






    












    #PARK SCENE 

    scene bg park

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show rose blank

    # These display lines of dialogue.

    r "Excuse us?"
    r "P-pardon?"


    # This ends the game.

    return


label gwee:
    "gweeee"
    "My count is [currentCount]"