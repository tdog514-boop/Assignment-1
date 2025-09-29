#My Chat Bot
def vacation_days(years):
  if years >= 2:
    print("You have 20 days of vacation.")
  else:
    print("You have 15 days of vacation.")

def handle_request(name):
  request = input("Which would you like help with? 'vacation', 'contact', or 'location': ")

  if "vacation" in request:
    years = int(input("How many years have you been with the company? "))
    vacation_days(years)
  elif "contact" in request:
    print("You can contact HR at help@pycorp.com")
  elif "location" in request:
    print("The office is located at 404 Coding Ave, Pyville")
  else:
    print("I'm sorry, this chatbot is currently under development and can provide information on vacation, contact and location.")

name = input("Hi. What's your name? ")
if "Stev" in name:
    print("I'm sorry, " + name + ", your system access has been revoked.")
else:
    print("Access granted. Welcome " + name + "!")
    handle_request(name)

    request = input("Is there anything else you'd like help with? (y/n) ")
    if "y" in request:
      handle_request(name)
    else:
      print("Thank you for using this chatbot!")