import sys

input_string = 'SOR XIC I1 BST XIC I2 NXB XIC O1 BND OTE O1 EOR'
ladder_representation = {
    'XIC':'-| |-','XIO':'-|/|-', 'OTE':'-( )-', 'OTL':'-(L)-',
    'OTU':'-(U)-'}



def generate_logic(ladder_split_input, curr_line):
    header_line = 0
    logic_line = 1
    line_output = ['','']
    #iterator = iter(split_input)
    if('NXB' in ladder_split_input):
        start_of_subsection = ladder_split_input.index('NXB')
        end_of_subsection = len(ladder_split_input)-  ladder_split_input[::-1].index('BND')

        subsection_list = ladder_split_input[start_of_subsection:end_of_subsection:]
        if(start_of_subsection != 0):
            del(ladder_split_input[start_of_subsection:end_of_subsection])
    for code_index in range(len(ladder_split_input)):
        code = ladder_split_input[code_index]
        if(start_of_subsection != 0 and code_index == start_of_subsection):
            line_output[logic_line] += '-+-'
            line_output[header_line] += '   '
        #if code == 'SOR':
            #line_output[header_line] += '  | '
            #line_output[logic_line] += '{} |-'.format(curr_line)
        if code == 'EOR':
            line_output[logic_line] = '{} |-'.format(curr_line) + line_output[logic_line] + '-|'
            line_output[header_line] = '  | ' + line_output[header_line] + ' |'
            full_line_length = len(line_output[header_line])
            for line_index in range(2, len(line_output)):
                line_output[line_index] = '  | ' + line_output[line_index]
                line_output[line_index] = line_output[line_index].ljust(full_line_length - 1) + '|'
            curr_line += 1
            code_index += 1
            line_output.extend(generate_logic(ladder_split_input[code_index::], curr_line + 1))
        elif code in ladder_representation:
            line_output[logic_line] +=  ladder_representation[code]
            code_index += 1
            io_code = ladder_split_input[code_index]
            line_output[header_line] += '{}'.format(io_code).center(len(code) + len(io_code))
        elif code == 'BST':
            line_output[logic_line] += '-+-'
            line_output[header_line] += '   '
            curr_line_length = len(line_output[logic_line])
            subsection_output = generate_logic(subsection_list, curr_line)
            for line_index in range(len(subsection_output)):
                subsection_output[line_index] = subsection_output[line_index].rjust(curr_line_length + len(line_output[line_index])-1)
            line_output.extend(subsection_output)
        elif code == 'NXB':
            line_output[logic_line] += '+-'
            line_output[header_line] += '| '
        elif code == 'BND':
            line_output[logic_line] += '-+'
            line_output[header_line] += ' |'
    return line_output

def process_ladder_input(ladder_input_string):
    ladder_split_input = ladder_input_string.split()
    line_output = generate_logic(ladder_split_input, 1)
    for line in line_output:
        print(line)

if __name__ == '__main__':
    process_ladder_input(input_string)
