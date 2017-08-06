import sys

input_string = 'SOR XIC I1 XIO I2 OTL O1 EOR SOR XIC I2 OTU 01 EOR'
ladder_representation = {
    'XIC':'-| |-','XIO':'-|/|-', 'OTE':'-( )-', 'OTL':'-(L)-',
    'OTU':'-(U)-'}



def generate_logic(ladder_input):
    split_input = ladder_input.split()
    header_line = 0
    logic_line = 1
    curr_line = 1
    graphic_output = list()
    line_output = ['','']
    iterator = iter(split_input)
    for code in iterator:
        if code == 'SOR':
            line_output[header_line] += '  | '
            line_output[logic_line] += '{} |-'.format(curr_line)
        elif code == 'EOR':
            line_output[header_line] += ' |'
            line_output[logic_line] += '-|'
            curr_line += 1
            line_output.extend(['',''])
            header_line += 2
            logic_line += 2
        elif code in ladder_representation:
            line_output[logic_line] +=  ladder_representation[code]
            thing = next(iterator)
            line_output[header_line] += '{}'.format(thing).center(len(code) + len(thing))
        elif code == 'BST':
            line_output[logic_line] += '-+-'
            line_output[header_line] += '   '
        elif code == 'NXB':
            line_output[logic_line] += ' +-'
            line_output[header_line] += ' | '
        elif code == 'BND':
            line_output[logic_line] += '-+ '
            line_output[header_line] += ' | '
    for line in line_output:
        print(line)
if __name__ == '__main__':
    generate_logic(input_string)
