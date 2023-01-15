# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IjLobIIlvckjQ_uWtPHQNbgLR5QO2usj
"""

import matplotlib.pyplot as plt

# Create a 2x3 subplot grid
fig, axs = plt.subplots(1, 3, figsize=(15, 10))

# Load and display image 1
img1 = plt.imread("/content/MAX_np_C3_brain0_isotropic.tif")
axs[0].imshow(img1, cmap='gray')
axs[0].set_title("(a): Isotropic Model Output")

# Load and display image 2
img2 = plt.imread("/content/MAX_np_C3_brain0_anisotropic.tif")
axs[1].imshow(img2, cmap='gray')
axs[1].set_title("(b): Anisotropic Model Output")

# Load and display image 3
img3 = plt.imread("/content/Diff.tif")
axs[2].imshow(img3, cmap='gray')
axs[2].set_title("(c): Difference between (a) and (b)")


# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# Display the figure
plt.show()
plt.savefig('/content/Result_Iso_AnIso_Diff.png')

fig, axs = plt.subplots(1, 2, figsize=(15, 10))

# Load and display image 1
img1 = plt.imread("/content/isotropic-gaussian.png")
axs[0].imshow(img1, cmap='gray')
axs[0].set_title("(d): Difference between (a) and its Gaussian filtered")
axs[0].set_axis_off()

# Load and display image 2
img2 = plt.imread("/content/iso-aniso.png")
axs[1].imshow(img2, cmap='gray')
axs[1].set_title("(e): Difference between (a) and (b)")
axs[1].set_axis_off()

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# Display the figure
plt.show()
plt.savefig('/content/Result_False_Color_Scale.png')
