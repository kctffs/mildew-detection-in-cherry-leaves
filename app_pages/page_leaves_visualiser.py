import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_leaves_visualiser_body():

    st.write("---")
    st.write("## Leaf Visualizer")
    st.write("---")
    st.info(
        f"This page achieves Business Requirement 1: \n\n Visually "
        f"differentiating a leaf infected with powdery mildew from "
        f"a healthy leaf.")

    version = 'v1'
    if st.checkbox("Differences between the variability and averages image"):
        st.info(
              f"As shown below, the average infected cell had white marks"
              f"in the centere of the leaf, whilst the healthy leaf "
              f"is clear")

        avg_infected = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.image(avg_infected, caption='Infected Leaf - Variables and Average')
        st.image(avg_uninfected, caption='Healthy Leaf - Variables and Average')
        st.write("---")

    if st.checkbox(
            "Differences in average infected and healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.info(
            f"* There is a visible difference between the average "
            f"leaves however, this is not visible in the average"
            f" differences image.")
        st.image(diff_between_avgs,
                 caption='Difference between the average images')

    if st.checkbox("Image Montage"):
        st.write("* To reload the image montage, click the 'Create Montage' button")
        my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label",
                                        options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=5, ncols=3, figsize=(10, 15))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:

        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

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

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
