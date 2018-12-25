# In this program Table is considered as a list which have two values status and
# action associated with the status.
# percept contains the present state of the vaccum cleaner.
# percepts contains the history of previous percept.
# Lookup() helps in finding the accosiated action for the current status.
# move() function helps in finding the vaccum if the current status is clean to which tile to move.
# Action contains what to do.
def table_driven_agent(percept):
    percepts=[]
    table=[['dirt','suck the dust'],['clean','move']]
    percepts.append(percept)
    action = lookup(percept,table)
    if action == 'move':
       action = move(percept[1])
    return(action)
def lookup(percept,table):
    for i in table:
        if i[0] == percept[0]:
            return(i[1])
def move(percept):
    if percept == 'left':
        return('Go to right')
    elif percept == 'right':
        return('Go to left')
percept = list(map(str,input("Enter the status and postion: ").split(',')))
action = table_driven_agent(percept)
print(action)
        
            
    
    
