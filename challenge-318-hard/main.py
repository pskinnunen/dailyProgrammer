import sys

input_string = 'SOR XIC I1 BST XIC I2 NXB XIC O1 BND OTE O1 EOR'
ladder_representation = {
    'XIC':'-| |-','XIO':'-|/|-', 'OTE':'-( )-', 'OTL':'-(L)-',
    'OTU':'-(U)-'}



def generate_logic(ladder_input):
    split_input = ladder_input.split()
    header_line = ''
    logic_line = ''
    line = 1
    iterator = iter(split_input)
    for code in iterator:
        if code == 'SOR':
            header_line += '  | '
            logic_line += '{} |-'.format(line)
        elif code == 'EOR':
            header_line += ' |'
            logic_line += '-|'
            line += 1
        elif code in ladder_representation:
            logic_line +=  ladder_representation[code]
            thing = next(iterator)
            header_line += '{}'.format(thing).center(len(code) + len(thing))
        elif code == 'BST':
            logic_line += '-+-'
            header_line += '   '
        elif code == 'NXB':
            logic_line += ' +-'
            header_line += ' | '
        elif code == 'BND':
            logic_line += '-+ '
            header_line += ' | '
    print(header_line)
    print(logic_line)

if __name__ == '__main__':
    generate_logic(input_string)
