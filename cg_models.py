#!/usr/bin/python

# class for individual state in the diagram
class State(object):
    """docstring for State"""

    def __init__(self, name, code):
        super(State, self).__init__()
        self.name = name  # name of the state
        self.code = code  # code in the state machine
        self.transitions = []  # transitions of the state. This would include objects of class Transition

    def __str__(self):
        return self.name


# class for transition from one state to another
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

