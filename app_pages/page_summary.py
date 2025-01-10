import streamlit as st


def page_summary_body():
    st.write("---")
    st.write("## Quick Project Summary")
    st.write("---")

    st.info(
        f"### Information"

        f"\n Powdery mildew is a fungal disease caused by Podosphaera "
        f"clandestina that affects cherry trees. The fungus causes the "
        f"leaves to curl up, and may appear as white powdery patches on the "
        f"leaves. \n"
        f"The disease has to be visually identified, which can take an "
        f"employee up to half an hour per tree, however the treatment only "
        f"takes a minute if necessary.\n"
        f"Using this machine learning system, an employee can accurately "
        f"identify infected trees quickly, to make the inspection process "
        f"possible within the time limitations."
    )

    st.warning(
        f"### Project Dataset\n\n"
        f"The dataset, available on "
        f"[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves), "
        f"contains over 4000 images of cherry tree leaves. Half the leaves are"
        f" infected with powdery mildew, and the other half are healthy."
    )

    st.success(
        f"### The Project has two business requirements:\n"
        f"1 - The client wants to conduct a study to visually differentiate "
        f"between healthy cherry leaves and leaves infected with powdery "
        f"mildew.\n\n"
        f"2 - The capability of predicting whether a cherry leaf is healthy "
        f"or contains powdery mildew."
    )

    st.write(
        f"For additional information about this project, please visit and read"
        f" the [Project README file]"
        f"(https://github.com/kctffs/mildew-detection-in-cherry-leaves)"
    )