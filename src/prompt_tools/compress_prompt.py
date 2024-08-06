def convert_multiline_to_single_line(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
        
    # Join the lines with \n to form a single line
    single_line_content = '\\n'.join(line.strip() for line in lines)
    
    # Open the output file in write mode
    with open(output_file, 'w') as output:
        # Write the single line content to the output file
        output.write(single_line_content)
        
input_file = 'prompt.txt'
output_file = 'prompt_compressed.txt'
convert_multiline_to_single_line(input_file, output_file)