# ==========================================
# 1. DEFINE CHARACTERS & IMAGES
# ==========================================

define m = Character("Arwa", color="#c83b86")
define k = Character("Kawtar", color="#4ba3e3")
define M = Character("Mehdi", color="#e36b4b")
define f = Character("Fatima Zahra", color="#a34be3")
define g = Character("Mama", color="#e3ab4b")
define s = Character("Suhaibe", color="#4be371")

# --- Backgrounds (الأسماء مطابقة تماماً لما يوجد في مجلد images لديك) ---
image bg toto = "toto.png"
image bg manzil = "manzil.png"
image bg babe = "babe.png"
image bg tri9 = "tri9.png"
image foto = "foto.png"

# --- صورة الهاتف مكبرة وفي الوسط ---
image tili1 = Transform("tili1.png", zoom=2.5)

# --- Characters & Sprites ---
image kawtar1 = Transform("kawtar1.png", zoom=2.0)
image kawtarhappy = Transform("kawtarhappy.png", zoom=2.0)
image kawtarmasdoma = Transform("kawtarmasdoma.png", zoom=2.0)
image mama = Transform("mama.png", zoom=2.0)
image fati = Transform("fati.png", zoom=2.0)
image tswirw bad = "foto.png"

# ==========================================
# 2. GAME START
# ==========================================

label start:

    scene black
    "I'm Arwa, a girl. This is my story. I am 16 years old now."

    jump tell_the_story
         

# ==========================================
# 3. TELL THE STORY
# ==========================================         

label tell_the_story:

    scene bg toto 

    m "Let's go back 3 years ago"
    m "It all started in 8th grade on the first day of school"
    m "At that time, I was standing with a friend in front of the classroom waiting for the break to end"
    
    show kawtar1 at center
    
    m "And I saw her standing there. I remember she was wearing a dark pink hijab with a dress, her heart-shaped earrings were clearly visible" 
    m "She looked like she didn't want to talk to anyone or as if she looked down on us and was wearing glasses"        
    m "And I looked weird"
    m "I actually go to school one or three times a week"
    m "I was always with my friend"
    m "The first time we talked was in a sport session"
    m "I talked with her or I can say my friend talked to her and me"
    m "After that I started to talk with her"
    
    jump talk_with_mama

# ========================================
# 4. DIALOG WITH MAMA
# ========================================

label talk_with_mama:

    scene bg manzil
    show mama at center

    g "Hi Arwa, what about going with your brother at extra hours in English"

    menu:
        "Ask about more":
            m "Give me more information"
            g "It's just a girl who is 19 years old explaining English in her house and Nazha says it is good"
            m "Okei it is good"
            m "Alors tu vas le faire?"
            
            menu:
                "Yes":
                    m "Okei" 
                    g "THAT'S good you have a session tomorrow at 5pm"
                    m "Okei"
                    
                    scene bg tri9 
                    
                    m "You know Mama tell me to do extra hours with Suhaibe"
                    k "Oh thats good"
                    m "Yes"

                    scene bg manzil
                    show mama at center
                    
                    m "This is the time"
                    g "Yes is it"
                    m "Okei I'm going"
                    
                    scene bg babe
                    show kawtarmasdoma at center
                    
                    m "What?, Kawtar what are you doing here?"
                    k "This is my house"
                    "This is so fuckin embarrassing"
                    
                    scene bg manzil
                    show fati at center
                    
                    m "Hi"
                    f "Hi Arwa sit down here and you Suhaib here"
                    m "Okei"
                    s "Okei"
                    f "Donc what grade are you in?"
                    m "Oh, now im in second year in college and already studying in same class as Kawtar"
                    k "Ah yes"
                    f "Thats good"
                    "Oh this session it is good and also Kawtar here thats very good"
                    
                    scene black
                    "After a few months the summer vacation and i stay going at extra hours with Fatima Zahra and more training chips with Kawtar but i feel good i have a new good friend and i also i dead of laughing with her"
                    "And one day in extra hours both we see one message"
                    
                    scene bg manzil
                    show kawtarmasdoma at center
                    
                    k "Oh hmp we are not in the same class thats bad"
                    m "Ou yes thats bad"
                    k "Oh the class WhatsApp group send something"
                    m "Oh what it is?"
                    
                    scene black
                    show tili1 at truecenter
                    
                    k "What the fuck this can't be real"
                    m "Why what"
                    k "Amina.."
                    m "Yes" 
                    k "Amina dead"
                    m "What how -how did you know?"
                    k "The message see"
                    m "But how she dead she was younger she just 13 years old"
                    f "Ha your friend dead you are sure?"
                    m "No this just a message send by her sister"
                    f "Ask more? And she can't just be laughing with you?"
                    k "No she never laughing like that"
                    m "Yes and she disappear this month she didn't answer any message and she always answers"
                    k "Yes and her instagram account deleted"
                    m "Yes"
                    f "She has the big sibling"
                    k "Yes" 
                    f "Ah Arwa you need to go back the time up and its dark now"
                    m "Oh okei Suhaibe let's go"
                    
                    "And this the day when i lost Amina our angel Amina she was kind helpful and the best person you can know"
                    "That's sad i think this is the first bad emotion we share"
                    "After that my personality change i take learning seriously"
                    "In the 9th grade i didn't absent for no reason look like last year"
                    
                    scene bg toto 
                    show kawtarhappy at center
                    
                    k "Oh finally i see you. We cooked , this is more exams"
                    m "Yes me tooo"
                    k "Damn Kawtar Kawtar do you see the trend at school where they choke you , and right after that they give you a light tap so you pass out?"
                    
                    menu:
                        "ou let's do it":
                            m "Let's do it , i dont want to study for this hour"
                            k "Me i have math"
                            m "Thats better i have svt"
                            k "Ou fuck oumadi this teacher"
                            m "I'm cooked i gonna kill my self"
                            k "Me too"
                            "Ou thats disgusting"
                            m "Ou thats disgusting"
                            m "Wait"
                            k "Some of the girls in my class do it"
                            m "Nah thats bad"
                            
                        "No thanks, let's study":
                            m "Nah let's just focus on studying."
                            k "You're right, we are already cooked."

                    scene black    
                    scene bg tri9
                    "Oh i finish this class"
                    "Finally i feel like i am tortured but i have extra hours nahhhhh but i will draw in it and talk with Kawtar"
                    
                    k "Arwa"
                    k "Arwa"
                    
                    show kawtarhappy at center
                    m "Ou Kawtar finally"
                    k "Ah"
                    m "So les go but i gonna buy mesamane withe hany"
                    k "Oh yeh i didn't eat any thing"
                    m "Me to now lest go fast we late"
                    
                    scene black
                    "After that i will be very happy to talk withe her i say every thing to her and also i saw her every good thing i love and any thing happen withe me and thas the same fore bouth of we."
                    "And like thats i star to talk her in discord and in discord i meet the best fortnite player mehdi and his bashe friend"
                    "And one day after i be some close"
                    
                    m "Oh Kawtar MyBaByiLoVeyOusOmuChE"
                    k "OhhYehYouLovEMe"
                    M "Yo yo hi betche"
                    M "You fat betche"
                    k "Yo hi Mehdi"
                    m "Hi mahdi , hey stop dont say thas"
                    M "Hahaha this fate"
                    "Ah again this is personality of mehdi but i still want him a friend"
                    "And like thas i can spend my time withe they and talk about any thing"
                    "Now i can say i love my life and some time i hate it"
                    "But still i dont want a normal or a simpel life i want pride life i want any person juste talk withe me feel pride of me"
                    
                    scene black
                    show foto at truecenter
                    "This is a real story or my story thanks so mache for playng MWAH" 
                    "And thanks very matche Kawtar becouse you are my friend"              
                    return

                "No":
                    m "I don't think so mama"
                    g "As you like !"
                    m "okei"
                    m "i need to go"
                    
                    scene bg tri9
                    m "Hi Kawtar"
                    k "Ah hiy arwa"
                    m "What we have in this day"
                    k "We have mats and arabic"
                    m "Thanks"
                    
                    scene black
                    "After some months the year end and i did not talk withe her again"
                    "And then during that period a fallout happened between me and my friend XXXX ,and i discoverts a lot of things she did. She exploited the secrets i had told her, and afterward , i fell into depression"
                    "However, i managed to hide it a little"
                    "After losing XXXX , i didn't have the capacity to trust easily."
                    "The following year, i met another girl, but i couldn't tell her every thing about myself or even trust her because of what XXXX did , despite my life had died-a girl who used to study with me. I only found out months later. I loved her, but even after her disappearance, i couldn't imagine that she was gone"
                    "And like thas in the end of the year i see her again but" 
                    "And in the end of the year i see Kawtar again but just look like a person i know him in the party of graduation in the end of the year"
                    
                    
                    "Thanks for playing my game and share it white your besti"
                    "And again thanks soooo muche Kawtar becouse you are my freind"
                    return