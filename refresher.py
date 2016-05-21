from nhl_team import nhl_team

def state_truth():
    name = "Brian"
    age = 29
    print("This is %s and I am %d years old" % (name, age))
    
def list_exercise():
    mylist = []
    mylist.append("a")
    mylist.append("b")
    mylist.append("c")
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print_listing(mylist)

def superhero_string_list():
    namestring = "Spiderman,Iron Man,Batman"
    superheros = namestring.split(",")
    print_listing(superheros)

def print_listing(this_list):
    for item in this_list:
        print(item)

def use_class_to_define_the_rangers():
    ateam = nhl_team()
    ateam.location = "New York"
    ateam.name = "Rangers"
    ateam.print_team_name()

def print_break():
    print("=================")

print_break()
state_truth()
print_break()
list_exercise()
print_break()
superhero_string_list()
print_break()
use_class_to_define_the_rangers()