weights = [15,25]
node_list = [
{"name": "A0","kind": "start", "origins": []},
{"name": "B0","kind": "small", "origins": ["A0","C0","B1"]},
{"name": "C0","kind": "small", "origins": ["B0","D0"]},
{"name": "D0","kind": "small", "origins": ["C0","D1"]},
{"name": "E0","kind": "small", "origins": ["E1","G0"]},
{"name": "G0","kind": "large", "origins": ["E0","G1"]},
{"name": "B1","kind": "large", "origins": ["B0","C1"]},
{"name": "C1","kind": "large", "origins": ["B1","D1"]},
{"name": "D1","kind": "large", "origins": ["C1","D0","E1"]},
{"name": "E1","kind": "small", "origins": ["D1","E0","F1"]},
{"name": "F1","kind": "small", "origins": ["E1","F2","G1"]},
{"name": "G1","kind": "large", "origins": ["F1","G0","H2"]},
{"name": "C2","kind": "large", "origins": ["C1","C3","D2"]},
{"name": "D2","kind": "small", "origins": ["C2","D3"]},
{"name": "F2","kind": "small", "origins": ["D2","F1","F3","G2"]},
{"name": "G2","kind": "large", "origins": ["F2","H2"]},
{"name": "H2","kind": "end", "origins": ["G1","G2","G3"]},
{"name": "A3","kind": "start", "origins": []},
{"name": "B3","kind": "small", "origins": ["A3","B4","C3"]},
{"name": "C3","kind": "small", "origins": ["B3","C2","C4"]},
{"name": "D3","kind": "small", "origins": ["D2","D4","F3"]},
{"name": "F3","kind": "small", "origins": ["D3","F2","G3"]},
{"name": "G3","kind": "large", "origins": ["F3","G4","H2"]}, #G4 is a dead end, so cannot start from here
{"name": "B4","kind": "large", "origins": ["B3","C4"]},
{"name": "C4","kind": "small", "origins": ["B4","C3","D4"]},
{"name": "D4","kind": "large", "origins": ["C4","D3"]},
{"name": "G4","kind": "large", "origins": ["G3"]}
]