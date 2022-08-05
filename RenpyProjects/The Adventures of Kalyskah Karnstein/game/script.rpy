define notSettings = 1

define IsKalyNaked = 0

define Kalyskah = Character("Kalyskah", color = "#ADD8E6")
define Merishya = Character("Merishya", color = "#DC143C")

label splashscreen:
    #default persistent.game_language = 'eng'
    scene black
    show logo_1 with blinds
    $ renpy.pause(2.0, hard = True)
    hide logo_1 with blinds
    $ renpy.pause(1.0, hard = True)
    #jump start
    #scene warning with Dissolve(0.5)
    #$ renpy.pause(4.0, hard = True)
return


label start:
    play music "audio/forest_exploration.mp3" loop fadeout 1.0
    scene HighresScreenshot00001 with Dissolve(0.6)
    "It was a tiresome morning of august when the vampire Kalyskah had finally decided to listen to the request of Merishya Sarinoza"
    "The demoness told her about a place in the country of Gormakar, far from Thulgatha, where they originally met."
    scene HighresScreenshot00002 with Dissolve(0.6)
    "It was said that this place contained a very specific resonance that could help the demoness back home"
    "Kalyskah would rather not go, but a sense of honour and gratitude urged her to help the demoness with her predicament."
    scene HighresScreenshot00003 with Dissolve(0.6)
    "Hours of hiking have turned to days… Kalyskah would stay quiet for most of the time. But she could see the demoness humming all the way."
    scene HighresScreenshot00004 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00005 with Dissolve(0.6)
    Kalyskah "Demoness… I am confident we have already seen this tree."
    scene HighresScreenshot00006 with Dissolve(0.6)
    "They stared into the horizon. Merishya just wiggled her tail:"
    scene HighresScreenshot00007 with Dissolve(0.6)
    Merishya "Hmm…"
    scene HighresScreenshot00008 with Dissolve(0.6)
    Kalyskah "Merishya, are you sure we are in the correct place?"
    Merishya "Hmm…"
    scene HighresScreenshot00009 with Dissolve(0.6)
    Kalyskah "Demoness… Answer me!"
    scene HighresScreenshot00010 with Dissolve(0.6)
    Merishya "Well, it looks the same…Smells the same…."
    scene HighresScreenshot00011 with Dissolve(0.6)
    Kalyskah "You do not sound so sure!"
    scene HighresScreenshot00012 with Dissolve(0.6)
    Kalyskah "We have been walking for hours, even my forbearance has its limits."
    scene HighresScreenshot00013 with Dissolve(0.6)
    Merishya "It was around here somewhere, the portal."
    scene HighresScreenshot00014 with Dissolve(0.6)
    Kalyskah "Yes, yes! The red portal with fire on the other side."
    scene HighresScreenshot00013 with Dissolve(0.6)
    Merishya "Exactly! I can finally get back home; I just need to... Find it."
    scene HighresScreenshot00015 with Dissolve(0.6)
    Kalyskah "<sighs> Fair enough, lead the way…"

    scene HighresScreenshot00016 with Dissolve(0.6)
    "The Sun was high in the sky, hours were passing quickly."
    "Kalyskah was grateful she was well fed so that the daylight couldn’t harm her skin."
    scene HighresScreenshot00017 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00018 with Dissolve(0.6)
    "Meanwhile, Merishya was quiet."
    "Thoughtful, even.."
    scene HighresScreenshot00019 with Dissolve(0.6)
    Merishya "I’m sure I’ve seen this rock.."
    scene HighresScreenshot00020 with Dissolve(0.6)
    Merishya "Hmm…"
    scene HighresScreenshot00021 with Dissolve(0.6)
    "That was it. That was the last humming the vampire could endure to listen."
    "She stopped, glaring to the succubus."
    "Something had finally sinked in."
    scene HighresScreenshot00022 with Dissolve(0.6)
    Merishya "What’s the problem?"

    #*Render of them looking around. Kalyskah is annoyed and impatient*

    scene HighresScreenshot00023 with Dissolve(0.6)
    Kalyskah "We are lost, are we not?"
    scene HighresScreenshot00024 with Dissolve(0.6)
    Merishya "Lost is such a strong word. Let’s say… We are taking a detour!"
    "The truth was exposed, there was no reason to fight over it. Kalyskah calmed down."
    scene HighresScreenshot00025 with Dissolve(0.6)
    Kalyskah "Let us sit, Merishya."
    scene HighresScreenshot00026 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00027 with Dissolve(0.6)
    Merishya "Why? Don’t tell me you’re tired, Kalyskah."
    scene HighresScreenshot00028
    Kalyskah "Vampires do not get tired. I just want a break. Besides, we need to plan what we’ll do next, walking in circles will do us no good."
    scene HighresScreenshot00029 with Dissolve(0.6)
    Kalyskah "We have been walking for hours and this place…"
    scene HighresScreenshot00030 with Dissolve(0.6)
    Kalyskah "Brings back memories."
    scene HighresScreenshot00031 with Dissolve(0.6)
    "Merishya could sense the trouble in the eyes of her companion. She nodded."

    scene HighresScreenshot00032 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00033 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00034 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00035 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()

    scene HighresScreenshot00036 with Dissolve(0.6)
    Merishya "You’re quiet. Coin for your thoughts?"
    scene HighresScreenshot00037 with Dissolve(0.6)
    Kalyskah "It is this jungle… It– it takes me back home."
    scene HighresScreenshot00038 with Dissolve(0.6)
    Merishya "Home? You mean the underground temple you’ve found me in?"
    scene HighresScreenshot00039 with Dissolve(0.6)
    Kalyskah "Not that home. That was more like a Temple."
    scene HighresScreenshot00040 with Dissolve(0.6)
    Kalyskah "When I say ’home’ I mean the place I was born."
    scene HighresScreenshot00041 with Dissolve(0.6)
    Merishya "Oh! Sometimes I forget you were human once."
    scene HighresScreenshot00042 with Dissolve(0.6)
    Merishya "How long ago was that?"
    scene HighresScreenshot00043 with Dissolve(0.6)
    Kalyskah "If my maths are correct..."
    scene HighresScreenshot00044 with Dissolve(0.6)
    Kalyskah "it was at least twenty-two thousand years ago."
    scene HighresScreenshot00045 with Dissolve(0.6)
    Kalyskah "The world was very different… As was I."
    scene HighresScreenshot00046 with Dissolve(0.6)
    Merishya "Uhum…"
    scene HighresScreenshot00047 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00048 with Dissolve(0.6)
    Merishya "Care to elaborate or should we just enjoy the silence?"
    scene HighresScreenshot00049 with Dissolve(0.6)
    Kalyskah "Well, we did not have tools like we have today."
    scene HighresScreenshot00050 with Dissolve(0.6)
    Kalyskah "Our weapons were mostly wooden spears with sharp stone at the tip."
    scene HighresScreenshot00051 with Dissolve(0.6)
    Merishya "Ha! So you’re telling me you were born in the actual stone age!"
    scene HighresScreenshot00052 with Dissolve(0.6)
    Kalyskah "I think that is what you call it today."
    Kalyskah "The climate was hotter in the region that Thulgatha is today, so those pine woods there used to be a jungle…"
    scene HighresScreenshot00053 with Dissolve(0.6)
    Kalyskah "Just like this one."
    scene HighresScreenshot00054 with Dissolve(0.6)
    Kalyskah "Just one of the many things that changed, I suppose."
    scene HighresScreenshot00055 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00056 with Dissolve(0.6)
    Merishya "Oh! That sounds lovely. I’m used to hot places!"
    Kalyskah "Hehe. I see what you did there.."

    scene HighresScreenshot00057 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00058 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00059 with Dissolve(0.6)
    window hide # hides the window. 
    $ renpy.pause()
    scene HighresScreenshot00060 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00061 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00062 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00063 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00064 with Dissolve(0.6)
    Merishya "Sweetie.."
    scene HighresScreenshot00065 with Dissolve(0.6)
    Merishya "Are you all right?"
    scene HighresScreenshot00066 with Dissolve(0.6)
    Kalyskah "Yes… I am fine."
    scene HighresScreenshot00067 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00068 with Dissolve(0.6)
    Merishya "Want to be left alone for a moment?"
    scene HighresScreenshot00069 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()

    jump Choice_2
return




label Choice_2_1:

    scene HighresScreenshot00071 with Dissolve(0.6)
    Kalyskah "I do not want to be alone... I have been lonely for far too long."
    scene HighresScreenshot00072 with Dissolve(0.6)
    Kalyskah "Please, do not go." 
    Merishya "Want to talk about it?"
    scene HighresScreenshot00073 with Dissolve(0.6)
    Kalyskah "No... Just– just kiss me."

    #*Merishya looks surprised. They start making out.*
    play music "audio/lovers_scene.mp3" loop fadeout 1.0

    scene HighresScreenshot00074 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00075 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00076 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00077 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00078 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00079 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00080 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00081 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()

    scene HighresScreenshot00082 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00083 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00084 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00085 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00086 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00087 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00088 with Dissolve(0.6)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00089 with Dissolve(0.6)
    Kalyskah "Oh, my…"
    scene HighresScreenshot00090 with Dissolve(0.6)
    Kalyskah "Yes… go lower…"
    "Merishya puts her hands on the clothes on Kalyskah’s chest"
    scene HighresScreenshot00091 with Dissolve(0.6)
    Merishya "Hehe.."
    scene HighresScreenshot00092 with Dissolve(0.6)
    Kalyskah "Why are you looking at me like that?"
    scene HighresScreenshot00093 with Dissolve(0.6)
    Merishya "These clothes…"
    scene HighresScreenshot00094 with Dissolve(0.6)
    Kalyskah "They’ve got to go!"
    #Some sound-effect of clothes being ripped and the camera shaking

    scene HighresScreenshot00095 with Dissolve(0.6)
    Kalyskah "You ruined my clothes!"
    scene HighresScreenshot00096 with Dissolve(0.6)
    Kalyskah "{i}{color=#DCDCDC}By the storms, is her knees where I think they are?"
    scene HighresScreenshot00097 with Dissolve(0.6)
    Kalyskah "{i}{color=#DCDCDC}Uhng.. I won’t be able to control myself.."
    scene HighresScreenshot00098 with Dissolve(0.6)
    Merishya "Yes! I ruined them. What are you going to do about it?"
    Merishya "Because I know what I’ll do.."
    scene HighresScreenshot00099 with Dissolve(0.6)
    Kalyskah "{i}{color=#DCDCDC}Urgh… such a hot tongue!"
    scene HighresScreenshot00100 with Dissolve(0.6)
    Kalyskah "Ok, you convinced me. You may proceed."
    scene HighresScreenshot00101 with Dissolve(0.6)
    Merishya "Can I?"
    scene HighresScreenshot00102 with Dissolve(0.6)
    Merishya "I had an idea in that case:"
    scene HighresScreenshot00103 with Dissolve(0.6)
    Merishya "This tail is begging to get inside somewhere, so you better choose fast!"

    menu:
        "Choose pussy":  #1.a 
            scene HighresScreenshot00103 with Dissolve(0.6)
            Kalyskah "Err… Lets.. take it slow!"
            scene HighresScreenshot00104 with Dissolve(0.6)
            Merishya "Your wish is my command, lady!"
            scene HighresScreenshot00105 with Dissolve(0.6)
            Kalyskah "Ughn!"
            scene HighresScreenshot00106 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00107 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00108 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Is she increasing the pace?"
            scene HighresScreenshot00109
            Kalyskah "{i}{color=#DCDCDC}Oh fuck, I don’t care!"



        "Choose arse": #1.b
            scene HighresScreenshot00103 with Dissolve(0.6)
            Kalyskah "Hm… I am feeling adventurous today! Let’s try my back door!"
            scene HighresScreenshot00101 with Dissolve(0.6)
            Merishya "Oh my, who would have ever thought that the lady vampire was such a dirty slut!"

            menu:
                "Don’t talk dirty to me!": #1.b.1 
                    scene HighresScreenshot00100 with Dissolve(0.6)
                    Kalyskah "Tune down your attitude, or I will make you do so!"
                    scene HighresScreenshot00103 with Dissolve(0.6)
                    Merishya "Oh, I’m sorry. I got a bit carried away."
                    scene HighresScreenshot00108 with Dissolve(0.6)
                    Merishya "Lift up your legs, sweetie."
                    scene HighresScreenshot00109 with Dissolve(0.6)
                    Kalyskah "It’s so hot!"
                    scene HighresScreenshot00110 with Dissolve(0.6)
                    Merishya "Don’t worry, I’m taking it slow."
                    Kalyskah "Come here, let me taste your tongue."
                    scene HighresScreenshot00111 with Dissolve(0.6)
                    window hide # hides the window.
                    $ renpy.pause()

                "Yes! I am!": #1.b.2 

                    scene HighresScreenshot00100 with Dissolve(0.6)
                    Kalyskah "Yes, yes! I am, now stop talking and fuck my arse!"
                    scene HighresScreenshot00103 with Dissolve(0.6)
                    Merishya "Your wish is my command, vampire slut!"
                    scene HighresScreenshot00112 with Dissolve(0.6)
                    Kalyskah "FUCK! You put it all at once!"
                    scene HighresScreenshot00101 with Dissolve(0.6)
                    Merishya "Shut up. I know you like it!"
                    scene HighresScreenshot00110 with Dissolve(0.6)
                    Kalyskah "Nhum… Guilty…."
                    scene HighresScreenshot00111 with Dissolve(0.6)
                    scene HighresScreenshot00109 with Dissolve(0.6)
                    Merishya "Moan for me, slut!"
                    scene HighresScreenshot00113 with Dissolve(0.6)
                    Kalyskah "*moans*"




        "Let her choose": #1.c 
            scene HighresScreenshot00100 with Dissolve(0.6)
            Kalyskah "Hm… Why don’t you surprise me?!"
            scene HighresScreenshot00101 with Dissolve(0.6)
            Merishya "No preference, hm? So powerful yet so submissive."
            scene HighresScreenshot00103 with Dissolve(0.6)
            Merishya "Alright.."
            scene HighresScreenshot00163 with Dissolve(0.6)
            Merishya "Stay quiet and enjoy!"
            scene HighresScreenshot00164 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Damn, when did she became so– *Urgh*"
            scene HighresScreenshot00167 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Her tail is in my…!"
            scene HighresScreenshot00165 with Dissolve(0.6)
            Merishya "What’s the problem, vampire, did you feel the sting?"
            scene HighresScreenshot00169 with Dissolve(0.6)
            "Merishya pushes her tail even deeper"
            scene HighresScreenshot00166 with Dissolve(0.6)
            Merishya "Awnser me, slut!"
            scene HighresScreenshot00168 with Dissolve(0.6)
            "*Pinches*"
            scene HighresScreenshot00165 with Dissolve(0.6)
            Merishya "I know you love it in the arse!"
            scene HighresScreenshot00164 with Dissolve(0.6)
            Kalyskah "*Moans* Y-yesh!"
            scene HighresScreenshot00168 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00170 with Dissolve(0.6)
            "Kalyskah tried not to say anything else, how could she, with her mouth so busy?"
            "The vampire just layed down, relaxing her body and enjoyed the way the succubus was handling her."



        "Just kiss me": #1.d 
            scene HighresScreenshot00100 with Dissolve(0.6)
            Kalyskah "Stop with the games, I am not in the mood for this right now. Just… kiss me"
            scene HighresScreenshot00103 with Dissolve(0.6)
            Merishya "I know a place that I could kiss."
            scene HighresScreenshot00173 with Dissolve(0.6)
            Kalyskah "Hey! What are you doing with your tail!?"
            scene HighresScreenshot00103 with Dissolve(0.6)
            Merishya "Just relax, Kalyskah, I need your legs wide open for this."
            scene HighresScreenshot00171 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}By the storms, her tongue is just so…"
            scene HighresScreenshot00172 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}So.."
            scene HighresScreenshot00174 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00175 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Fucking perfect!"
            scene HighresScreenshot00176 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00177 with Dissolve(0.6)


    scene black with Dissolve(0.6)
    "This part is in development and more content will be added here."
    "For now I bring you back to the first choice menu"
    play music "audio/forest_exploration.mp3" loop fadeout 1.0
    jump Choice_2



return





label Choice_2:
    scene HighresScreenshot00070 with Dissolve(0.6)
    menu:
        "Stay with me.": #1
            jump Choice_2_1
            


        "I need to be alone.": #2
            scene HighresScreenshot00114 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            
            scene HighresScreenshot00115 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00116 with Dissolve(0.6)
            Kalyskah "I would."
            scene HighresScreenshot00117 with Dissolve(0.6)
            Kalyskah "Also, I’m not in the mood for your games right now."
            scene HighresScreenshot00118 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00119 with Dissolve(0.6)
            Kalyskah "I’m sorry Merishya, it’s just… It’s been a long day."
            scene HighresScreenshot00120 with Dissolve(0.6)
            Merishya "Very well"
            scene HighresScreenshot00121 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00122 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00123 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}I hope she doesn’t go too far and get even more lost"
            scene HighresScreenshot00124 with Dissolve(0.6)
            Merishya "Shout me if you need me!"
            scene HighresScreenshot00125 with Dissolve(0.6)
            Kalyskah "As if you are not the one that always gets into trouble!"
            scene HighresScreenshot00126 with Dissolve(0.6)
            Merishya "I know you love me!"
            scene HighresScreenshot00127 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Bold of her to assume this…."
            scene HighresScreenshot00128 with Dissolve(0.6)
            Kalyskah "I have been a shell with so few emotions ever since I became what I am."
            scene HighresScreenshot00129 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Finally, some time alone."
            scene HighresScreenshot00130 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}The sun is high… I should probably rest until night.."
            scene HighresScreenshot00131 with Dissolve(0.6)
            window hide # hides the window.
            $ renpy.pause()
            scene HighresScreenshot00132 with Dissolve(0.6)
            Kalyskah "How I miss those old days… The taste of sugar cane…"
            scene HighresScreenshot00133 with Dissolve(0.6)
            "The vampire closed her eyes and did not realise she was no longer alone."

            play music "audio/tentacles_aproaching.mp3" loop fadeout 1.0
            scene HighresScreenshot00134 with Dissolve(0.6)
            "A funny thing is the sleep of a vampire."
            scene HighresScreenshot00135 with Dissolve(0.6)
            "It’s heavy…"
            scene HighresScreenshot00136 with Dissolve(0.6)
            "Leave them vulnerable."
            scene HighresScreenshot00137 with Dissolve(0.6)
            "And unaware."
            scene HighresScreenshot00138 with Dissolve(0.6)
            "Until suddenly."
            scene HighresScreenshot00139 with Dissolve(0.6)
            Kalyskah "What in the Storms are you!"
            scene HighresScreenshot00140 with Dissolve(0.6)
            Kalyskah "Do not come any closer!"
            scene HighresScreenshot00141 with Dissolve(0.6)
            Kalyskah "Oh.. you do not want to harm me, do you?"
            scene HighresScreenshot00142 with Dissolve(0.6)
            Kalyskah "What are you doing?"
            scene HighresScreenshot00143 with Dissolve(0.6)
            Kalyskah "Stop it... It-it tickles!"
            scene HighresScreenshot00144 with Dissolve(0.6)
            Kalyskah "Wait... do you want to–"
            scene HighresScreenshot00145 with Dissolve(0.6)
            Kalyskah "To mate?"
            scene HighresScreenshot00146 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}They are everywhere…"
            scene HighresScreenshot00147 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Hm… It feels soo soft in my arm…."
            scene HighresScreenshot00148 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}No one would know, would they?"
            scene HighresScreenshot00149 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}Hold on a moment Kalyskah… You are not actually considering…"
            scene HighresScreenshot00150 with Dissolve(0.6)
            Kalyskah "{i}{color=#DCDCDC}But no one is looking right now…"

            menu:
                "Mate with the creature":

                    scene HighresScreenshot00150 with Dissolve(0.6)
                    Kalyskah "All right... What harm can it do? Besides, I do need a distraction…"
                    scene HighresScreenshot00178 with Dissolve(0.6)
                    Kalyskah "Whoops! You are holding me a bit too tight, who gave you permission for that?"
                    scene HighresScreenshot00249 with Dissolve(0.6)
                    "Despite her words, under her clothes, the state of her nipples wouldn’t allow her to deny her feelings"
                    scene HighresScreenshot00179 with Dissolve(0.6)
                    Kalyskah "You.. you are so… Soft.."
                    scene HighresScreenshot00180 with Dissolve(0.6)
                    Kalyskah "{i}{color=#DCDCDC}He’s all over me now!"
                    scene HighresScreenshot00238 with Dissolve(0.6)
                    Kalyskah "Found something interesting down there?"
                    scene FirstGlow
                    Kalyskah "Wait, why are you glowing?"
                    scene SecondGlow
                    Kalyskah "Whoa! You are ruining my clothes!"
                    scene HighresScreenshot00242 with Dissolve(0.6)
                    window hide # hides the window.
                    $ renpy.pause(0.1, hard = True)
                    scene HighresScreenshot00241 with Dissolve(0.6)
                    window hide # hides the window.
                    $ renpy.pause(0.1, hard = True)
                    scene HighresScreenshot00182 with Dissolve(0.6)
                    window hide # hides the window.
                    $ renpy.pause(0.1, hard = True)
                    scene HighresScreenshot00183 with Dissolve(0.6)
                    window hide # hides the window.
                    $ renpy.pause(0.1, hard = True)
                    Kalyskah "Alright…"
                    scene HighresScreenshot00184 with Dissolve(0.6)
                    Kalyskah "I might have encouraged you…"
                    scene HighresScreenshot00185 with Dissolve(0.6)
                    Kalyskah "But maybe you are going a bit too far!"
                    scene HighresScreenshot00186 with Dissolve(0.6)
                    Kalyskah "Hm…" 
                    scene HighresScreenshot00187 with Dissolve(0.6)
                    Kalyskah "{i}{color=#DCDCDC}Should I take control over the situation?"



                    menu:
                        "Let the creature dominate you":
                            scene HighresScreenshot00187 with Dissolve(0.6)
                            Kalyskah "Hm.. I see you are quite an assertive being… Come, then, show me what you– "
                            scene HighresScreenshot00188 with Dissolve(0.6)
                            Kalyskah "*Gags*"
                            scene HighresScreenshot00189 with Dissolve(0.6)
                            Kalyskah "{i}{color=#DCDCDC}Fuck! He is everywhere!"
                            "It takes a while before Kalyskah manages to adjust to it, but once it happens her jaw relaxes and she gladly swallows down around the tentacle. "
                            "It pushes in and out, wet, thick and sloshing down her throat as it happens."
                            "She presses her tongue on the underside and bobs her head simultaneously with the thrusts it pushes…"
                            scene HighresScreenshot00193 with Dissolve(0.6)
                            "Unable to pay attention to the rest of the tentacles as they grab her and spread her open, exposing her so thoroughly especially as it starts pressing against the clit."
                            scene HighresScreenshot00190 with Dissolve(0.6)
                            Kalyskah "{i}{color=#DCDCDC}Ahh! He’s not even trying to be gentle!"
                            scene HighresScreenshot00191 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00192 with Dissolve(0.6)
                            Kalyskah "{i}{color=#DCDCDC}What is he doing back there?"
                            scene HighresScreenshot00193 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00194 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00192 with Dissolve(0.6)
                            Kalyskah "{i}{color=#DCDCDC}By the–"
                            scene HighresScreenshot00195 with Dissolve(0.6)
                            Kalyskah "{i}{color=#DCDCDC}*Ughn* I fucking love it!"
                            scene HighresScreenshot00196 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00197 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00198 with Dissolve(0.6)
                            Kalyskah "{i}{color=#DCDCDC}Y-yes.. Use me for your pleasure!"
                            scene HighresScreenshot00199 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00200 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00201 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00202 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()

                            jump Merishya_Return

                        
                        "Do not allow it to restrict your movements":
                            scene HighresScreenshot00187 with Dissolve(0.6)
                            "The vampire starts to gather her strength and…"
                            scene HighresScreenshot00210 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00211 with Dissolve(0.6)
                            "The living vines prove no match for her strength!"
                            scene HighresScreenshot00212 with Dissolve(0.6)
                            Kalyskah "{i}{color=#DCDCDC}I hope I did not hurt it."
                            Kalyskah "{i}{color=#DCDCDC}Wait, are they going away?"
                            scene HighresScreenshot00213 with Dissolve(0.6)
                            "She quickly grabs one of the tentacles."
                            Kalyskah "We will play, sweet creature."
                            scene HighresScreenshot00214 with Dissolve(0.6)
                            Kalyskah "But under my terms!"
                            scene HighresScreenshot00215 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00216 with Dissolve(0.6)
                            "Kalyskah picks up a tentacle and starts licking it, using her left hand to appease the others that were afraid of her."
                            scene HighresScreenshot00217 with Dissolve(0.6)
                            "The vampire was eons old, her tongue was so skilled that the creature could do nothing but melt at her touch."
                            scene HighresScreenshot00218 with Dissolve(0.6)
                            "Noticing that, the others started to come back."
                            scene HighresScreenshot00245 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00246 with Dissolve(0.6)
                            "She didn’t lose time either; after tasing it for a while, noticing how wet and rough the creature’s texture was, she brought it inside her mouth." 
                            scene HighresScreenshot00247 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00248 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00220 with Dissolve(0.6)
                            Kalyskah "I see what you are trying to do back there… don’t be shy, I love it in the arse!"
                            scene HighresScreenshot00220 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00221 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00222 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00223 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00224 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00225 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00226 with Dissolve(0.6)
                            "Kalyskah squirms as the tentacle enters her."
                            scene HighresScreenshot00227
                            "Her face was distorted by pleasure as she bites her lips."
                            scene HighresScreenshot00228 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00229 with Dissolve(0.6)
                            "It took her a moment to adjust to a comfortable position."
                            scene HighresScreenshot00230 with Dissolve(0.6)
                            Kalyskah "Oh, you look lonely, come here…"
                            scene HighresScreenshot00231 with Dissolve(0.6)
                            "She started to suck on another of the tentacles, unaware that tendrils were creeping all over her body."
                            scene HighresScreenshot00232 with Dissolve(0.6)
                            "Fnding her weak spot was just a game so the creature could get the upper hand."
                            scene HighresScreenshot00233 with Dissolve(0.6)
                            "Her moanings were getting louder at each second."
                            scene HighresScreenshot00226 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00225 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00224 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00223 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00223 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00224 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00225 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00226 with Dissolve(0.6)
                            window hide # hides the window.
                            $ renpy.pause()
                            scene HighresScreenshot00233 with Dissolve(0.6)
                            "It didn’t take long for the vampire’s submissive nature to kick in."
                            scene HighresScreenshot00234 with Dissolve(0.6)
                            "The next thing she knew, she was…"
                            scene HighresScreenshot00235 with Dissolve(0.6)
                            "...being lifted in the air, completely dominated by the tentacles."
                            scene HighresScreenshot00236 with Dissolve(0.6)
                            "But she didn’t fight back this time.. She was enjoying it."
                            scene HighresScreenshot00237 with Dissolve(0.6)
                            "She submitted to the creature it spread her open and gave her a pleasure she could have only imagined."

                            jump Merishya_Return



                        "Kick it and look for Merishya":
                            $IsKalyNaked = 1
                            jump KalyKickTheThing
                    
                "Kick it and look for Merishya (Leads to ending the novel)":
                    jump KalyKickTheThing

                    


return



label KalyKickTheThing:
    play music "audio/kicked_the_tentacles.mp3" loop fadeout 1.0
    if IsKalyNaked == 0:
        scene HighresScreenshot00151 with hpunch
        #Camera Shake
        Kalyskah "No! Just– no!"
        scene HighresScreenshot00152 with Dissolve(0.6)
        Kalyskah "Get The fuck out of my sight!"
        scene HighresScreenshot00153 with Dissolve(0.6)
        "The creatures start to retreat in fear."
        scene HighresScreenshot00154 with Dissolve(0.6)
        "The vampire shows her fangs and get’s ready for a fight."
        scene HighresScreenshot00155 with Dissolve(0.6)
        "She waits for it…"
        scene HighresScreenshot00156 with Dissolve(0.6)
        "And waits...."
        scene HighresScreenshot00157 with Dissolve(0.6)
        "But they were already gone."
        scene HighresScreenshot00158 with Dissolve(0.6)
        Kalyskah "{i}{color=#DCDCDC}*Phew* That was weird.."
        scene HighresScreenshot00159 with Dissolve(0.6)
        Kalyskah "Merishya, are you there?"
        scene HighresScreenshot00160 with Dissolve(0.6)
        Kalyskah "I hope she’s not in trouble... I was a bit harsh with her."
        scene HighresScreenshot00161 with Dissolve(0.6)
        Kalyskah "Oh, whom am I kidding? She’s probably fucking a tree."
        scene HighresScreenshot00162 with Dissolve(0.6)
        Kalyskah "Merishya! If you are hiding somewhere out there, I will go and give you a spank you will never forget!"

        # Kalyskah "Merishya, we need to leave this place, now!"
        # Merishya "Are you sure? That little thing doesn’t seem too harmful… I think we can have some fun before we continue our journey!"

        # menu:
        #     "I am sure (ends the novel)":
        #         Kalyskah "I am sure, we need to focus. Besides, this is all too much for me."
        #         Merishya "That’s disappointing, but alright. Let’s leave"


        #     "Maybe we can stay for a bit":
        #         Kalyskah "Hm, you might be right.. Fine. Let us head back and attract the creature. I would rather enjoy watching you melt at the touch of it." 

    else:
        scene HighresScreenshot00151 with hpunch
        #Camera Shake
        Kalyskah "No! Just– no!"
        scene HighresScreenshot00152 with Dissolve(0.6)
        Kalyskah "Get The fuck out of my sight!"
        scene HighresScreenshot00153 with Dissolve(0.6)
        "The creatures start to retreat in fear."
        scene HighresScreenshot00154 with Dissolve(0.6)
        "The vampire shows her fangs and get’s ready for a fight."
        scene HighresScreenshot00155 with Dissolve(0.6)
        "She waits for it…"
        scene HighresScreenshot00156 with Dissolve(0.6)
        "And waits...."
        scene HighresScreenshot00157 with Dissolve(0.6)
        "But they were already gone."
        scene HighresScreenshot00158 with Dissolve(0.6)
        Kalyskah "{i}{color=#DCDCDC}*Phew* That was weird.."
        scene HighresScreenshot00159 with Dissolve(0.6)
        Kalyskah "Merishya, are you there?"
        scene HighresScreenshot00160 with Dissolve(0.6)
        Kalyskah "I hope she’s not in trouble... I was a bit harsh with her."
        scene HighresScreenshot00161 with Dissolve(0.6)
        Kalyskah "Oh, whom am I kidding? She’s probably fucking a tree."
        scene HighresScreenshot00162 with Dissolve(0.6)
        Kalyskah "Merishya! If you are hiding somewhere out there, I will go and give you a spank you will never forget!"

        # Kalyskah "Merishya, we need to leave this place, now!"
        # Merishya "Are you sure? That little thing doesn’t seem too harmful… I think we can have some fun before we continue our journey!"

        # menu:
        #     "I am sure (ends the novel)":
        #         Kalyskah "I am sure, we need to focus. Besides, this is all too much for me."
        #         Merishya "That’s disappointing, but alright. Let’s leave"


        #     "Maybe we can stay for a bit":
        #         Kalyskah "Hm, you might be right.. Fine. Let us head back and attract the creature. I would rather enjoy watching you melt at the touch of it." 



    scene black with Dissolve(0.6)
    "This part is in development and more content will be added here."
    "For now I bring you back to the first choice menu"
    play music "audio/forest_exploration.mp3" loop fadeout 1.0
    jump Choice_2

return


label Merishya_Return:
    scene HighresScreenshot00203 with Dissolve(0.6)
    "So lost in pleasure, Kalyskah started to lose track of the time."
    scene HighresScreenshot00205 with Dissolve(0.6)
    "Until she looked up and realised she had an audience."
    scene HighresScreenshot00206 with Dissolve(0.6)
    Merishya "Oh my! Kalyskah, if you wanted to be left alone to have fun, you could have just told me!"
    scene HighresScreenshot00207 with Dissolve(0.6)
    Merishya "Look at you now… Such a lovely sight!"
    scene HighresScreenshot00208 with Dissolve(0.6)
    "Kalyskah looks back to the succubus embarrassed."
    "She could have turned into mist and left that place at once."
    "She could have overpowered the creature with her inhuman strength."
    scene HighresScreenshot00205 with Dissolve(0.6)
    "Instead, she just looked up to her friend, embarrassed, but at the same time she was feeling so hot that she couldn’t think about gathering the strength to stop it."

    scene HighresScreenshot00209 with Dissolve(0.6)
    Merishya "Oh, don’t look at me like this! Would you mind if I joined in?"

    scene black with Dissolve(0.6)
    "This part is in development and more content will be added here."
    "For now I bring you back to the first choice menu"
    play music "audio/forest_exploration.mp3" loop fadeout 1.0
    jump Choice_2


    # menu:
    #     "Let Merishya join":

        
    #     "Tell Merishya to leave":



return