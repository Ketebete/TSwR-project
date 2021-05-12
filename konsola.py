from statemachine import StateMachine, State, Transition

# define states for a master (way of passing args to class)
master_options = [{'name': 'Oczekiwanie na bufor', "value": 'bufor', 'initial': True},
          {'name': 'Wyrób w polu pobierania robota', 'value': 'w_polu', 'initial': False},
          {'name': 'Wyrób chwycony', 'value': 'chwycony', 'initial': False},
          {'name': 'Proces testowania', 'value': 'testuj', 'initial': False},
          {'name': 'Odbiór wyrobu', 'value': 'odbiór', 'initial': False},
          {'name': 'Wyrób spakowany', 'value': 'pakuj', 'initial': False},
          {'name': 'Wyrób odłożony jako niezgodny', 'value': 'odloz', 'initial': False}]

master_states = [State(**opt) for opt in master_options]

master_form_to = [[0, [1]],
          [1, [2]],
          [2, [3]],
          [3, [4]],
          [4, [5]],
          [4, [6]],
          [5, [0]],
          [6, [0]]]

master_transitions = {}

slave_options = [{'name': 'Proces testowania', "value": 'testowanie', 'initial': True}, # 0
          {'name': 'TEST 1', 'value': 'test1', 'initial': False}, # 1
          {'name': 'ReTEST 1', 'value': 'retest1', 'initial': False}, # 2
          {'name': 'ReTEST 2', 'value': 'retest2', 'initial': False}, # 3
          {'name': 'Wyrób gotowy do spakowania', 'value': 'pakujok', 'initial': False}, # 4
          {'name': 'wyrób gotowy do wybrakowania', 'value': 'brakujok', 'initial': False}] # 5

slave_states = [State(**opt) for opt in slave_options]

slave_form_to = [[0, [1]],
          [1, [2, 4]],
          [2, [3, 5]],
          [3, [4, 5]],
          [4, []],
          [5, []]]

slave_transitions = {}

# create transitions for a master (as a dict)
for indices in master_form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
        master_transitions[op_identifier] = transition

        # add transition to source state
        master_states[from_idx].transitions.append(transition)

# create transitions for a master (as a dict)
for indices in slave_form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "s_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(slave_states[from_idx], slave_states[to_idx], identifier=op_identifier)
        slave_transitions[op_identifier] = transition

        # add transition to source state
        slave_states[from_idx].transitions.append(transition)


# create a generator class
class Tester(StateMachine):
    states = []
    transitions = []
    states_map = {}
    current_state = None

    def __init__(self, states, transitions):

        # creating each new object needs clearing its variables (otherwise they're duplicated)
        self.states = []
        self.transitions = []
        self.states_map = {}
        self.current_state = states[0]

        # create fields of states and transitions using setattr()
        # create lists of states and transitions
        # create states map - needed by StateMachine to map states and its values
        for s in states:
            setattr(self, str(s.name).lower(), s)
            self.states.append(s)
            self.states_map[s.value] = str(s.name)

        for key in transitions:
            setattr(self, str(transitions[key].identifier).lower(), transitions[key])
            self.transitions.append(transitions[key])

        # super() - allows us to use methods of StateMachine in our Generator object
        super(Tester, self).__init__()

    # define a printable introduction of a class
    def __repr__(self):
        return "{}(model={!r}, state_field={!r}, current_state={!r})".format(
            type(self).__name__, self.model, self.state_field,
            self.current_state.identifier,
        )

    # method of creating objects in a flexible way (we can define multiple functions
    # which will create objects in different ways)
    @classmethod
    def create_master(cls, states, transitions) -> 'Tester':
        return cls(states, transitions)

# create paths from transitions (exemplary)
path_1 = ["s_0_1", "s_1_2","s_2_3","s_3_4"]
path_2 = ["m_0_1", "m_1_2", "m_2_3", "m_3_4", "m_4_5", "m_5_0"]
master_paths = [path_2]
slave_paths = [path_1]

# execute paths
for path in master_paths:

    # create a supervisor
    supervisor = Tester.create_master(master_states, master_transitions)

    # print('\n' + str(supervisor))

    # run supervisor for exemplary path
    print("\nExecuting path: {}".format(path))
    print(supervisor.current_state)
    for event in path:

        # launch a transition in our supervisor
        master_transitions[event]._run(supervisor)
        print(supervisor.current_state)

        # add slave
        if supervisor.current_state.value == "testuj":
            print('\nPrzejście do slave\n')
            for path2 in slave_paths:

                # create a supervisor
                supervisor2 = Tester.create_master(slave_states, slave_transitions)

                # run supervisor for exemplary path
                print("Executing path: {}".format(path2))
                print(supervisor2.current_state)
                for event2 in path2:
                    # launch a transition in our supervisor
                    slave_transitions[event2]._run(supervisor2)
                    print(supervisor2.current_state)
            print('\nPowrót do mastera\n')
