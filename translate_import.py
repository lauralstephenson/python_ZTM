#Translator
#Specifically for Japanese
from translate import Translator

#First, creat a text filse with something in it to translate
#then convert it to the langauge you want. ja is japanese
try:
    with open("test.text", mode ="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        #This prints the translation in your command line
        print(translation)
        #this translates the file and puts the translation
        #into a new file
        with open("./test-ja.txt", mode='w')as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("Checkf your file path, please!")

#for a command line version use:
#translate-cli -t ja "This is a pen."