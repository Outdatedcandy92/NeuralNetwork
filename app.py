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
pygame.display.set_caption('Digit Recognizer')

# Set the window size
window_width = 1300
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
text_x = 1000  # Adjust as needed
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


def display_text(window, text, position, font, color=(0, 0, 0)):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        window.blit(text_surface, (position[0], position[1] + i * 20))

def clear_neuron(neuron_activations):
    neuron_activations_lines = ["Neuron Activations:"] + [f"Neuron {i}: {activation}" for i, activation in enumerate(neuron_activations)]
    max_width = 0
    line_height = font.get_linesize()  # Height of one line of text
    total_height = line_height * len(neuron_activations_lines)  # Total height of all lines

    # Calculate the maximum width of the neuron activation lines
    for line in neuron_activations_lines:
        line_surface = font.render(line, True, text_color)
        line_width, _ = line_surface.get_size()
        if line_width > max_width:
            max_width = line_width

    # Clear the area where neuron activations text was displayed
    window.fill((255, 255, 255), (text_position[0], text_position[1], max_width, total_height))

# Initialize the drawing variable
drawing = False

# Game loop

running = True

border_thickness = 1
inner_rect = (box_x + border_thickness, box_y + border_thickness, box_width - 2*border_thickness, box_height - 2*border_thickness)
drawing_area = window.subsurface(inner_rect)
text_position = (1000, 150)

pygame.display.update()
# Inside the game loop, before updating the display
pygame.draw.rect(window, (0, 0, 0), (box_x, box_y, box_width, box_height))
while running:
    submit_button_rect = pygame.Rect(submit_button_x, submit_button_y, submit_button_width, submit_button_height)
    pygame.draw.rect(window, (252, 132, 119), submit_button_rect)  
    submit_text_surface = font.render('Submit', True, (0, 0, 0))  
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
                result, neuron_activations, buff = test.test_prediction(0, W1, b1, W2, b2)
                text_surface = font.render(f"Prediction: {str(result)}", True, text_color)
                text_width, text_height = text_surface.get_size()
                plot_image = pygame.image.load(buff)
                window.blit(plot_image, (550, 90)) 
                clear_neuron(neuron_activations)
                neuron_activations_text = "Neuron Activations:\n" + "\n".join(f"Neuron {i}: {str(activation).strip('[]')}" for i, activation in enumerate(neuron_activations))
                display_text(window, neuron_activations_text, text_position, font)


                window.fill((255,255,255), (text_x, text_y, text_width, text_height))

                window.blit(text_surface, (text_x, text_y))  
            

                window.fill((0, 0, 0), (box_x + 1, box_y + 1, box_width - 2, box_height - 2))  # Clear the drawing area
            


    pygame.draw.rect(window, (255, 0, 0), (box_x, box_y, box_width, box_height), 1)  # 1 pixel for the border

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()