import sys

input_string = 'SOR XIC I1 BST XIC I2 NXB XIC O1 BND OTE O1 EOR'
ladder_representation = {
    'XIC':'-| |-','XIO':'-|/|-', 'OTE':'-( )-', 'OTL':'-(L)-',
    'OTU':'-(U)-'}



def generate_logic(ladder_split_input):
    header_line = 0
    logic_line = 1
    curr_line = 1
    line_output = ['','']
    #iterator = iter(split_input)
    if('NXB' in ladder_split_input):
        start_of_subsection = ladder_split_input.index('NXB')
        end_of_subsection = len(ladder_split_input)-  ladder_split_input[::-1].index('BND')

        subsection_list = ladder_split_input[start_of_subsection:end_of_subsection:]
        if(start_of_subsection != 0):
            del(ladder_split_input[start_of_subsection:end_of_subsection])
        for sub_index in range(len(subsection_list)):
            print (subsection_list[sub_index])
    for code_index in range(len(ladder_split_input)):
        print (ladder_split_input[code_index])
        code = ladder_split_input[code_index]
        if(start_of_subsection != 0 and code_index == start_of_subsection):
            line_output[logic_line] += '-+-'
            line_output[header_line] += '   '
        if code == 'SOR':
            line_output[header_line] += '  | '
            line_output[logic_line] += '{} |-'.format(curr_line)
        elif code == 'EOR':
            line_output[logic_line] += '-|'
            line_output[header_line] += ' |'
            curr_line += 1
            code_index += 1
            line_output.extend(generate_logic(ladder_split_input[code_index::]))
        elif code in ladder_representation:
            line_output[logic_line] +=  ladder_representation[code]
            code_index += 1
            io_code = ladder_split_input[code_index]
            line_output[header_line] += '{}'.format(io_code).center(len(code) + len(io_code))
        elif code == 'BST':
            line_output[logic_line] += '-+-'
            line_output[header_line] += '   '
            line_output.extend(generate_logic(subsection_list))
            for line_index in range(2, len(line_output)):
                print(line_output[line_index])
                line_output[line_index] = line_output[line_index].rjust(len(line_output[logic_line]) + len(line_output[line_index]) - 2)
        elif code == 'NXB':
            line_output[logic_line] += '+-'
            line_output[header_line] += '| '
        elif code == 'BND':
            line_output[logic_line] += '-+'
            line_output[header_line] += ' |'
    return line_output

def process_ladder_input(ladder_input_string):
    ladder_split_input = ladder_input_string.split()
    line_output = generate_logic(ladder_split_input)
    for line in line_output:
        print(line)

if __name__ == '__main__':
    process_ladder_input(input_string)
