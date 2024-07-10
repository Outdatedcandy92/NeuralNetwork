import pygame
import sys
import matplotlib.pyplot as plt
import csv
from PIL import Image
import pandas as pd
import time

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0,0,0))
pygame.display.set_caption("Draw and Save")

drawing = False


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


csv_path = "output.csv"




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)

    pygame.display.flip()

    if pygame.key.get_pressed()[pygame.K_s]:  # Press 'S' to save
        pygame.image.save(screen, "drawing.png")
        label = input("Enter the label: ")
        from test import test_prediction, W1, b1, W2, b2
        image_to_csv("drawing.png", csv_path, label)
        time.sleep(1)
        test_prediction(0, W1, b1, W2, b2)
        exit()
        

       
        