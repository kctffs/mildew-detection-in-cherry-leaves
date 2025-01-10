import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    st.write("---")
    st.write("## ML Performance Metrics")
    st.write("---")

    version = 'v1'

    st.write("### Train, Test and Validation Set: Labels Frequencies")
    st.info(f"* The dataset contains an equal number of infected "
            f"and healthy leaves.")
    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Test and Validation Sets')
    st.write("---")

    st.write("### ML Model History")
    st.info("* The ML Model history shows how the ML Model trained, "
            "increasing the accuracy and lowering the loss.")
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.info(f"* The model acheived a high accuracy on the test "
            f"set, which means it accurately predicts whether a leaf is "
            f"healthy or infected with powdery mildew most of the time, "
            f"exceeding the 97% acccuracy criteria agreed with the client "
            f"as the project goal.")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                              index=['Loss', 'Accuracy']))