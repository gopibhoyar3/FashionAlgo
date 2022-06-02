#occasion = ["party","festival"  ]

color = {"white":["gray","light brown","dark brown","purple","navy blue","green","burgundy"],
         "light gray":["gray","black","light brown","dark brown","purple","navy blue","green","burgundy"],
         "black":["gray","black","purple","navy blue","green","burgundy"],
         "cream":["white","gray","light brown","dark brown","purple","navy blue","green","burgundy"],
         "dark brown":["white","light brown","dark brown","navy blue","green"],
         "gray":[],
         "green":[],         
         "blue":["white","gray","black","light brown","dark brown","purple","navy blue","green","burgundy"],
         "navy blue":["white","gray","black","light brown","dark brown","purple","navy blue","green","burgundy"],
         "burgundy":["white","gray","black","light brown","navy blue","green","burgundy"],
         }

def fashion(shirts,pants):
    
    if len(shirts)==0 and len(pants)==0:
        return "Please enter something!!"
    if len(shirts)==0:
        return "Sorry, no shirt colors"
    if len(pants)==0:
        return "Sorry, no pant colors"
    
    for shirt in shirts:
        for pantColor in color[shirt]:
            if pantColor in pants:
                print(f"{shirt}--{pantColor}, ")



print("Enter the shirt colors you have: (write 'done' when finished!) ")
shirts = set()
while True:
    i = input("Enter a shirt color: ")
    if i=="done":
        break
    if i not in color:
        print("Enter a valid color!")
    else:
        shirts.add(i)

pants = set()
print("Enter the pant colors you have: ")
while True:
    i = input("Enter a pant color: ")
    if i=="done":
        break
    if i not in color:
        print("Enter a valid color!")
    else:
        pants.add(i)
    
fashion(shirts,pants)
