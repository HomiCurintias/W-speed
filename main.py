#//> anyone can use this                                                        <\\# (nice desing, right? :3)
#//> i doing this for fun                                                       <\\#
#//> thats probaly the worst lenaguge (and english) u ever seen                 <\\#
#//> if u are think this is a shit                                              <\\#
#//> u're right                                                                 <\\#
#//> or                                                                         <\\#
#//> if u apreciate this                                                        <\\#
#//> u have mental problems                                                     <\\#

###########################################################################################################
# theres no documentation for ts, if u (idk why u would do that) use this leanguege, read the interpreter #
###########################################################################################################

import sys

path = sys.argv[1] #chatGPT also said is imporant to validate and bla bla bla, but i dont think like him
variables = {}
skip = False

try: #chatGPT told me thats important \_('-')_/
    with open(path, "r") as file: #its also a chatGPT ideia, prob the most useless shit ever created
        for line in file:
            tokens = line.strip().split()

            if not tokens:
                continue

            if skip:
                if tokens[0] == "8=D": #cock of destiny (this is for makes the if ends, sounds nice until u draw 13 cocks per code)
                    skip = False
                continue

            if tokens[0] == "var": #idk wtf tokens mean, but i think thats a cool name
                typ = tokens[1]
                name = tokens[2]
                value = tokens[3]

                if typ == "int": #interger (i wrote this right?)
                    variables[name] = int(value)
                elif typ == "str": #string ig
                    variables[name] = value
                else:
                    print("type error")
                    sys.exit(1)

            elif tokens[0] == "print": #thats not for printing the screen
                if len(tokens) != 2:
                    print("syntax error")
                    sys.exit(1)

                name = tokens[1]
                if name in variables:
                    print(variables[name])
                else:
                    print(name)

            elif tokens[0] == "if": #comparation type shi (i wrote comparation right?)
                if len(tokens) != 4:
                    print("syntax error")
                    sys.exit(1)

                left, op, right = tokens[1], tokens[2], tokens[3]

                left_val = variables[left] if left in variables else int(left)
                right_val = variables[right] if right in variables else int(right)

                ##########################
                # WORST PART OF THE CODE #
                ##########################
                #i sooooo good making desings man
                                
                if op == "==": 
                    result = left_val == right_val
                elif op == "!=":
                    result = left_val != right_val
                elif op == "<":
                    result = left_val < right_val
                elif op == ">":
                    result = left_val > right_val
                elif op == "<=":
                    result = left_val <= right_val
                elif op == ">=":
                    result = left_val >= right_val
                else:
                    print("unknown operator")
                    sys.exit(1)

                if not result:
                    skip = True
                
                #it ended ig

except FileNotFoundError: #chatGPT told me thats important
    print("file not found")
    sys.exit(1)

#i feel like a hacker using this dark VScode theme
#i also create web-applications
#pay me to get the best website ever created (or not)
#reasons why to do that:
#Why not?
#I program in flask
#i know how to program (ig)
#i beatiful (in india)
#i prefer kasane teto instead of hatsune miku
