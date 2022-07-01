from posixpath import split
from tracemalloc import start
 
file = open("Program.txt", "r")
 
FunctName = ""
 
VarDict = {}
FunctDict = {}
FunctDictLines = {}
 
lines = file.readlines()
 
CurrentLineFORFunctions = 1
 
xx = 1
x = 1
 
CurrentLine = 1
 
CheckFuncLines = 1
 
CL = 0
starttln = 0
 
for line in lines:
    chars = line.split(" ")
 
    #calling the functions
    if chars[0] == "call":
        Name = chars[1]
        functstuff = FunctDictLines.get(Name)
        stln = functstuff[0]
        enln = functstuff[1]
        RunFunction(stln, enln, CurrentLineFORFunctions)

    #variable assignment
    if len(chars) > 2:
        if chars[2].strip("\n") == "START":
            starttln = CurrentLine
            for LINE in lines:
                CL += 1
                charss = LINE.split(" ")
                if charss[0].strip("\n") == "STOP":
                    FINALLINE = CL
                continue
        
    
        if chars[1] == "=":
            VarDict.update({chars[0]: chars[2]})
        
    if CurrentLine > starttln and CurrentLine < FINALLINE:
        continue
    #print
    if chars[0] == "say":
        if chars[1] == '"':
            print(chars[2])
        else:
            x = chars[1].strip("\n")
            print(VarDict.get(x))
 
    #function assignment
    if chars[0] == "func":
        FunctDict.update({x: chars[1]})
        x += 1
        ENDLINE = CurrentLine
        if chars[2].strip("\n") == "START":
            FunctName = chars[1]
            #chekcs the current line
            for line in lines:
                STARTLINE = CurrentLine
                charsss = line.split(" ")
                if charsss[0].strip("\n") == "STOP":
                    LineArr = [STARTLINE, ENDLINE]
                    FunctDictLines.update({FunctName: LineArr})
                    xx += 1
                    break
                ENDLINE += 1
        def RunFunction(sll, enll, CurrentLineFORFunctionss):
            for line in lines:
                if CurrentLineFORFunctionss > sll and CurrentLineFORFunctionss < enll:
                    #variable assignment
                    chars = line.split(" ")
                    if len(chars) >= 2:
                        if chars[1] == "=":
                            VarDict.update({chars[0]: chars[2]})
                            
                    #print
                    if chars[0] == "say":
                        if chars[1] == '"':
                            print(chars[2])
                        else:
                            x = chars[1].strip("\n")
                            print(VarDict.get(x))
                    else:
                        continue
                CurrentLineFORFunctionss += 1
                    
                
            return
        
 
    #if statement
    
    #for loop
    
    #while loop
    CurrentLine += 1
 
