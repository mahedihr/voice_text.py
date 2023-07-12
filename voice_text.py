print("Enter your name: ")

name = input(">")

import speech_recognition as sr
def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Please say something...")

        audio = r.listen(source)

        with open('sample.txt', 'w') as f:
            print(f"{name}: ",r.recognize_google(audio), file=f)

        try:
            print("You have said: \n " + r.recognize_google(audio))

        except Exception as e:

            print("Error : " + str(e))

if __name__ == "__main__":
            main()
