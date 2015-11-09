# this is Mablib Program by S.MALGAS

def madlib():
    
    print "Welcome to my Mad Lib"
    
    name = raw_input("Enter a name: ")
    relative = raw_input("Enter a type of relative: ")
    verb = raw_input("Enter an 'ing' verb: ")
    adjective = raw_input("Enter an adjective: ")
    noun = raw_input("Enter a noun: ")

    print "My dear " , relative, name, "was", verb, "in the beach near Camps Bay when he was attacked by a ", adjective, noun
   
madlib()
