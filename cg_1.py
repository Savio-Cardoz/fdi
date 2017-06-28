#!/usr/bin/python
from cg_models import State


# Dictionaries for storing the names, code and objects of the states
state_names_dict = {}
state_code_dict = {}             
state_objects_dict = {}

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


# append and return content and format of individual State functions
def functions_write():
    function_list = []

    for num in range(int(no_of_states)):
        state_func_name = '(void) '+state_objects_dict[num].name+'(void) { \n \n \t'
        state_func_code = state_objects_dict[num].code+'\n } \n \n'
        function_list.append(state_func_name)
        function_list.append(state_func_code)
                
    return function_list


# get, set and return the name of the state machine file
def get_filename():
    name_from_fdi = raw_input("what is the name of the state machine \n")
    return name_from_fdi


# create file and write data to the file
def paint_file():

    # get the name of the file to be created and create the file
    file_name = get_filename()
    fo = open(file_name + ".c", "w")

    # paint the header of the respective file
    fo.write('#include "' + file_name + '.h" \n \n \n')

    # get the controller function list
    controller_list = controller_write()

    # get the cumulative function list
    function_list = functions_write()
    # paint individual functions
    for em in function_list:
        fo.write(em)

    # add some delibrate space    
    fo.write('\n \n')    

    # paint controller function
    for el in controller_list:
        fo.write(el)


# main function
def main():
    paint_file()


# function to be called on executing the file from command line
if __name__ == "__main__":
    main()
