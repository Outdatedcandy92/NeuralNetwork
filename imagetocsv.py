import csv
from PIL import Image
import pandas as pd

def image_to_csv(image_path, csv_path, label):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    image = image.convert("L")

    # Resize the image to 28x28 pixels
    image = image.resize((28, 28))

    # Get the pixel values of the image
    pixel_values = list(image.getdata())

    # Rearrange the pixel values in the desired format
    rearranged_pixel_values = []
    for i in range(28):
        for j in range(28):
            rearranged_pixel_values.append(f"{i+1}x{j+1}")

    # Write the pixel values to a CSV file
    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["label"] + rearranged_pixel_values)  # Write the label as the first row
        writer.writerow([label] + pixel_values)  # Write the pixel values with the label

# Example usage
image_path = "3.png"
csv_path = "output.csv"
label = input("Enter the label: ")
image_to_csv(image_path, csv_path, label)

import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv(csv_path)

# Get the pixel values of the current image
current_image = df.iloc[-1, 1:].values

# Reshape and normalize the pixel values
current_image = current_image.reshape((28, 28)) * 255

# Display the image
plt.gray()
plt.imshow(current_image, interpolation='nearest')
plt.show()
