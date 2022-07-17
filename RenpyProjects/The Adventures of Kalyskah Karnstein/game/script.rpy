define Kalyskah = Character("Kalyskah", color = "#ADD8E6")
define Merishya = Character("Merishya", color = "#DC143C")
define Story = Character("", color = "#808080")

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

    scene HighresScreenshot00001 with Dissolve(0.8)
    Story "It was a tiresome morning of august when the vampire Kalyskah had finally decided to listen to the request of Merishya Sarinoza"
    Story "The demoness told her about a place in the country of Gormakar, far from Thulgatha, where they originally met."
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00002 with Dissolve(0.8)
    Story "It was said that this place contained a very specific resonance that could help the demoness back home"
    Story "Kalyskah would rather not go, but a sense of honour and gratitude urged her to help the demoness with her predicament."
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00003 with Dissolve(0.8)
    Story "Hours of hiking have turned to days… Kalyskah would stay quiet for most of the time. But she could see the demoness humming all the way."
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00004 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00005 with Dissolve(0.8)
    Kalyskah "Demoness… I am confident we have already seen this tree."
    scene HighresScreenshot00006 with Dissolve(0.8)
    Story "They stared into the horizon. Merishya just wiggled her tail:"
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
    Story "The Sun was high in the sky, hours were passing quickly."
    Story "Kalyskah was grateful she was well fed so that the daylight couldn’t harm her skin."
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00017 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00018 with Dissolve(0.8)
    Story "Meanwhile, Merishya was quiet."
    Story "Thoughtful, even.."
    scene HighresScreenshot00019 with Dissolve(0.8)
    Merishya "I’m sure I’ve seen this rock.."
    scene HighresScreenshot00020 with Dissolve(0.8)
    Merishya "Hmm…"
    scene HighresScreenshot00021 with Dissolve(0.8)
    Story "That was it. That was the last humming the vampire could endure to listen."
    Story "She stopped, glaring to the succubus."
    Story "Something had finally sinked in."

    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00022 with Dissolve(0.8)
    Merishya "What’s the problem?"

    #*Render of them looking around. Kalyskah is annoyed and impatient*

    scene HighresScreenshot00023 with Dissolve(0.8)
    Kalyskah "We are lost, are we not?"
    scene HighresScreenshot00024 with Dissolve(0.8)
    Merishya "Lost is such a strong word. Let’s say… We are taking a detour!"
    Story "The truth was exposed, there was no reason to fight over it. Kalyskah calmed down."
    scene HighresScreenshot00025 with Dissolve(0.8)
    Kalyskah "Let us sit, Merishya."
    scene HighresScreenshot00026 with Dissolve(0.8)
    window hide # hides the window.
    $ renpy.pause()
    scene HighresScreenshot00027 with Dissolve(0.8)
    Merishya "Why? Don’t tell me you’re tired, Kalyskah."
    scene HighresScreenshot00028
    Kalyskah "Vampires do not get tired. I just want a break. Besides, we need to plan what we’ll do next, walking in circles will do us no good."
    scene HighresScreenshot00029 with Dissolve(0.8)
    Kalyskah "We have been walking for hours and this place…"
    scene HighresScreenshot00030 with Dissolve(0.8)
    Kalyskah "Brings back memories."
    scene HighresScreenshot00031 with Dissolve(0.8)
    Story "Merishya could sense the trouble in the eyes of her companion. She nodded."
    $ renpy.pause()


    return
