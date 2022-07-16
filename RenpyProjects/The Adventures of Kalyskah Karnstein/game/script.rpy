﻿define Kalyskah = Character("Kalyskah", color = "#ADD8E6")
define Merishya = Character("Merishya", color = "#DC143C")


label splashscreen:
    #default persistent.game_language = 'eng'
    scene black
    show logo_1 with blinds
    $ renpy.pause(2.0, hard = True)
    hide logo_1 with blinds
    $ renpy.pause(1.0, hard = True)
    show logo_2 with wiperight
    $ renpy.pause(2.0, hard = True)
    hide logo_2 with wiperight
    $ renpy.pause(1.0, hard = True)
    #jump start
    #scene warning with Dissolve(0.5)
    #$ renpy.pause(4.0, hard = True)
return


label start:

    scene HighresScreenshot00001 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00002 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00003 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00004 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00005 with Dissolve(0.8)
    Kalyskah "Demoness… I am confident we have already seen this tree."
    scene HighresScreenshot00006 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00007 with Dissolve(0.8)
    Merishya "Hmm…"
    scene HighresScreenshot00008 with Dissolve(0.8)
    Kalyskah "Merishya, are you sure we are in the correct place?"
    Merishya "Hmm…"
    scene HighresScreenshot00009 with Dissolve(0.8)
    Kalyskah "Demoness… Answer me!"
    scene HighresScreenshot00010 with Dissolve(0.8)
    Merishya "Well, it looks the same…Smells the same…."
    scene HighresScreenshot00011 with Dissolve(0.8)
    Kalyskah "You do not sound so sure!"
    scene HighresScreenshot00012 with Dissolve(0.8)
    Kalyskah "We have been walking for hours, even my forbearance has its limits."
    scene HighresScreenshot00013 with Dissolve(0.8)
    Merishya "It was around here somewhere, the portal."
    scene HighresScreenshot00014 with Dissolve(0.8)
    Kalyskah "Yes, yes! The red portal with fire on the other side."
    scene HighresScreenshot00013 with Dissolve(0.8)
    Merishya "Exactly! I can finally get back home; I just need to... Find it."
    scene HighresScreenshot00015 with Dissolve(0.8)
    Kalyskah "<sighs> Fair enough, lead the way…"

    scene HighresScreenshot00016 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00017 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00018 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00019 with Dissolve(0.8)
    Merishya "I’m sure I’ve seen this rock.."
    scene HighresScreenshot00020 with Dissolve(0.8)
    Merishya "Hmm…"
    scene HighresScreenshot00021 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00022 with Dissolve(0.8)
    Merishya "What’s the problem?"

    #*Render of them looking around. Kalyskah is annoyed and impatient*

    scene HighresScreenshot00023 with Dissolve(0.8)
    Kalyskah "We are lost, are we not?"
    scene HighresScreenshot00024 with Dissolve(0.8)
    Merishya "Lost is such a strong word. Let’s say… We are taking a detour!"
    scene HighresScreenshot00025 with Dissolve(0.8)
    Kalyskah "Let us sit, Merishya."
    scene HighresScreenshot00026 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00027 with Dissolve(0.8)
    Merishya "Why? Don’t tell me you’re tired, Kalyskah."
    scene HighresScreenshot00028
    Kalyskah "Vampires do not get tired. I just want a break."
    scene HighresScreenshot00029 with Dissolve(0.8)
    Kalyskah "We have been walking for hours and this place…"
    scene HighresScreenshot00030 with Dissolve(0.8)
    Kalyskah "Brings back memories."
    scene HighresScreenshot00031 with Dissolve(0.8)


    return
