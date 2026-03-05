# Character declarations

define d = Character("Damien")
define y = Character("[name]")

# Variable declarations
default damien_approval = 0
default aggressive = 0

# The game starts here.

label start:

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
    
        "\"Absolutely not.\" (Agressive)":
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

    return
