from nhl_team import nhl_team

def state_truth():
    name = "Brian"
    age = 32
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
    
def use_dict_card():
    card = dict(
                suit = "Diamond",
                rank = "Ace"
                )
    print("Card Suit is %s" % card["suit"])
    print("Card Rank is %s" % card["rank"])
    
def list_comprehension():
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    word_lengths = [len(word) for word in words if word != "the"]
    print_listing(word_lengths)

def multi_function_arguments(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first
    
def use_multi_argument_function():
    result = multi_function_arguments(1, 2, 3, action="sum", number="first")
    print("Result: %d" % result)

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
print_break()
use_dict_card()
print_break()
list_comprehension()
print_break()
use_multi_argument_function()
print_break()