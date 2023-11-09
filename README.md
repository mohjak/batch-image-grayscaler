# Batch Image Grayscaler

The `batch-image-grayscaler` is a Python-based utility designed to automatically convert color images within a specified directory to grayscale. This tool simplifies the process of batch image processing, making it ideal for workflows that require images in a monochrome format.

## Features

- **Batch Conversion:** Convert multiple images to grayscale in one operation.
- **Support for Various Formats:** Works with popular image formats such as JPG, PNG, TIFF, BMP, and GIF.
- **Automatic Directory Handling:** Automatically creates an output directory for converted images.

## Prerequisites

Before you can run the `batch-image-grayscaler`, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Pillow library

You can install the Pillow library using pip if it is not already installed:

```bash
pip install Pillow
```

## Installation

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/mohjak/batch-image-grayscaler.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd batch-image-grayscaler
   ```

## Usage

To use the `batch-image-grayscaler`, follow these steps:

1. Place all the images you want to convert in the `./images` directory within the `batch-image-grayscaler` project folder.
2. Run the script using the following command:
   ```bash
   python convert_to_grayscale.py
   ```
3. Converted images will be saved in the `./out` directory, with each output file prefixed with `grayscale_`.

## Structure

The project directory is structured as follows:

```
batch-image-grayscaler/
│
├── images/                   # Directory containing images to be converted
├── out/                      # Directory where the converted images will be saved
└── convert_to_grayscale.py   # Script to convert images to grayscale
```

## Contributing

Contributions to the `batch-image-grayscaler` are welcome! If you have suggestions for improvements or encounter any issues, please open an issue or send a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgements

- This project uses the [Pillow](https://python-pillow.org/) library for image processing.

## Support

For support, email mohjak@gmail.com or open an issue on the GitHub repository.

---

Thank you for using or contributing to the `batch-image-grayscaler`!
