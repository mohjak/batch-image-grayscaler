import os
from PIL import Image

def convert_to_grayscale(input_folder, output_folder):
    # Ensure output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for file_name in os.listdir(input_folder):
        # Construct the full file path
        file_path = os.path.join(input_folder, file_name)
        # Check if the file is an image (you may add or remove extensions as needed)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            # Open the image file
            img = Image.open(file_path)

            # Convert the image to grayscale
            grayscale_img = img.convert('L')

            # Construct the output file path
            grayscale_file_name = f'{file_name}_grayscale'
            grayscale_file_path = os.path.join(output_folder, grayscale_file_name)

            # Save the grayscale image
            grayscale_img.save(grayscale_file_path)
            print(f"Grayscale image saved as {grayscale_file_path}")

if __name__ == "__main__":
    # Define the input and output folders
    images_folder = './images'
    output_folder = './out'
    convert_to_grayscale(images_folder, output_folder)
