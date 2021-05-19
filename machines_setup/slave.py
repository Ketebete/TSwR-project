from statemachine import State

slave_options = [
{'name': 'Proces testowania',           'value': 'testowanie', 'initial': True},# 0
{'name': 'TEST 1',                      'value': 'test1', 'initial': False},    # 1
{'name': 'ReTEST 1',                    'value': 'retest1', 'initial': False},  # 2
{'name': 'ReTEST 2',                    'value': 'retest2', 'initial': False},  # 3
{'name': 'Wyrób gotowy do spakowania',  'value': 'pakuj_ok', 'initial': False}, # 4
{'name': 'Wyrób gotowy do wybrakowania','value': 'brakuj_ok', 'initial': False}]# 5

slave_states = [State(**opt) for opt in slave_options]

slave_form_to = [
[0, [1]],
[1, [2, 4]],
[2, [3, 5]],
[3, [4, 5]],
[4, [0]],
[5, [0]]
]

slave_transitions = {}

slave = {'states': slave_states, 'transitions': slave_transitions, 'form': slave_form_to, 'symbol': 's'}

slave_cords = {
'Proces testowania':            (0.0, -0.75),
'TEST 1':                       (0.5, -0.75),
'ReTEST 1':                     (1, -0.75),
'ReTEST 2':                     (1.5, -0.75),
'Wyrób gotowy do spakowania':   (1, -1.0),
'Wyrób gotowy do wybrakowania': (1, -0.5),
}

slave_color = []

slave_settings = {
'node_color': slave_color,
'edge_color': 'black',
'node_size': 5000,
'width': 1,
'with_labels': True,
'pos': slave_cords,
'node_shape': 'o',
'font_size': 7,
}

slave_edges = {
('Proces testowania', 'TEST 1'),
('TEST 1', 'Wyrób gotowy do spakowania'),
('TEST 1', 'ReTEST 1'),
('ReTEST 1', 'ReTEST 2'),
('ReTEST 1', 'Wyrób gotowy do wybrakowania'),
('ReTEST 2', 'Wyrób gotowy do wybrakowania'),
('ReTEST 2', 'Wyrób gotowy do spakowania'),
('Wyrób gotowy do spakowania', 'Proces testowania'),
('Wyrób gotowy do wybrakowania', 'Proces testowania')
}

slave_nodes = [
'Proces testowania',            # 0
'TEST 1',                       # 1
'ReTEST 1',                     # 2
'ReTEST 2',                     # 3
'Wyrób gotowy do spakowania',    # 4
'Wyrób gotowy do wybrakowania' # 5
]