# Character declarations

define d = Character("Damien")
define y = Character("[name]")

# The game starts here.

label start:

    # Variable declarations
    $ damien_approval = 0
    $ aggressive = 0

    "Content Warning: This narrative includes explicit discussion of death and its various causes."
    
    "Specifically, this text includes descriptions of accidental death, death by natural causes, and violent death."

    "These descriptions are relatively brief and are not graphic."
    
    "If you would like to avoid these descriptions, then when asked about your character's death, simply decline to answer in any way that feels appropriate for your character. This decision will not lock you out of any endings."

    python:

        name = renpy.input("What is your name?", default = "ghost")
        name = name.strip()

    # Placeholder bg.
    scene bg room 

    "You stand in front of the house, a twisted mass of graying wood, leaning precariously to one side. No place has ever screamed 'haunted' quite as loudly – it almost feels a bit on the nose."

    "At least you don't have to worry about being injured when the 'absolutely-should-be-condemned' building finally collapses. Though, you suppose, when that does happen, you and your new roommates will have to find another place."

    "And that's assuming you pass this interview. How are you feeling just before the big event?"

    menu:

        "Frustrated. (Aggressive)":
            jump intro_aggressive
        
        "Uneasy. (Nervous)":
            jump intro_nervous

        "Relaxed. (Confident)":
            jump intro_confident

        "Excited! (Cheerful)":
            jump intro_cheerful
    
label intro_aggressive:

    $ aggressive += 1

    "This whole situation is just... frustrating. There's only a handful of safe places in this city to haunt and they're all scooped up by groups of ghosts like this one. Now you have to 'prove' to this guy that you're worthy of living in his broken down mansion."

    "You are certainly not relishing in the idea of an afternoon spent being dissected and judged before having someone else decide whether you're decent enough to have a place to stay."

    "Still, being hauntless is... not an option. And at least this Damien guy was willing to hear you out, to even consider letting you move in. Several of the other haunted places had very territorial tenants."

    jump intro_2

label intro_nervous:

    "You can feel your nervousness in your body – or, well, whatever the ghost equivalent of a body is."

    "This is just like every other job interview, college interview, or apartment interview you had ever had to do when you were alive. The whole process is just one excruciating exercise in being seen with the added worry of saying the wrong thing."

    "'Selling yourself' has never been your strong suit."

    "Still, being hauntless is... not an option. And at least this Damien guy was willing to hear you out, to even consider letting you move in. Several of the other haunted places had very territorial tenants."

    jump intro_2

label intro_confident:

    "Despite some of the uncomfortable aspects of this situation, you feel relatively unfazed. This is simply something you have to do – a necessary step on the path to getting a safe place to stay in perpetuity. No more, no less."

    "Besides, your chances are looking quite good. You're lucky to have found this place, and luckier still that the keeper is willing to speak to you and potentially let you move in."
    
    "You feel confident that that luck will continue."

    jump intro_2

label intro_cheerful:

    "You haven't really had many opportunities to meet new people since you died, so the chance to talk to the keeper and potentially meet your housemates for eternity has you ecstatic."

    "You're lucky to have found this place, and luckier still that the keeper is willing to speak to you and potentially let you move in."

    "At this point, living here is all but a sure thing – you're a people person after all."

    jump intro_2

label intro_2:

    "You walk up to the door and reach out a hand to knock... and your arm passes right through."

    "Right. Dead. Should you just go in? Or would that be rude?"

    "Before you ponder that question too much, a tall figure in a moth-eaten charcoal suit steps through the door."

    "He's gaunt, tan skin and dark hair, with eyes that never seem quite fully focused."
    
    "Still, he looks like he died quite young. You wonder how long ago that was."

    d "Ah, I see you've found your way back here."

    "His voice is all too reminiscent of a creaking door hinge."

    "Damien, the self proclaimed 'Keeper' of this haunted mansion. You've met him only once before, when you first found this place."

    "It was him who suggested you come back today to interview for one of the open rooms in the house. It seems like he will be conducting the interview."

    d "Please, come inside."

    "He gestures for you to follow as he walks backwards through the door."

    "You follow – albeit reluctantly as you still haven't quite adjusted to walking through solid objects – and find yourself inside the manor."

    "For how rundown the place looks on the outside, it's actually quite well maintained."

    "You have no idea how they managed to keep it that way; no matter how hard you tried you hadn't been able to so much as hold a broom much less clean a massive house."

    "You turn to find Damien already sitting at a small tea table off to the right of the entryway."
    
    "You walk over to join him, before hesitantly starting to phase through the legs of the table and the armrest of the chair to try and sit."
    
    "Damien seems to notice your hesitancy."

    d "You won't fall. For some reason the only direction we can't phase is down."
    
    "True to his word, you managed to take a seat, straightening your posture after recovering from the awkward endeavor of sitting in a chair you could not feel."
    
    "You look at him expectantly. It's time for the interview to begin."

    d "As you know, this house is already haunted." 
    
    d "We have half a dozen spirits residing here already, and while there is plenty of room in this place for more, it is my job as keeper to ensure the safety of all who dwell here."
    
    d "To do that, I have devised this interview to see if you would be a good fit for the house."
    
    d "There are only a few questions. Are you ready to begin?"

    y "Alright, what would you like to know?"

    "Immediately, without missing a beat or shifting his decidedly neutral expression in the slightest, he pulls out a small journal and asks..."
    
    d "How did you die?"

    menu:
    
        "\"Absolutely not.\" (Aggressive)":
            jump q1_aggressive

        "\"Wha- I mean... is that really necessary?\" (Nervous)":
            $ damien_approval += 1
            jump q1_nervous

        "Tell him. (Confident)":
            $ damien_approval += 1
            jump q1_answer

        "\"Well, at least buy me dinner first.\" (Cheerful)":
            $ damien_approval += 1
            jump q1_cheerful

label q1_aggressive:

    $ aggressive += 1

    y "That information is mine, and mine alone. I will not have the circumstances of my death determine the entire course of my unlife."

    "You can feel your fist shaking as they are clenched in your lap."

    "Damien looks taken aback, and far more animated than you've seen him so far."

    "It seems he wasn't expecting that reaction. He should have been."

    d "I... I apologize. I meant no offense." 
    
    "Damien stammers, looking around uncomfortably."

    "The silence stretches on for just a moment too long. Finally, the keeper speaks up again."

    d "Let's just... move on with the interview." 
    
    "You nod tersely, feeling the muscles already stiff in your neck from the tension. Who knew ghosts could get stiff muscles?"

    jump q2


label q1_nervous:

    "Why was he asking you this? Were ghosts different based on how they died? Were only certain types allowed here?"

    "What if you couldn't remember how you died? Or was this just an \"everyone who lives here has to have a super exciting murder,\" type situation?"

    d "Ah,"
    
    "Damien miles sympathetically, interrupting your spiral."
    
    d "Perhaps that was a bit... tactless of me. I didn't mean to startle you."
    
    d "I simply ask because you can learn a lot about someone by hearing them speak on their own death."
    
    d "The information isn't required, and I've already learned a great deal about you. Let us move on."

    "What does that mean?! Regardless, he jots down a few notes and seems ready for the next question."

    jump q2


label q1_cheerful:

    "Damien lets out a laugh so dry it could be mistaken for a cough."
    
    "He looks surprised, like he's out of practice with amusement."

    d "All the more pity we can't eat." 
    
    "Nonetheless, he continues to look at you expectantly. It seems your joke didn't adequately sate his curiosity."

    menu:

        "Tell him.":
            jump q1_answer
        
        "Move the conversation in a different direction.":
            jump q1_deflect


label q1_deflect:

    y "So tell me a bit about the others who live... unlive? Unlive here. I'd like to know some more about them if I stay here."

    "Damien's smile thins a bit, face masked in a guarded expression."

    d "In due time."
    
    "His eyes betray that he knows exactly what you're doing, but thankfully he doesn't push you on the whole 'cause of death' thing."
    
    d "Some of the residents here are... skittish. And I take their privacy seriously."

    d "Rest assured that if you don't care for them when you meet them, you may always leave. There is no contract of residence here."

    "That statement doesn't fill you with confidence."

    jump q2

label q1_answer:
    menu:
        "\"Natural causes.\"":
            jump q1_natural

        "\"There was... an accident.\"":
            jump q1_accident

        "\"I was killed.\"":
            $ damien_approval += 1
            jump q1_murder

        "\"I honestly don't know...\"":
            jump q1_idk
  
label q1_natural:
    y "As far as I can remember, it all happened very peacefully."

    "Damien's eyes soften as he gives you a small smile."
    
    d "You are quite fortunate then." 
    
    d "I appreciate your candor on what is undoubtedly a sensitive topic. Thank you." 
    
    "Unsure of what to say in response, you nod, and Damien writes something down in the small pocket journal he's been holding."

    jump q2

label q1_accident:

    y "I think there was a car involved...? Sorry. The details are really hazy."

    "Damien nods sagely."
    
    d "You are newly dead. Those details will come back with time. And should you end up staying here, we will help you when they do." 
    
    d "I appreciate your candor on what is undoubtedly a sensitive topic. Thank you." 
    
    "Unsure of what to say in response, you nod, and Damien writes something down in the small pocket journal he's been holding."

    jump q2

label q1_murder:

    y "I can't... I dont remember all the details, but I know I was murdered."


    "Damien's eyes drop. He tries to muster up a smile, but it doesn't reach his eyes."
    
    d "I see." 
    
    "His voice is hardly above a whisper."
    
    d "Those memories will resurface with time. They can be quite painful when they do. We can help you through it, though, as we have helped each other."
    
    "Unsure of what to say in response, you nod, and Damien writes something down in the small pocket journal he's been holding."
    
    jump q2

label q1_idk:

    y "I don't remember anything about my death."

    "Damien nods sagely."
    
    d "You are newly dead. While it is rare to remember nothing, it is rarer still to remember all of it with clarity."
    
    d "Those details will come back with time. And should you end up staying here, we will help you when they do."
    
    d "I appreciate your candor on what is undoubtedly a sensitive topic. Thank you." 
    
    "Unsure of what to say in response, you nod, and Damien writes something down in the small pocket journal he's been holding."
    
    jump q2

label q2:
    "Damien flips to another page in his small journal."
    
    "You sit, slightly uncomfortable while he reads over the next page – perhaps he's reading his next question?"
    
    "Finally, he raises his head and looks towards you."

    d "When you lived, who was it you lived with?"

    menu:
        "Roommates.":
            jump q2_roommates

        "Friends.":
            jump q2_friends

        "Family.":
            jump q2_family

        "Alone.":
            jump q2_alone

label q2_roommates:

    y "Oh, I lived in a pretty small place, split the rent with a couple of roommates."

    "You pause, but Damien continues to stare expectantly at you. You clear your throat and continue."

    y "I didn't know them very well, and they moved out a couple of weeks after I woke up, so..."

    d "I understand" 
    
    "Damien holds up a hand, interrupting you. He pauses for a moment."
    
    d "How did you find it, your old living situation?"

    menu:
        "Annoying. (Aggressive)":
            $ damien_approval -= 1
            $ aggressive += 1
            jump q2_roommates_aggressive

        "Stressful. (Nervous)":
            $ damien_approval -= 1
            jump q2_roommates_nervous

        "Alright. (Confident)":
            jump q2_roommates_confident

        "Fun. (Cheerful)":
            $ damien_approval += 1
            jump q2_roommates_cheerful

label q2_roommates_aggressive:

    y "Ah, in a word... irritating. They weren't great roommates, and none of us shared space with each other well."
    
    y "Didn't fight much, but it certainly happened. Glad not to be living there any more."

    d "I see."
    
    "Damien looks at you blankly before flipping to a new page in his notebook."

    jump q3

label q2_roommates_nervous:

    y "I... um, well it could be a bit much at times. I didn't really know them very well and we didn't always... communicate well."
    
    y "But there weren't any fights or anything! We just, you know, didn't talk very much."

    d "I see."
    
    "Damien looks at you blankly before flipping to a new page in his notebook."

    jump q3

label q2_roommates_confident:

    y "It was fine I suppose." 
    
    "You shrug."
    
    y "I didn't know my roommates particularly well but we were amiable, no major conflicts."

    d "Good to hear." 
    
    "Damien nods and flips to the next page of his notebook."

    jump q3

label q2_roommates_cheerful:

    y "It was nice! I didn't know them that well to start, but we got along well. I would live with them again if, y'know...."

    d "I see; that's quite good to hear." 
    
    "A small smile spreads across Damien's face. He flips to the next page of his notebook."

    jump q3

label q2_friends:

    y "Oh, I lived in a pretty small place, split the rent with a couple of friends."

    "You pause, but Damien continues to stare expectantly at you. You clear your throat and continue."
    
    y "They moved out a couple of weeks after I woke up, I guess painful memories, so..."

    d "I understand." 
    
    "Damien holds up a hand, interrupting you. He pauses for a moment."
    
    d "How did you find it, your old living situation?"

    menu:
        "Annoying. (Aggressive)":
            $ damien_approval -= 1
            $ aggressive += 1
            jump q2_friends_aggressive

        "Stressful. (Nervous)":
            $ damien_approval -= 1
            jump q2_friends_nervous

        "Alright. (Confident)":
            jump q2_friends_confident

        "Fun. (Cheerful)":
            $ damien_approval += 1
            jump q2_friends_cheerful

label q2_friends_aggressive:

    y "Ah, in a word... irritating. Even though we were friends before, they weren't great roommates, and none of us shared space with each other well."
    
    y "Didn't fight much, but it certainly happened. Glad not to be living there any more."
    
    d "I see."
    
    "Damien looks at you blankly before flipping to a new page in his notebook."

    jump q3

label q2_friends_nervous:

    y "I... um, well it could be a bit much at times. They were my friends and we got along well but I wasn't used to living with people, and we didn't... communicate well."
    
    y "But there weren't any fights or anything! We just, you know, didn't talk about roommate issues much."

    d "I see."
    
    "Damien looks at you blankly before flipping to a new page in his notebook."

    jump q3

label q2_friends_confident:

    y "It was fine I suppose." 
    
    "You shrug."
    
    y "We were friends, had our disagreements but no major conflicts. All in all I'd say we lived together well"

    d "Good to hear." 
    
    "Damien nods and flips to the next page of his notebook."

    jump q3

label q2_friends_cheerful:

    y "It was nice! I was a bit nervous about living with friends, worried it would spoil the friendships, but we got along well. I would live with them again if, y'know...."

    d "I see; that's quite good to hear." 
    
    "A small smile spreads across Damien's face. He flips to the next page of his notebook."

    jump q3

label q2_family:

    y "Oh, I lived with my family."

    "You pause, but Damien continues to stare expectantly at you. You clear your throat and continue."
    
    y "It... it doesn't feel right, haunting them. I cant go back there."
    
    d "I understand." 
    
    "Damien holds up a hand, interrupting you. He pauses for a moment."
    
    d "How did you find it, your old living situation?"

    menu:
        "Annoying. (Aggressive)":
            $ damien_approval -= 1
            $ aggressive += 1
            jump q2_family_aggressive

        "Stressful. (Nervous)":
            $ damien_approval += 1
            jump q2_family_nervous

        "Alright. (Confident)":
            jump q2_family_confident

        "Safe. (Cheerful)":
            jump q2_family_cheerful

label q2_family_aggressive:

    y "Ah, in a word... irritating. I didn't get along with my family. I wish I had had a chance to go out on my own."
    
    d "I see."
    
    "Damien looks at you blankly before flipping to a new page in his notebook."

    jump q3

label q2_family_nervous:

    y "I... um, well it could be a bit much at times. My family could be really overbearing and... well I prefer to have more space to myself. Emotionally I mean."

    d "I see."
    
    "Damien looks at you blankly before flipping to a new page in his notebook."

    jump q3

label q2_family_confident:

    y "It was fine I suppose." 
    
    "You shrug."
    
    y "They're family. Sometimes we fought, but we loved each other."

    d "Good to hear." 
    
    "Damien nods and flips to the next page of his notebook."

    jump q3

label q2_family_cheerful:

    y "It was... safe. You don't always get along with family but it was really comforting to have them close by. I hope I can find something like that again..."

    d "Perhaps you will find that here."

    "A small smile spreads across Damien's face. He flips to the next page of his notebook."

    jump q3

label q2_alone:

    y "I lived alone."

    "Damien's eyes drop and he nods. He levels his gaze back on you."

    d "How did you find it, your old living situation?"

    menu:
        "Isolating. (Aggressive)":
            $ damien_approval += 1
            $ aggressive += 1
            jump q2_alone_aggressive

        "Lonely. (Nervous)":
            $ damien_approval += 1
            jump q2_alone_nervous

        "Alright. (Confident)":
            jump q2_alone_confident

        "Peaceful. (Cheerful)":
            jump q2_alone_cheerful
            $ damien_approval -= 1

label q2_alone_aggressive:

    y "It was... I didn't live alone for lack of trying. And living disconnected from others can be sort of isolating."

    d "Ah."
    
    "Damien offers you a sad smile."
    
    d "I can certainly understand that. Perhaps you'll find what you're looking for here."
    
    "He flips to a new page in his notebook."

    jump q3

label q2_alone_nervous:

    y "It was... lonely. I missed having other people around."

    d "Ah."
    
    "Damien offers you a sad smile."
    
    d "I can certainly understand that. Perhaps you'll find what you're looking for here."
    
    "He flips to a new page in his notebook."

    jump q3

label q2_alone_confident:

    y "It was fine, I suppose. Lots of space to think."

    d "I see."
    
    "Damien looks at you blankly before flipping to a new page in his notebook."

    jump q3

label q2_alone_cheerful:

    y "It was peaceful. I like the quiet."

    "Damien lets out a small chuckle."

    d "You might be disappointed here then."

    "He flips to a new page in his notebook."

label q3:

    if damien_approval >= 2:

        jump q3_approve
    
    d "Alright, just one more question."
    
    "Damien straightens up in his chair, his tone going more serious than before."
    
    d "Say you moved in. Say there was a crisis of some sort in the house. How would you handle it?"

    menu:
        "\"Figure out who's causing trouble and deal with them directly.\" (Aggressive)":
            $ damien_approval -= 1
            $ aggressive += 1
            jump q3_aggressive
        
        "\"What kind of crisis?\" (Nervous)":
            d "Any kind. I just want to know how you would respond in general."
            jump q3_layer2

        "\"Can you elaborate?\" (Confident)":
            d "I could." 
            "He paused."
            d "But I won't. I suppose I want to know your strategy for dealing with stressful things more generally."
            jump q3_layer2
        
        "\"Talk to everyone and figure out what I can do to help.\" (Cheerful)":
            $ damien_approval += 1
            jump q3_cheerful

label q3_approve:
    d "Alright, just one more question." 
    
    "Damien straightens up in his chair, his tone going more serious than before." 
    
    d "Say y-" 
    
    "He stops mid sentence, looking down at his notebook, furrowing his brow before closing the notebook and looking back towards you."

    d "I wish to be frank with you. We have all died, and death is inherently traumatic. We all have demons we face, and the residents of this house are no different."
    
    d "But sometimes, needs clash. Sometimes what is helpful for one is harmful to another, and conflict arises. How would you deal with this conflict?"

    menu:
        "\"Figure out who's causing trouble and deal with them directly.\" (Aggressive)":
            $ damien_approval -= 1
            $ aggressive += 1
            jump q3_aggressive
        
        "\"...I wouldn't.\" (Nervous)":
            $ damien_approval -= 1
            jump q3_nervous

        "\"Try to calm down whoever is in crisis and go from there.\" (Confident)":
            $ damien_approval += 1
            jump q3_confident2
        
        "\"Sit with whoever is having a rough time and let them vent to me.\" (Cheerful)":
            $ damien_approval += 1
            jump q3_cheerful


label q3_layer2:
    menu:
        "\"Figure out who's causing trouble and deal with them directly.\" (Aggressive)":
            $ damien_approval -= 1
            $ aggressive += 1
            jump q3_aggressive
        
        "\"...I wouldn't.\" (Nervous)":
            $ damien_approval -= 1
            jump q3_nervous

        "\"Without knowing the specific issue, I can't say for sure, but I'm good at keeping a level head.\" (Confident)":
            $ damien_approval += 1
            jump q3_confident
        
        "\"Talk to everyone and figure out what I can do to help.\" (Cheerful)":
            $ damien_approval += 1
            jump q3_cheerful


label q3_aggressive:

    d "What?"
    
    "Damien looks... concerned."

    y "I just mean... well, we're dead, so this crisis obviously isn't a natural disaster or anything. It's interpersonal." 
    
    y "And if you're so concerned about making sure everyone here is a 'good fit,' then fine. Whoever is causing the problem can leave."

    "Damien looks stunned. Several times he opens his mouth to speak, but closes it again, unsure what to say. Frustrated, you finally speak up."
    
    y "Look, this can't be an unexpected answer. That's basically what you're doing here. If you don't fit in, you're kicked to the curb."
    
    d "I... see."

    jump endings

label q3_nervous:

    d "What?"
    
    "Damien looks... concerned."

    y "I... I freeze up, when things are intense. In all honesty I probably wouldn't be much help."

    d "I... see."
    
    "He clears his throat and rights himself before continuing."
    
    d "I appreciate your honesty."

    jump endings

label q3_confident:

    d "Indeed."
    
    "Damien nods, seemingly impressed."

    jump endings

label q3_confident2:

    y "I would need to know more about the specific issue at hand, but I'm good at keeping a level head."

    d "Indeed."
    
    "Damien nods, seemingly impressed."

    jump endings

label q3_cheerful:

    y "In my experience, just hearing people out and really listening helps the most."

    d "Indeed."
    
    "Damien nods, seemingly impressed."

    jump endings

label endings:

    return
