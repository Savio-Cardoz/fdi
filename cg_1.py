#!/usr/bin/python
from cg_models import State
from cg_models import Transition


# Dictionaries for storing the names, code and objects of the states
state_names_dict = {}
state_code_dict = {}             
state_objects_dict = {}

# Dictionary for storing the Transitions objects
transitions_objects_dict = {}

no_of_states = 0

# append and return content and format for the controller function
def controller_write():
    
    # use global no_of_states
    global no_of_states 
    controller_list = []

    # controller function signature
    switch_signature = 'void Controller(void){ \n \n \tswitch(state_variable){ \n \n'
    controller_list.append(switch_signature)

    no_of_states = raw_input("How many states are there?")

    # store the code and name of the states and create State objects
    for num in range(int(no_of_states)):
        state_names_dict[num] = raw_input("Please provide the name of the state_"+str(num))
        state_code_dict[num] = raw_input("please provide the code of the state_"+str(num))
        state_objects_dict[num] = State(state_names_dict[num], state_code_dict[num])

    # paint the states to the controller_list
    for num in range(int(no_of_states)):
        state_name = '\tcase '+state_objects_dict[num].name.upper()+' : \n'
        state_func = '\t \t \t \t' + state_objects_dict[num].name + '(); \n \n'
        controller_list.append(state_name)
        controller_list.append(state_func)

    # default state signature
    default_signature = "\tdefault:    /* Do Nothing*/ \n \n }"
    controller_list.append(default_signature)

    return controller_list


# append and return content and format of individual State functions and transitions
def functions_write():
    function_list = []
    global state_objects_dict

    for num in range(int(no_of_states)):
        state_func_name = '(void) '+state_objects_dict[num].name+'(void) { \n \n \t'
        function_list.append(state_func_name)
        
        state_func_code = state_objects_dict[num].code+'\n } \n \n'
        
        if len(state_objects_dict[num].transitions) != 0:
        # if not state_objects_dict[num].transitions:
            for num_1 in state_objects_dict[num].transitions:
                # num_1 has the code of the transition now
                trs_name = '/* '+num_1.name+' */ \n'
                trs_signature = "\t if("+num_1.condition+"){ \n"
                trs_satement = "\t\t state_variable= "+num_1.trs_to+"; \n\t}\n\n\t"
                function_list.append(trs_name)
                function_list.append(trs_signature)
                function_list.append(trs_satement)
                
        else:
            print("There are no transitions in any of the State's in functions_write()")
            
        # TODO: This shall be moved up 
        function_list.append(state_func_code)
                
    return function_list

# write the individual declarations of each function in the header file 
def functions_decl_write():
    functions_decl_list = []

    for num in range(int(no_of_states)):
        state_func_name = '(void) '+state_objects_dict[num].name+'(void) ; \n \n '
        functions_decl_list.append(state_func_name)
                        
    return functions_decl_list


# get, set and return the name of the state machine file
def get_filename():
    name_from_fdi = raw_input("what is the name of the state machine \n")
    return name_from_fdi


# append and return content and format of the enum
def enum_write():
    enum_list = []
    enum_counter = 1
    global no_of_states

    enum_signature = "typedef enum{ \n"
    enum_list.append(enum_signature)

    for num in range(int(no_of_states)):
        em_state = '\t\t'+state_objects_dict[num].name.upper()+'= '+str(enum_counter)+';\n';
        enum_list.append(em_state)
        enum_counter += 1

    enum_close_signature = "\t \t}state; \n \n "    
    enum_list.append(enum_close_signature)

    return enum_list

# get the transition data from the diagram
def get_trans_data():
    
    global no_of_states
    transitions_objects_dict = {}
    global state_objects_dict

    no_of_trans = raw_input("How many transitions are there ?")

    # get the details of individual transitions and save in dictionary
    for num in range(int(no_of_trans)):
        trs_name = raw_input("please enter the name of the transition_"+str(num))
        trs_from = raw_input("transition from which state?")
        trs_to = raw_input("transition to which state?")
        trs_condition = raw_input("condition of transition?")
        transitions_objects_dict[num] = Transition(trs_name, trs_to, trs_from, trs_condition)

        # map the transitions to the State's
        for num_1 in range(int(no_of_states)):
            if((trs_from) == (state_objects_dict[num_1].name)):
                state_objects_dict[num_1].transitions.append(transitions_objects_dict[num])
                print("The transition has matched with the "+state_objects_dict[num_1].name)    
            else:
                print("The transitions didn't match any of the State's in get_trans_data()")
                

    
# create file and write data to the file
def paint_file():

    # get the name of the file to be created and create source and header file
    file_name = get_filename()
    fs = open(file_name + ".c", "w")
    fh = open(file_name + ".h", "w")


    # paint the header of the respective file
    fs.write('#include "' +file_name+ '.h" \n \n \n')

    # get the controller function list. user inputs are given here
    controller_list = controller_write()

    # get the transitions details and merge the transitions with the State objects
    get_trans_data()        

    # get the enum list    
    enum_list = enum_write()
    # paint the enum to the header file
    for el in enum_list:
        fh.write(el)

    # create the state variable    
    fs.write("state state_variable; \n \n")

    # paint the function declarations to the header file
    functions_decl_list = functions_decl_write()
    for fd in functions_decl_list:
        fh.write(fd)

    # get the cumulative function list
    function_list = functions_write()
    # paint individual functions
    for fl in function_list:
        fs.write(fl)

    # add some delibrate space    
    fs.write('\n \n')    

    # paint controller function
    for cf in controller_list:
        fs.write(cf)


# main function
def main():
    paint_file()


# function to be called on executing the file from command line
if __name__ == "__main__":
    main()
