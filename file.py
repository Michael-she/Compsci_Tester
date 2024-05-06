import os

def read_file_contents(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the contents of the file
            contents = file.read()
            return contents
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Replace 'example.txt' with the path to the file you want to read
file_contents = read_file_contents('Expected_Outputs/002.txt')

def remove_every_second_line(filename, input_directory):
    
        open_path = os.path.join(input_directory, filename)
        # Open the file in read mode
        with open(open_path, 'r') as file:
            # Read the contents of the file
            lines = file.readlines()
        print(filename)
        #print(lines)

        # Remove every second line
        modified_lines = [line for index, line in enumerate(lines) if index % 2 != 1]

        # Get the original file name without the path
        file_name = filename.split('/')[-1]

        
        # Create the directory if it doesn't exist
       
       

        # Write the modified lines to a new file in the formatted_outputs directory
        output_file = f'Expected_Outputs/{file_name}'
        with open(output_file, 'w') as file:
            file.writelines(modified_lines)


        return f"The modified file '{file_name}' has been saved in the '{output_file}' directory."
    
    

# Replace 'example.txt' with the path to the file you want to modify
file_path = 'Christiaan_outputs/002.txt'
# Get all file names in the directory
directory = 'Christiaan_outputs'
file_names = os.listdir(directory)

# Loop through each file and perform remove_every_second_line function
for file_name in file_names:

    result = remove_every_second_line(file_name, directory)
    print(result)



