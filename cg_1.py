#!/usr/bin/python


# TODO: The classes shall be moved to another file and would be imported here
# This class is used to depict a state in the state machine
class State(object):
    """docstring for State"""

    def __init__(self, name, code):
        super(State, self).__init__()
        self.name = name  # name of the state
        self.code = code  # code in the state machine
        self.transitions = []  # Transitions of the state. This would include objects of class Transition

    def __str__(self):
        return self.name


# This class is used to depict a transition from ione state to another
class Transition(object):
    """docstring for Transition"""

    def __init__(self, name, trs_to, trs_from, condition):
        super(Transition, self).__init__()
        self.name = name  # name of the transition
        self.trs_to = trs_to  # name of the destination state
        self.trs_from = trs_from  # name of the source state
        self.condition = condition  # condition of transition

    def __str__(self):
        return self.name


# TODO: Create a list here for the Controller function and pass to to paint_file()
def Controller_Write():
    controller_list = []

    # Controller function signature
    switch_signature = 'void Controller(void){ \n \n \tswitch(state_variable){ \n \n'
    # switch_signature = 'void '+name_from_fdi_+'controller(void){ \n \n \t switch(state_variable){ \n \n'
    controller_list.append(switch_signature)

    no_of_states = raw_input("How many states are there?")

    # Dictionaries for storing the names, code and objects of the states
    state_names_dict = {}
    state_code_dict = {}
    State_objects_dict = {}

    # Store the code and name of the states and create State objects
    for num in range(int(no_of_states)):
        state_names_dict[num] = raw_input("Please provide the name of the state_"+str(num))
        state_code_dict[num] = raw_input("please provide the code of the state_"+str(num))
        State_objects_dict[num] = State(state_names_dict[num], state_code_dict[num])


    # Paint the states to the controller_list
    for num in range(int(no_of_states)):
        state_name = '\tcase '+State_objects_dict[num].name+' : \n'
        state_code = '\t \t \t \t'+State_objects_dict[num].code+'\n \n'
        controller_list.append(state_name)
        controller_list.append(state_code)


    # Default state signature
    default_signature = "\tdefault:    /* Do Nothing*/ \n \n }"
    controller_list.append(default_signature)

    return controller_list


# This function creates and returns the name of the state machine file
def paint_filename():
    global name_from_fdi
    name_from_fdi = raw_input("what is the name of the state machine \n")

    return name_from_fdi


# This function creates the file
def paint_file():
    # Get the name of the file to be created and create the file
    file_name = paint_filename()
    fo = open(file_name + ".c", "w")

    # include the header of the respective file
    fo.write('#include "' + file_name + '.h" \n \n \n')

    # Generation of controller function
    controller_list = Controller_Write()
    for el in controller_list:
        fo.write(el)


    # TODO: Individual functions to be called here


# main function
def main():
    paint_file()


# This function would be called on executing the file from command line
if __name__ == "__main__":
    main()


# TODO: Start writing into the file the proper content with the name of the function and the transitions.



