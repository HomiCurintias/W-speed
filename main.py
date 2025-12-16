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

import sys #only 1 library? +999 aura

path = sys.argv[1] #chatGPT also said is imporant to validate and bla bla bla, but i dont think like him
variables = {} #stairs
Params = {} #stairs
fns = {} #stairs
skip = False
current_func = None

try:
    with open(path, "r") as file:
        for line in file:
            tokens = line.strip().split()

            if not tokens:
                continue

            if current_func:
                if tokens[0] == "ItsOver": #mogged
                    current_func = None
                    skip = False
                else:
                    fns[current_func]["body"].append(line.strip())
                continue

            if skip:
                if tokens[0] == "8=D": #cock of the destiny
                    skip = False
                continue

            if tokens[0] == "var": #variables oooowowowooooo
                typ = tokens[1]
                name = tokens[2]
                value = tokens[3]

                if typ == "int": #i feel like einstein writing "int"
                    variables[name] = int(value)
                elif typ == "str": #same
                    variables[name] = value
                else:
                    print("type error")
                    print("code = 1")
                    sys.exit(1)

            elif tokens[0] == "print": #no, its don't print ur screen
                if len(tokens) != 2:
                    print("syntax error")
                    print("code = 1")
                    sys.exit(1)

                name = tokens[1]
                if name in variables:
                    print(variables[name])
                else:
                    print(name)

            elif tokens[0] == "if": #comparative type shi
                if len(tokens) != 4:
                    print("syntax error")
                    print("code = 1")
                    sys.exit(1)

                left, op, right = tokens[1], tokens[2], tokens[3]

                left_val = variables[left] if left in variables else int(left)
                right_val = variables[right] if right in variables else int(right)

                ##########################
                # WORST PART OF THE CODE #
                ##########################

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
                    print("code = 1")
                    sys.exit(1)

                if not result:
                    skip = True
                
                #it ended ig

            elif tokens[0] == "func": #i feel like a genious rn
                fname = tokens[1]
                params = tokens[2:] #idk why we need the ":", but chatGPT told me thats important

                fns[fname] = {
                    "params": params,
                    "body": []
                } #its json? idk

                current_func = fname
                skip = True

            elif tokens[0] == "call": #this one was made by chatGPT ngl
                fname = tokens[1]
                args = tokens[2:]

                if fname not in fns:
                    print("function not found")
                    print("code = 1")
                    sys.exit(1)

                func = fns[fname]

                if len(args) != len(func["params"]):
                    print("wrong number of args")
                    print("code = 1")
                    sys.exit(1)

                local_vars = variables.copy()

                for p, a in zip(func["params"], args):
                    local_vars[p] = int(a) if a.isdigit() else variables.get(a, a)

                for cmd in func["body"]:
                    parts = cmd.split()
                    if parts[0] == "print":
                        name = parts[1]
                        print(local_vars[name] if name in local_vars else name)

except FileNotFoundError:
    print("file not found")
    print("code = 1")
    sys.exit(1)
