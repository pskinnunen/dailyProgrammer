import sys

def gen_gray_code(bits):
    gray_code_array = []
    if bits == 1:
        gray_code_array = ['0','1']
    else:
        temp_array = gen_gray_code(bits-1)
        for code in temp_array:
            gray_code_array.append('0'+code)
        for code in temp_array[::-1]:
            gray_code_array.append('1'+code)
    return gray_code_array

if __name__ == '__main__':
   if len(sys.argv) != 2:
       print("Usage ./{} [number of bits]".format(sys.argv[0]))
       exit(1)
   num_of_bits = int(sys.argv[1])
   final_gray_code = gen_gray_code(num_of_bits)
   for gray_code in final_gray_code:
       print(gray_code)
