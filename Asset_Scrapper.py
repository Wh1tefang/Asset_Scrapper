import csv
import re

def extract_text(input_text):
    pattern = r'(?:;;|assets:)(.*?)(?=\()'
    matches = re.findall(pattern, input_text, re.DOTALL)
    extracted_text = [match.strip() for match in matches]
    return extracted_text

def export_to_csv(data, output_filename='output.csv'):
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

if __name__ == "__main__":
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            input_text = file.read()
            extracted_data = [[item] for item in extract_text(input_text)]  # Wrap each item in a list
            export_to_csv(extracted_data, output_filename)
            print(f"Extraction successful. Data exported to {output_filename}")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
