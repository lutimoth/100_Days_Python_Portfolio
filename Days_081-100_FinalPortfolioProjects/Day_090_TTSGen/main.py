import pyttsx3

with open('4085-0.txt', encoding="utf8") as f:
    lines = f.readlines()
    
print(lines)
engine = pyttsx3.init()

# engine.say(lines)
engine.save_to_file(lines, "audiobook.mp3")
engine.runAndWait()