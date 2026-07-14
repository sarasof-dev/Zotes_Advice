
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
import random
from turtle import delay 
from pathlib import Path

folder=Path(__file__).parent
assets=folder / "assets"

#zote list
zote_precepts = [
    "Precept One: 'Always Win Your Battles'. Losing a battle earns you nothing and teaches you nothing. Win your battles, or don't engage in them at all!",

    "Precept Two: 'Never Let Them Laugh at You'. Fools laugh at everything, even at their superiors. But beware, laughter isn't harmless! Laughter spreads like a disease, and soon everyone is laughing at you. You need to strike at the source of this perverse merriment quickly to stop it from spreading.",

    "Precept Three: 'Always Be Rested'. Fighting and adventuring take their toll on your body. When you rest, your body strengthens and repairs itself. The longer you rest, the stronger you become.",

    "Precept Four: 'Forget Your Past'. The past is painful, and thinking about your past can only bring you misery. Think about something else instead, such as the future, or some food.",

    "Precept Five: 'Strength Beats Strength'. Is your opponent strong? No matter! Simply overcome their strength with even more strength, and they'll soon be defeated.",

    "Precept Six: 'Choose Your Own Fate'. Our elders teach that our fate is chosen for us before we are even born. I disagree.",

    "Precept Seven: 'Mourn Not the Dead'. When we die, do things get better for us or worse? There's no way to tell, so we shouldn't bother mourning. Or celebrating for that matter.",
    
    "Precept Eight: 'Travel Alone'. You can rely on nobody, and nobody will always be loyal. Therefore, nobody should be your constant companion.",

    "Precept Nine: 'Keep Your Home Tidy'. Your home is where you keep your most prized possession - yourself. Therefore, you should make an effort to keep it nice and clean.",
   
    "Precept Ten: 'Keep Your Weapon Sharp'. I make sure that my weapon, 'Life Ender', is kept well-sharpened at all times. This makes it much easier to cut things.",
    
    "Precept Eleven: 'Mothers Will Always Betray You'. This Precept explains itself.",
    
    "Precept Twelve: 'Keep Your Cloak Dry'. If your cloak gets wet, dry it as soon as you can. Wearing wet cloaks is unpleasant, and can lead to illness.",
    
    "Precept Thirteen: 'Never Be Afraid'. Fear can only hold you back. Facing your fears can be a tremendous effort. Therefore, you should just not be afraid in the first place.",
    
    "Precept Fourteen: 'Respect Your Superiors'. If someone is your superior in strength or intellect or both, you need to show them your respect. Don't ignore them or laugh at them.",
    
    "Precept Fifteen: 'One Foe, One Blow'. You should only use a single blow to defeat an enemy. Any more is a waste. Also, by counting your blows as you fight, you'll know how many foes you've defeated.",
    
    "Precept Sixteen: 'Don't Hesitate'. Once you've made a decision, carry it out and don't look back. You'll achieve much more this way.",
    
    "Precept Seventeen: 'Believe In Your Strength'. Others may doubt you, but there's someone you can always trust. Yourself. Make sure to believe in your own strength, and you will never falter.",
    
    "Precept Eighteen: 'Seek Truth in the Darkness'. This Precept also explains itself.",
    
    "Precept Nineteen: 'If You Try, Succeed'. If you're going to attempt something, make sure you achieve it. If you do not succeed, then you have actually failed! Avoid this at all costs.",
    
    "Precept Twenty: 'Speak Only the Truth'. When speaking to someone, it is courteous and also efficient to speak truthfully. Beware though that speaking truthfully may make you enemies. This is something you'll have to bear.",
    
    "Precept Twenty-One: 'Be Aware of Your Surroundings'. Don't just walk along staring at the ground! You need to look up every so often, to make sure nothing takes you by surprise.",
    
    "Precept Twenty-Two: 'Abandon the Nest'. As soon as I could, I left my birthplace and made my way out into the world. Do not linger in the nest. There is nothing for you there.",
    
    "Precept Twenty-Three: 'Identify the Foe's Weak Point'. Every foe you encounter has a weak point, such as a crack in their shell or being asleep. You must constantly be alert and scrutinising your enemy to detect their weakness!",
    
    "Precept Twenty-Four: 'Strike the Foe's Weak Point'. Once you have identified your foe's weak point as per the previous Precept, strike it. This will instantly destroy them.",
    
    "Precept Twenty-Five: 'Protect Your Own Weak Point'. Be aware that your foe will try to identify your weak point, so you must protect it. The best protection? Never having a weak point in the first place.",
    
    "Precept Twenty-Six: 'Don't Trust Your Reflection'. When peering at certain shining surfaces, you may see a copy of your own face. The face will mimic your movements and seems similar to your own, but I don't think it can be trusted.",
    
    "Precept Twenty-Seven: 'Eat As Much As You Can'. When having a meal, eat as much as you possibly can. This gives you extra energy, and means you can eat less frequently.",
    
    "Precept Twenty-Eight: 'Don't Peer Into the Darkness'. If you peer into the darkness and can't see anything for too long, your mind will start to linger over old memories. Memories are to be avoided, as per Precept Four.",
    
    "Precept Twenty-Nine: 'Develop Your Sense of Direction'. It's easy to get lost when travelling through winding, twisting caverns. Having a good sense of direction is like having a magical map inside of your head. Very useful.",
    
    "Precept Thirty: 'Never Accept a Promise'. Spurn the promises of others, as they are always broken. Promises of love or betrothal are to be avoided especially.",
    
    "Precept Thirty-One: 'Disease Lives Inside of Dirt'. You'll get sick if you spend too much time in filthy places. If you are staying in someone else's home, demand the highest level of cleanliness from your host.",
    
    "Precept Thirty-Two: 'Names Have Power'. Names have power, and so to name something is to grant it power. I myself named my nail 'Life Ender'. Do not steal the name I came up with! Invent your own!",
    
    "Precept Thirty-Three: 'Show the Enemy No Respect'. Being gallant to your enemies is no virtue! If someone opposes you, they don't deserve respect or kindness or mercy.",
    
    "Precept Thirty-Four: 'Don't Eat Immediately Before Sleeping'. This can cause restlessness and indigestion. It's just common sense.",
    
    "Precept Thirty-Five: 'Up is Up, Down is Down'. If you fall over in the darkness, it can be easy to lose your bearing and forget which way is up. Keep this Precept in mind!",
    
    "Precept Thirty-Six: 'Eggshells are brittle'. Once again, this Precept explains itself.",
    
    "Precept Thirty-Seven: 'Borrow, But Do Not Lend'. If you lend and are repayed, you gain nothing. If you borrow but do not repay, you gain everything.",
    
    "Precept Thirty-Eight: 'Beware the Mysterious Force'. A mysterious force bears down on us from above, pushing us downwards. If you spend too long in the air, the force will crush you against the ground and destroy you. Beware!",
    
    "Precept Thirty-Nine: 'Eat Quickly and Drink Slowly'. Your body is a delicate thing and you must fuel it with great deliberation. Food must go in as fast as possible, but fluids at a slower rate.",
    
    "Precept Forty: 'Obey No Law But Your Own'. Laws written by others may inconvenience you or be a burden. Let your own desires be the only law.",
    
    "Precept Forty-One: 'Learn to Detect Lies'. When others speak, they usually lie. Scrutinise and question them relentlessly until they reveal their deceit.",
    
    "Precept Forty-Two: 'Spend Geo When You Have It'. Some will cling onto their Geo, even taking it into the dirt with them when they die. It is better to spend it when you can, so you can enjoy various things in life.",
    
    "Precept Forty-Three: 'Never Forgive'. If someone asks forgiveness of you, for instance a brother of yours, always deny it. That brother, or whoever it is, doesn't deserve such a thing.",
    
    "Precept Forty-Four: 'You Can Not Breathe Water'. Water is refreshing, but if you try to breathe it you are in for a nasty shock.",
    
    "Precept Forty-Five: 'One Thing Is Not Another'. This one should be obvious, but I've had others try to argue that one thing, which is clearly what it is and not something else, is actually some other thing, which it isn't. Stay on your guard!",
    
    "Precept Forty-Six: 'The World is Smaller Than You Think'. When young, you tend to think that the world is vast, huge, gigantic. It's only natural. Unfortunately, it's actually quite a lot smaller than that. I can say this, now having travelled everywhere in the land.",
    
    "Precept Forty-Seven: 'Make Your Own Weapon'. Only you know exactly what is needed in your weapon. I myself fashioned 'Life Ender' from shellwood at a young age. It has never failed me. Nor I it.",
    
    "Precept Forty-Eight: 'Be Careful With Fire'. Fire is a type of hot spirit that dances about recklessly. It can warm you and provide light, but it will also singe your shell if it gets too close.",
    
    "Precept Forty-Nine: 'Statues are Meaningless'. Do not honour them! No one has ever made a statue of you or I, so why should we pay them any attention?",
    
    "Precept Fifty: 'Don't Linger on Mysteries'. Some things in this world appear to us as puzzles. Or enigmas. If the meaning behind something is not immediately evident though, don't waste any time thinking about it. Just move on.",
    
    "Precept Fifty-One: 'Nothing is Harmless'. Given the chance, everything in this world will hurt you. Friends, foes, monsters, uneven paths. Be suspicious of them all.",
    
    "Precept Fifty-Two: 'Beware the Jealousy of Fathers'. Fathers believe that because they created us we must serve them and never exceed their capabilities. If you wish to forge your own path, you must vanquish your father. Or simply abandon him.",
    
    "Precept Fifty-Three: 'Do Not Steal the Desires of Others'. Every creature keeps their desires locked up inside of themselves. If you catch a glimpse of another's desires, resist the urge to claim them as your own. It will not lead you to happiness.",
    
    "Precept Fifty-Four: 'If You Lock Something Away, Keep the Key'. Nothing should be locked away for ever, so hold onto your keys. You will eventually return and unlock everything you hid away.",
    
    "Precept Fifty-Five: 'Bow to No-one'. There are those in this world who would impose their will on others. They claim ownership over your food, your land, your body, and even your thoughts! They have done nothing to earn these things. Never bow to them, and make sure to disobey their commands.",
    
    "Precept Fifty-Six: 'Do Not Dream'. Dreams are dangerous things. Strange ideas, not your own, can worm their way into your mind. But if you resist those ideas, sickness will wrack your body! Best not to dream at all, like me.",
    
    "Precept Fifty-Seven: 'Obey All Precepts'. Most importantly, you must commit all of these Precepts to memory and obey them all unfailingly. Including this one! Hmm. Have you truly listened to everything I've said? Let's start again and repeat the 'Fifty-Seven Precepts of Zote'",
    ]

zote_intro = [
    "Yes, your eyes do not deceive you. I am Zote the Mighty, a knight of great renown. Tremble before me!",
    
    "I am Zote the Mighty. Yes, yes. All glory to me. But I don't have time for your adulation! I must rest and prepare for my next journey down.",
    
    "I am Zote the Mighty, a knight of great renown. My weapon, 'Life Ender,' has struck down hundreds of foes. Begone, or you'll be next!",
    
    "I am Zote the Mighty! And as soon as I draw my nail, 'Life Ender', your laughter will turn into terror!",
    
    "I have been fighting my whole life. I've slain hundreds, nay thousands, of foes. I am Zote, the Mighty",
    ]


#window set up
root = tk.Tk()
root.title("Zote's Precepts")
root.geometry("1000x563")
root.configure(bg="black")

#background thingy (canvas)
background_image = tk.PhotoImage(file=str(assets / "BackgroundZ.png"))

canvas = tk.Canvas(root, width=1000, height=563, highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

canvas.create_image(0, 0, anchor="nw", image=background_image)

#button style
style = ttk.Style()
style.configure("Rounded.TButton", 
                font=("Trajan Pro", 12, "bold"),
                padding=5,  # Increases padding to create a rounded effect
                relief="flat",
                background="#000000",
                foreground="#000000",
                borderwidth=15)

#Zotes frames
zote_frame_c_og = Image.open(assets / "Zote_closed.png").convert("RGBA")  # Open image with transparency Pillow (tk not support transparency)
zote_frame_o_og = Image.open(assets / "Zote_open.png").convert("RGBA")

zote_frame_c = zote_frame_c_og.resize((int(zote_frame_c_og.width*0.7),int(zote_frame_c_og.height*0.7))) 
zote_frame_o = zote_frame_o_og.resize((int(zote_frame_o_og.width*0.7),int(zote_frame_o_og.height*0.7)))

#conversion for tk
zote_frame_c_tk = ImageTk.PhotoImage(zote_frame_c)
zote_frame_o_tk = ImageTk.PhotoImage(zote_frame_o)

#funciones 

def typewriter(label, text, index=0, delay=70, callback=None): #prints, waits, updates and goes
    button_block()
    if index < len(text):
        label.config(text=text[:index + 1])
        root.after(delay, typewriter, label, text, index + 1, delay, callback) 
    else:
        button_unblock()
        if callback:
            root.after(300, callback)
            
def talking(label, text, index=0):
    if index < len(text):
        label.config(text=text[:index + 1])
        
        #frames
        if index % 2 == 0: 
            canvas.itemconfig(zote_image, image=zote_frame_o_tk)  # Mouth open
        else:
            canvas.itemconfig(zote_image, image=zote_frame_c_tk)  # Mouth closed

        label.after(70, talking, label, text, index+1)
    else:
        canvas.itemconfig(zote_image, image=zote_frame_c_tk)    

def button_block(): #no button spamming
    show_button.config(state="disable")
    show_buttonr.config(state="disable")

def button_unblock(): #no button spamming
    show_button.config(state="normal")
    show_buttonr.config(state="normal")    
            
def show_ran_p():
    precept_Label.config(text="")  
    ranchoice= random.choice(zote_precepts)
    typewriter(precept_Label, ranchoice)
    talking(precept_Label, ranchoice)
    precept_input.delete(0, tk.END)

    
def show_buttons():
    delay=50
    precept_input.place(x=250,y=435)
    show_button.config(command=show_precept)
    show_button.place(x=195,y=465)
    show_buttonr.config(command=show_ran_p)
    show_buttonr.place(x=335,y=465)

def ask():
    ask_Label.place(x=150,y=400)
    typewriter(ask_Label, "What precept would you like to know?", callback=show_buttons)
    talking(ask_Label, "What precept would you like to know?")

def show_precept():
    try:
        number = int(precept_input.get()) 
        if 1<=number < len(zote_precepts):
            precept_Label.config(text="")  # Clear text before showing new one
            typewriter(precept_Label, zote_precepts[number - 1]) #number -1 since lists in pythoon start at 0 
            talking(precept_Label, zote_precepts[number - 1])
            precept_input.delete(0, tk.END)
        else: 
            typewriter(precept_Label,text="There are 57 precepts no more no less...")
            talking(precept_Label,text="There are 57 precepts no more no less...")
            precept_input.delete(0, tk.END)

    except ValueError:
        typewriter(precept_Label,text="Do not mock Zote the Mighty. Cross me again, and you'll find out why they call my weapon 'Life Ender'")
        talking(precept_Label,text="Do not mock Zote the Mighty. Cross me again, and you'll find out why they call my weapon 'Life Ender'")
        precept_input.delete(0, tk.END)

    
#zotes canvas (for transparency since label adds bg to the pic)
zote_image = canvas.create_image(750, 372, anchor="nw", image=zote_frame_c_tk)

#texts label
precept_Label = tk.Label( root, text="", font=("Trajan Pro", 16, 'bold'),fg="white", bg="#000000", wraplength=700)
precept_Label.place(x=172,y=75)

#ask for number label  
ask_Label = tk.Label(root,text="", font=("Trajan Pro", 14, 'bold'),fg="white", bg="#000000")

#input field
precept_input = tk.Entry(root, font=("Trajan Pro", 12, 'bold'),fg="white", bg="#000000")

#button precepts
show_button = ttk.Button(root, text="Listen",style="Rounded.TButton", command=show_precept)

#button random    
show_buttonr = ttk.Button(root, text="Let Zote guide you",style="Rounded.TButton", command=show_ran_p)

#start mainloop
intro = random.choice(zote_intro)

typewriter(precept_Label, intro, callback=ask)
talking(precept_Label, intro)

#run app
root.mainloop()