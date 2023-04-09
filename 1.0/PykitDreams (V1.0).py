import numpy as np
import sys
import os
import turtle
import random
import pygame
import turtle

class Computer:
    def __init__(self, company, model):
        self.company = company
        self.model = model

def hello():
  
    name = str(input("Enter your name: "))
    
    print("Hello there " + str(name) + "! Welcome to PykitDreams - a CodeMaster7000 Studios Python module designed to revolutionise the way you use your computers!"))
    
    
def fourfunctionscalculator():  
    
    operation = input("Please enter the symbol for the operation you would like to complete: ")

    number_1 = int(input("Please enter your first number: "))
    number_2 = int(input("Please enter the second number: "))

    if operation == '+':
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("Invalid operator.")

def TypingTest():
    # Typing Test by @CodeMaster7000
    
    from time import time
    
    def typingErrors(prompt):
        global iwords

        words = prompt.split()
        errors = 0

        for i in range(len(iwords)):
            if i in (0, len(iwords)-1):
                if iwords[i] == words[i]:
                    continue
            else:
                errors +=1
                else:
                    if iwords[i] == words[i]:
                        if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                            continue
                        else:
                            errors += 1
                    else:
                        errors += 1
        return errors

    def typingSpeed(iprompt, stime, etime):
        global time
        global iwords

        iwords = iprompt.split()
        twords = len(iwords)
        speed = twords / time

        return speed

    def timeElapsed(stime, etime):
        time = etime - stime

        return time

    if __name__ == '__main__':
        prompt = "\n\nA turquoise-blue stream wound its merry way through the forest. Babbling and burbling, it sprung over the limestone rocks in its way. Pebbles whisked about in the under wash like pieces of glitter. Streams are the liquid soul of the forest, and this one was glowing. Chords of soft light speared down from above, bathing its surface in gold. It was glinting with little sparkles, like a thousand diamonds blessed with an inner fire. A galaxy of dragonflies fizzed through the beams of light, wings a-glitter in the sun."
        print("TYPE THIS: ", prompt,"")

        input("\nPress 'Enter' when you are ready!")

        stime = time()
        iprompt = input()
        etime = time()

        time = round(timeElapsed(stime, etime), 2)
        speed = typingSpeed(iprompt, stime, etime)
        errors = typingErrors(prompt)

        print("Total time elapsed:", time, "s")
        print("Mean typing speed:", speed, "words/minute")
        print("With a total of:", errors, "errors")
