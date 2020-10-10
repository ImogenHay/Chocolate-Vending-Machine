## CHOCOLATE VENDING MACHINE V4 (frame layout)##
from tkinter import * #imports everything from tkinter
##Frames##
root = Tk() #creates a tkinter window
root.title("Chocolate Vending Machine:") #gives the tkinter window a title
frame = Frame(root)
frame.pack()

topleftframe = Frame(root) #creates frame 
topleftframe.pack(side=LEFT,anchor=N)#positions frame in top left of window

toprightframe = Frame(root)#creates frame
toprightframe.pack(side=RIGHT,anchor=N)#positions frame in top right of window

centreframe = Frame(root)#creates frame
centreframe.pack(side=RIGHT,anchor=N)#positions frame in centre of window

##Work out and display change##
def ShowPaid(): #creates function to work out change due
    quote = "Paid: " + str(paid.get()) + "p\n" #adds amount paid to quote, \n move onto next line
    change = int(paid.get()) - price.get()#works out amount of change needed
    if int(paid.get()) > price.get(): #selection and iteration so that only works out change if change is needed
        quote = quote + "You need " + str(change) + "p change.\n" #adds amount of change needed to quote
    else:
        quote = "Invalid amount" #selection to make sure no invalid data entered
    coins = [200,100,50,20,10,5,2,1] #array of the different coins that a vending machine can dispence
    x = 0 #variable used to move along the list
    while change > 0: #while loop and iteration so that only dispences coins if change is still needed
        while change >= coins[x]: #while loop and iteration so that coins of highest value possible dispensed
            change = change - coins[x] #amount of change due is decreased as change is given
            quote = quote + str(coins[x]) + "p dispensed\n" #add the coins dispensed to 'quote' variable,
                                                            #used casting to make coins str becuse rest of quote is string
        x = x + 1 #to move along list when coin has too high a value
    T.insert(END, quote+"\n")#insert 'quote' to text widget

##Option Box (Top Left)##
price = IntVar()#makes price the variable 
price.set(1)
chocolates = [["Mars            = £0.78",78],["Galaxy          = £0.99",99],["Dairy Milk      = £0.59",59],["EXIT",0]]
                #creates list of items available with their set prices
choose = Label(topleftframe, text="""Choose your favourite
         chocolate bar:""") #radiobuttons labelled so user knows what they are for, label put in top left frame
choose.pack(side=TOP) #positions label at top of frame

for i in range (0,len(chocolates)-1):#for loop creates button for each item in list
  choice = Radiobutton(topleftframe, #puts radiobutton in top left frame
                       text=chocolates[i][0], #puts name of chocolate bar and price on button
                       indicatoron = 0, #make the radiobuttons design that they are
                       width = 20, #defines width or each button
                       padx = 20, #makes all the buttons the same dimensions
                       variable=price, #makes the varialve the price
                       value=chocolates[i][1]) #makes the value the price
  choice.pack(side=TOP) #positions each radiobutton

choice = Radiobutton(topleftframe, #creates another radiobutton in top left frame
                       text=chocolates[i+1][0], #puts "EXIT" on button
                       indicatoron = 0, #makes the radiobutton the design that it is
                       width = 20, #defines the width of the button
                       padx = 20,#makes the button the same as the other radiobuttons created
                       variable=price,#makes the variable the price
                       command=quit, #so that when clicked the program will end
                       value=chocolates[i+1][1]) #makes the value the price
choice.pack(side=TOP) #positions the radio button in line with the others

##Paying box (Top Right)##
paying = Label(toprightframe, text="Enter Money: ") #creates label for entry widget
paying.pack(side=LEFT) #positions the label
paid = Entry(toprightframe) #creates an entry widget in the top right frame
paid.pack(padx=10,side=LEFT) #positions the entry widget and defines its size

pay = Button(toprightframe, text='Pay', command=ShowPaid)#creates a button that starts the ShowPaid function when clicked
pay.pack(side=RIGHT)#positions the pay button next to the entry widget

##Proccess box (Centre)##
S = Scrollbar(centreframe)#creates a scroll bar in the centre frame so user can view all text
T = Text(centreframe, height=8, width=50)#creates text widget in centre frame an defines dimensions
S.pack(side=RIGHT, fill=Y)#positions scroll bar and makes it same height as text widget
T.pack(side=LEFT, fill=Y)#positons text widget and makes it same height as scroll bar
S.config(command=T.yview)#makes 'S' a working scroll bar
T.config(yscrollcommand=S.set)#makes 'S' a working scroll bar
T.insert(END, "Change:\n\n")#inserts title to text box so user knows what it is displaying

##Loop##
root.mainloop( )


##choice = Radiobutton(topleftframe, 
##                       text=chocolates[i+1][0],
##                       indicatoron = 0,
##                       width = 20,
##                       padx = 20,
##                       variable=price,
##                       command=quit,
##                       value=chocolates[i+1][1])

## VENDING MACHINE CODE ##
##choice = None #Means the while loops starts without any options being selected
##while choice != "4": #So that when nothing is selected the program ends
##
##    print( #Displays the options for the user with their set prices
##        """
##        ======= Choice of Chocolate Bars =======
##        
##        1 - Mars            = £0.78
##        2 - Galaxy          = £0.99
##        3 - Dairy Milk      = £0.59
##        4 - Nothing         = £0.00
##        
##        """
##        )
##    
##    choice = input("Choose a chocolate bar: ") #Allows the user to pick an option
##    if choice != 4: #So that users don't have to pay for nothing
##        paid = int(input("Enter your money: ")) #Allows the user to pay for their product
##
##    def wchange(paid, price): #Function that works out the amount of change due
##        while paid < price: #While loop using iteration to make sure valid amount paid
##            print ("You have not paid enough money.")
##            print ("You needed",price - paid,"pence more, have your",paid,"pence back and")
##            paid = int(input("Enter your money again: "))
##        change = paid - price #Works out the amount of change due
##        print ("You need",change,"pence change.")
##        coins = [200,100,50,20,10,5,2,1] #List of coins in ascending order so fewest amount
##        x = 0                            #of coins possible outputted
##        while change > 0:
##            while change >= coins[x]: #Makes sure highest value of coins possible used
##                change = change - coins[x] #Reduces amount of chnage due as it is given
##                print (coins[x],"p dispensed")#Prints each amount dispensed
##            x = x + 1 #Makes while loops move along list of coins when it needs to
##        
##    if choice == "4": #For if nothing is selected
##        print ("Okay, come back soon!")   
##    elif choice == "Mars" or choice == "1":
##        wchange(paid,78)
##    elif choice == "2" or choice == "Galaxy":
##        wchange(paid,99)
##    elif choice == "3" or choice == "Dairy Milk":
##        wchange(paid,59)
##    else:
##        print("Sorry, but we don't have",choice, "chocolate bars.")#For if invalid amount entered
##            
##            
##
