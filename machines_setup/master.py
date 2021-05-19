from statemachine import State

master_options = [
{'name': 'Oczekiwanie na bufor',                'value': 'bufor', 'initial': True},     # 0
{'name': 'Wyrób w polu pobierania robota',      'value': 'w_polu', 'initial': False},   # 1
{'name': 'Wyrób chwycony',                      'value': 'chwycony', 'initial': False}, # 2
{'name': 'Proces testowania',                   'value': 'testuj', 'initial': False},   # 3
{'name': 'Odbiór wyrobu',                       'value': 'odbior', 'initial': False},   # 4
{'name': 'Wyrób spakowany',                     'value': 'pakuj', 'initial': False},    # 5
{'name': 'Wyrób odłożony jako niezgodny',       'value': 'odloz', 'initial': False}     # 6
]

master_states = [State(**opt) for opt in master_options]

master_form_to = [
[0, [1]],
[1, [2]],
[2, [3]],
[3, [4]],
[4, [5]],
[4, [6]],
[5, [0]],
[6, [0]]
]

master_transitions = {}

master = {'states': master_states, 'transitions': master_transitions, 'form': master_form_to, 'symbol': 'm'}

master_cords = {
'Oczekiwanie na bufor':             (0.0, 0.0),
"Wyrób w polu pobierania robota":   (0.0, -0.25),
"Wyrób chwycony":                   (0.0, -0.5),
"Proces testowania":                (0.0, -0.75),
"Odbiór wyrobu":                    (0.0, -1.0),
"Wyrób spakowany":                  (-0.25, -1.25),
'Wyrób odłożony jako niezgodny':    (0.25, -1.25)
}

master_color = []

master_settings = {
'node_color': master_color,
'edge_color': 'black',
'node_size': 5000,
'width': 1,
'with_labels': True,
'pos': master_cords,
'node_shape': 'o',
'font_size': 7,
}

master_edges = [
('Oczekiwanie na bufor', "Wyrób w polu pobierania robota"),
("Wyrób w polu pobierania robota", "Wyrób chwycony"),
("Wyrób chwycony", "Proces testowania"),
("Proces testowania", "Odbiór wyrobu"),
("Odbiór wyrobu", "Wyrób spakowany"),
("Odbiór wyrobu", 'Wyrób odłożony jako niezgodny'),
("Wyrób spakowany", 'Oczekiwanie na bufor'),
('Wyrób odłożony jako niezgodny', 'Oczekiwanie na bufor')
]

master_nodes = [
'Oczekiwanie na bufor',                 # 0
'Wyrób w polu pobierania robota',       # 1
'Wyrób chwycony',                       # 2
'Proces testowania',                    # 3
'Odbiór wyrobu',                        # 4
'Wyrób spakowany',                      # 5
'Wyrób odłożony jako niezgodny'         # 6
]