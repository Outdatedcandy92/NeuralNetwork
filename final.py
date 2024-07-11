import pygame
import time
from PIL import Image
import csv
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import importlib
import test
       
# Initialize Pygame
pygame.init()

# Set the window size
window_width = 1000
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the initial background color
window.fill((255, 255, 255))  # Move this outside the loop to prevent erasing the drawing

# Set the box size and position
box_width = 400
box_height = 400
box_x = 50
box_y = 100
csv_path = "./resources/output.csv"


font_size = 24
font = pygame.font.SysFont('arial', font_size)

# Render the text
text_color = (0, 0, 0)  # White



# Position for the text
text_x = 500  # Adjust as needed
text_y = 100  # Adjust as needed


submit_button_x = box_x
submit_button_y = box_y + box_height + 10  # 10 pixels below the drawing area
submit_button_width = 100
submit_button_height = 30


with open('./resources/model_parameters.json', 'r') as json_file:
    loaded_parameters = json.load(json_file)

W1 = np.array(loaded_parameters["W1"])
b1 = np.array(loaded_parameters["b1"])
W2 = np.array(loaded_parameters["W2"])
b2 = np.array(loaded_parameters["b2"])


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


# Initialize the drawing variable
drawing = False

# Game loop

running = True

border_thickness = 1
inner_rect = (box_x + border_thickness, box_y + border_thickness, box_width - 2*border_thickness, box_height - 2*border_thickness)
drawing_area = window.subsurface(inner_rect)

pygame.display.update()
# Inside the game loop, before updating the display
pygame.draw.rect(window, (0, 0, 0), (box_x, box_y, box_width, box_height))
while running:
    submit_button_rect = pygame.Rect(submit_button_x, submit_button_y, submit_button_width, submit_button_height)
    pygame.draw.rect(window, (0, 255, 255), submit_button_rect)  # Drawing a green submit button
    submit_text_surface = font.render('Submit', True, (0, 0, 0))  # White text
    window.blit(submit_text_surface, (submit_button_x + 10, submit_button_y + 5)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            if box_x <= event.pos[0] <= box_x + box_width and box_y <= event.pos[1] <= box_y + box_height:
                pygame.draw.circle(window, (255, 255, 255), event.pos, 20)  # Draw inside the box
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if box_x <= event.pos[0] <= box_x + box_width and box_y <= event.pos[1] <= box_y + box_height:
                drawing = True
            elif submit_button_rect.collidepoint(event.pos):    

                pygame.image.save(drawing_area, "./resources/drawing.png")
                print("Drawing saved as 'drawing.png'")
                image_to_csv("./resources/drawing.png", csv_path, 1)
                importlib.reload(test)
                result = test.test_prediction(0, W1, b1, W2, b2)
                text_surface = font.render(f"Prediction: {str(result)}", True, text_color)
                text_width, text_height = text_surface.get_size()
                window.fill((255,255,255), (text_x, text_y, text_width, text_height))

                window.blit(text_surface, (text_x, text_y))  
            

                window.fill((0, 0, 0), (box_x + 1, box_y + 1, box_width - 2, box_height - 2))  # Clear the drawing area
            


    pygame.draw.rect(window, (255, 0, 0), (box_x, box_y, box_width, box_height), 1)  # 1 pixel for the border

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()