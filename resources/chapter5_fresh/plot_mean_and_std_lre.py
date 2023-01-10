import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def plot_images(png_file, jpg_file, output_file):
    # Read in the png file and store it in a variable
    png = mpimg.imread(png_file)

    # Read in the jpg file and store it in a variable
    jpg = mpimg.imread(jpg_file)

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Plot the png image in the first subplot
    ax1.imshow(png)

    # Plot the jpg image in the second subplot
    ax2.imshow(jpg)

    # Save the figure to a file
    plt.savefig(output_file)


# Example usage
png_file=r'D:\04.GitRepository\masterthesis_report\resources\chapter5\additional_tables\ldm\mean_std_plot_ldm.png'
jpg_file=r'D:\04.GitRepository\masterthesis_report\resources\chapter5\additional_tables\ldm\names.jpg'
output_file=r'D:\04.GitRepository\masterthesis_report\resources\chapter5\additional_tables\ldm\ldm.png'
plot_images(png_file, jpg_file, output_file);
