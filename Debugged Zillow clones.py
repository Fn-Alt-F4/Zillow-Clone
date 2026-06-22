
#*********** IMPORTANT READ FIRST ****** --- This is just practice to get code on paper down, dont expect it to be right. a finished correct version will come out.
        # *************************


#This is going to be a clone of the housing website zillow.

#1. Step one, create a login (while true) loop.

#2. Step two, creare a disctionary of houses with the specific price as the value and then the house as the key.

#3. Step three, let the user select a house and then have that house selection list off different things about it.
#3a. So it would list off, the location(country, state, city, zip, sqft, price, any specific specialality things about said house)

#4. Step four, let the buyer go through all the houses and see all the information about each one they select.

#5. Step five, let the buyer schedule a house tour of the one they are interested in.

#6. Step six, let the buyer purchuse the house.

#7. Step seven, have the buyer fill out their information.

#8. Step eight, let the buyer fill in their credit card information.
#8a. Have the buyer fill in all the small details, (Their bank, their credit, if they would like to use a loan, where they currently live...)

#9. Step nine, give a congratulations to the buyer for their new home!

#10. Step ten, give the user the ability to rate the service. (basically rate the zillow clone)

#11. Step eleven, create a logout section for the user to log out after.

###

###

###

#1. Step one, create the login.

username = "edogg"

password = "dogee"

while True:

    typed_username = input("Whats your username?")
    typed_password = input("Whats your password?")

    if typed_username == username and typed_password == password:
        print("Your username and password are correct, you may precede to your next page.")
    break
else:
    print("Your username and password were incorrect, please try again.")

###

###

###

#2. Step two, create your housing dictionary.

available_houses = {"Home 1" : 270000 , "Home 2" : 340000 , "Home 3" : 520000 , "Home 4" : 180000 , "Home 5" : 735000 , "Home 6" : 1234000 , "Home 7" : 863000 , "Home 8" : 665000 , "Home 9" : 952000 , "Home 10" : 69000}

###

###

###

#3a. We need to create the information about each house first before we create the ability for the user to select which house information pops up
#That information and and code wil be on 3b.

house_info = {

"Home 1" : "This home is located in Sterling heights Michigan, USA. It is 1800 square feet. It has 2 bedrooms, 2 bathrooms, a basement, a backyard with a fence, and its single story size. The price of this first home is $270,000." ,

"Home 2" : "This home is located in Fort lauderdale Florida, USA. It is 2100 square feet. It has 3 bedrooms, 1 bathroom, and not basement. Backyard is fairly small since its behind a pond. The price of this home is #340,000." ,

"Home 3" : "This home is located in Houstan Texas, USA. It is 3200 square feet. It has 4 bedrooms, 2 bathrooms, it has a hot tub. its 2 stories, main floor then upstairs bedrooms. it has a complete backyard. price is $520,000." ,

"Home 4" : "This home is located in fayetteville Georgia, USA. Its 1400 square feet. 2 bedrooms, 1.5 bathrooms. It has a basement(small), and its got a fairly nice backyard. This house costs $180,000." ,

"Home 5" : "This home is located in New Orleans Louisiana, USA. Its 3400 square feet. 5 bedrooms 2 bathrooms. It has no basement, it has a hot tub and a pool, other then that the backyard is small. The house cost $735,000." ,

"Home 6" : "This home is located in Seattle Washington, USA. Its 1400 square feet condo. it has 2 bedrooms and 1 bathroom. its in the heart of downtown seattle. you have your own personal pool and hot tub in the complex. price $1,234,000." ,

"Home 7" : "This home is located in outside Nashville Tennesee, USA. Its 2100 square feet. 2 bedrooms 2 bathrooms. small backyard. price is $863000." ,

"Home 8" : "This home is located in Las Vegas Nevada. Its 2800 square feet. It has 4 bedrooms 3 bathrooms, it has a pool and a nice decorated backyard and small basement. The price is $665,000." ,

"Home 9" : "This home is located in Rochester Hills Michigan, USA. Its 2500 square feet. it has a upstairs and down stairs. It also has a nice backyard. 4 beds 4 bathrooms. price is $952,000." ,

"Home 10" : "This home is located in Detroit Michigan, USA. Its 1800 square feet. 3 beds 1 bathroom. It has a basement and a small yard. Area is somewhat dangerous. The price is $69,000." , }

###

###

###


#3. Step three, let the user select a house.

print(available_houses)

choice = input("What houses in our list are you intrested in seeing their specifics?")

if choice in house_info:
    print(house_info[choice])
else:
    print("Thats not on our list.")


###

###

###

#3b. print out the info of the selected house

print(available_houses[0 : 19])

#Have to print out all the info houses because I dont know how to print the singular one the user chooses.

###

###

###

#5. Step five, Let the buyer schedule a house tour of the home they are interested in.

house_tour = input("Would you like to tour this house your interested in?")

if house_tour == "yes":
    print("Okay lets go!")
elif house_tour == "no":
    print("okay.")
else:
    print("Invalid option.")

###

###

###

#6. Step six, let the user buy the house.

house_buy = input("Would you like to purchuse this house?")
if house_buy == "yes":
    print("Sounds good lets get your information.")
else:
    print("No problem.")

###

###

###

#7. Step seven, lets gather the users information.

buyer_name = input("Whats your full name?")

buyer_age = input("How old are you?")

buyer_credit_score = input("Whats your credit score?")

buyer_bank = input("What is your bank provider?")

buyer_SSN = input("Whats your social security number?")

buyer_credit_card_provider = input("Whats your credit card provider? EXAMPLES (Chase, visa, discover, amex, etc...)")

buyer_credit_card_numbers = input("Whats your credit card number?")

buyer_card_card_expiration_date = input("Whats the expiration date on your credit card?")

buyer_credit_card_security_digits = input("What are the 3 digits on the back of the card?")

buyer_name_on_card = input("Whats the name on the card?")

print(buyer_name , buyer_age , buyer_credit_score , buyer_bank , buyer_SSN , buyer_credit_card_provider , buyer_credit_card_numbers , buyer_card_card_expiration_date , buyer_credit_card_security_digits , buyer_name_on_card)

question_1 = input("Does this information seem correct? yes or no?")

if question_1 == "yes":
    print("Excellent")
elif question_1 == "no":
    print("try again")
else:
    print("error")

###

###

###

print("Congratulations on your new home!!!!")

###

###

###

#Have the user rate the service we provided

#Then lastly create a logout

service_rating = input("Would you please rate our service. 1-5 stars. example: (4 stars)")

if service_rating == "1 stars":
    print("How could we improve our service")
    input()

elif service_rating == "2 stars":
    print("What was the flaws in the service we provided that led you to rate us 2 stars?")
    input()

elif service_rating == "3 stars":
    print("Thank you for your rating, any way we can improve our service?")
    input()

elif service_rating == "4 stars":
    print("Thank you for your feedback.")

elif service_rating == "5 stars":
    print("Excellent, we are happy you are satasfied!")

else:
    print("error")

###

###

###

#Logout

logout = input("Would you like to logout?")

if logout == "yes":
    print("logout")
else:
    print("didnt logout")

#DONEEEEEEEEEEEE

#FYI THIS IS NOT DEBUGGED