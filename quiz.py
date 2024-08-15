def quiz():
     score = 0
     keys = list(qans.keys())
     values  = list(qans.values())
    
     for i,j in  zip(keys,values):
        print(i)
        ans=input("Enter Your answer:")
        if ans==j:
            score = score+1
            
        else:
            print("Out")
            break
     print("final score:",score)

skill =input("Enter Your skill:").lower()
if skill=="html":
    qans = {'What is the extension for saving file in html?':'.html',
    'which tag is used to create forms in html?':'<form>'
    }
    quiz()
        

                
elif skill=="css":
    qans = {'Which function is used to change the font style?':'font-family',
    'which function is used to create annimation in css?':'@mediaquery'
}
    quiz()
elif skill=="javascript":
    qans = {'What is the function to print statement in console?':'console.log()',
    'Is elif use in javascript?':'No'
    }
    quiz()
else:
    print("Invalid skill")

