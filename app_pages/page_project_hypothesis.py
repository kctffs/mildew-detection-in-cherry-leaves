import streamlit as st
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import random
import itertools


def page_project_hypothesis_body():
    st.write("---")
    st.write("## Project Hypothesis and Validation")
    st.write("---")

    st.warning(
        f"* We are assuming that the leaves that are infected "
        f"with powdery mildew have clear "
        f"signs, mostly white patches on the surface, that will "
        f"seperate them from the healthy leaves.\n\n"
    )

    st.success(
        f"* The Average Images shows that the surface of the "
        f"averaging healthy leaf "
        f"is clearer, whilst the surface of the averaging infected leaf has "
        f"white patches.\n\n"
        f"* The Variability Images presents white lines accross the centre of "
        f"the averaging infected leaf, whilst the centre of the average "
        f"healthy leaf is clear."
    )

    version = 'v1'
    avg_infected = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
    avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

    st.image(avg_infected, caption='Infected Leaf - Variability and Average')
    st.image(avg_uninfected, caption='Healthy Leaf - Variability and Average')

    st.success(
        f"* An Image Montage shows that generally, an infected leaf has white "
        f"patches on the surface. \n"
        )

    my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
    labels = os.listdir(my_data_dir + '/validation')
    image_montage(dir_path=my_data_dir + '/validation',
                  label_to_display='healthy',
                  nrows=2, ncols=3, figsize=(10, 8))

    my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
    labels = os.listdir(my_data_dir + '/validation')
    image_montage(dir_path=my_data_dir + '/validation',
                  label_to_display='powdery_mildew',
                  nrows=2, ncols=3, figsize=(10, 8))


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)
    images_list = os.listdir(dir_path + '/' + label_to_display)
    img_idx = random.sample(images_list, nrows * ncols)


    list_rows = range(0, nrows)
    list_cols = range(0, ncols)
    plot_idx = list(itertools.product(list_rows, list_cols))


    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for x in range(0, nrows*ncols):
        img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
        img_shape = img.shape
        axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
        axes[plot_idx[x][0], plot_idx[x][1]].set_title(
            f"Width {img_shape[1]}px x Height {img_shape[0]}px")
        axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
        axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()

    st.pyplot(fig=fig)
    plt.show()
