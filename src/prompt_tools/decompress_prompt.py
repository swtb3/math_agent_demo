def convert_single_line_to_multiline(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        
    # Split the content by the \n characters to get individual lines
    lines = content.split('\\n')
    
    # Open the output file in write mode
    with open(output_file, 'w') as output:
        # Write each line to the output file
        for line in lines:
            output.write(line + '\n')

# Specify the input file name
input_file = 'prompt_compressed.txt'
output_file = 'prompt.txt'
convert_single_line_to_multiline(input_file, output_file)
