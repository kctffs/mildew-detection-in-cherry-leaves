### This project was not deployed through Heroku although, being assisted by the tutor team and advised to deploy by [Render](https://render.com/) I will provide the appropriate deployment details as well as Heroku's.

# Mildew Detection in Cherry Leaves.

Live Link: [Powdery Mildew Detector](https://mildew-detection-in-cherry-leaves-1.onrender.com)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis

- Leaves that are infected with powdery mildew have patches of white that are the main factor in seperating them from the healthy leaves.
  - To understand and act upon this, there can be a study based on the investigation into the infection.
 
## Validation

- Ensuring validation was by being presented with the averaging infected image showing white patches over the leaf, and the body of the averaging healthy leaf shows none.
- The  variability images that is classed as healthy presents the centre of the leaf being mostly clear, whilst the infected variability images has visible white lines and patches throughout.
  
<img width="656" alt="Validation-Img1" src="https://github.com/user-attachments/assets/e79afc0f-f656-4f8f-a0f7-f344a0451136" />

- There is a clear, visual difference between the healthy leaves and the infected leaves shown; the infected leaves show no life and almost have sad tendencies.

<img width="588" alt="Validation-img2" src="https://github.com/user-attachments/assets/c45c18b2-b42c-4bd2-80bf-02747aa350b0" />

- When it comes to the averaging images that display them, the comparison of the averaging is partially condescending as there is an unclear image produced.

<img width="606" alt="Validation-Img3" src="https://github.com/user-attachments/assets/6018f1d0-a3eb-4662-a888-1a90a01de1d6" />

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business Requirement 1:
  - The inclusion of average images and variability images for each class (healthy or powdery mildew).
  - The implementation of data between average healthy and average powdery mildew cherry leaves.
  - An image montage for each class to your liking.

- Business Requirement 2:
  - The capability of predicting whether a cherry leaf is healthy or contains powdery mildew.

## User Stories

- As a client, I can work the dashboard without confusion and understand the data shown.
  - The dashboard has been built using streamlit, with  navigation bar to navigate easily between pages without confusion.
- As a client, I can see the contrast between the averaging infected and averaging healthy cherry leaves.
  - The page named 'Leaves Visualiser' shows the client the difference between the averaging healthy and the averaging infected cherry leaves which also includes text.
- As a client, I can display a images montage of cherry leaves that are either healthy or infected with powdery mildew.
  - The page named 'Leaves Visualiser' implements a feature that the client can generate a montage of healthy or infected leaves. This also includes refreshing for a different set of images.
- As a client, I want a ML model to estimate with a 97% accuracy rating by whether a random cherry leaf is either healthy or is infected with powdery mildew.
  - The page named 'Powdery Mildew Detection' page consists of a feature that a user can upload images, and then the ML Model will produce a prediction with accuracy whether the leaf is infected with powdery mildew or healthy.
- As a client, I can produce a report by a set of images. These images are undisclosed by a binary classifier and the report tells me which leaves are infected.
  - When a client has uploaded images of cherry leaves on the 'Powdery Mildew Detection' page, they will be provided with an analysis report classifying all uploaded images with their results.

## ML Business Case

- What are the business requirements?
  - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
- Is there any business requirement that can be answered with conventional data analysis?
  - Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- Does the client need a dashboard or an API endpoint?
  - The client needs a dashboard.
- What does the client consider as a successful project outcome?
  - A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  - Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.
- Can you break down the project into Epics and User Stories?
  - Information gathering and data collection.
  - Data visualisation, cleaning, and preparation.
  - Model training, optimisation and validation.
  - Dashboard planning, designing, and development.
  - Dashboard deployment and release.
  - Ethical or Privacy concerns?
  - The client provided the data under an NDA (non-disclosure agreement), therefore the data should only be shared with professionals that are officially involved in the project.
- Does the data suggest a particular model?
  - The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.
- What are the model's inputs and intended outputs?
  - The input is a cherry leaf image and the output is a prediction of whether the cherry leaf is healthy or contains powdery mildew.
- What are the criteria for the performance goal of the predictions?
  - We agreed with the client a degree of 97% accuracy.
- How will the client benefit?
  - The client will not supply the market with a product of compromised quality.

## Dashboard Design

### Page 1: Project Summary

- Information that includes the content provided for the study which is:
  - Powdery mildew is a fungal disease caused by Podosphaera clandestina that affects cherry trees. The fungus causes the leaves to curl up, and may appear as white powdery patches on the leaves. The disease has to be visually identified, which can take an employee up to half an hour per tree, however the treatment only takes a minute if necessary. Using this machine learning system, an employee can accurately identify infected trees quickly, to make the inspection process possible within the time limitations.

- Project Dataset
  -The dataset, available on Kaggle, contains over 4000 images of cherry tree leaves. Half the leaves are infected with powdery mildew, and the other half are healthy.

- The Project has two business requirements:
  - The client wants to conduct a study to visually differentiate between healthy cherry leaves and leaves infected with powdery mildew.
  - The capability of predicting whether a cherry leaf is healthy or contains powdery mildew."

<img width="278" alt="Streamlit-menu" src="https://github.com/user-attachments/assets/85105ae6-4513-4375-a642-3c09fb10ed98" />
<img width="612" alt="Summary-Page" src="https://github.com/user-attachments/assets/0be3eada-6740-4060-a1ec-c3854418d180" />

### Page 2: Leaves Visualiser

This page achieves Business Requirement 1: Visually differentiating a leaf infected with powdery mildew from a healthy leaf.

Checkbox 1: Differences between the variability and averages image.

Checkbox 2: Differences in average infected and average healthy leaves.

Checkbox 3: Image Montage.

<img width="590" alt="Powdery-Mildew-Detector-Page" src="https://github.com/user-attachments/assets/bbfa03d2-8dd0-4f20-b11b-8138505eebab" />
<img width="679" alt="Powdery-Mildew-Detector-Page2" src="https://github.com/user-attachments/assets/b5e3122b-ce37-44a8-bb77-f7f992d1e6a5" />

## Page 3: Powdery Mildew Detection

This page achieves Business Requirement 2: The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

UI consists of a file upload widget where the client can go and download their own set of images and then upload multiple cherry leaf images for their own liking. After the client uploads their images they will have a scenario where:
- Will be presented with a estimated statement, which will then inform whether the leaf is infected with powdery mildew or healthy.
- The client will see a table with the image names and prediction results.

<img width="602" alt="Powdery-Mildew-Detector-Page3" src="https://github.com/user-attachments/assets/42e4af90-bcb5-427c-a955-6b0297d1e011" />

## Page 4: Project Hypothesis

We are assuming that the leaves that are infected with powdery mildew have clear signs, mostly white patches on the surface, that can separate them from healthy leaves. The Average Images shows that the surface of the averaging healthy leaf is clearer, whilst the surface of the averaging infected leaf has white patches. The Variability Images presents white lines across the centre of the averaging infected leaf, whilst the centre of the average healthy leaf is clear.

<img width="634" alt="Powdery-Mildew-Detector-Page4" src="https://github.com/user-attachments/assets/bcbd03a2-c6d8-4b3e-9bb6-9e19e615850d" />

## Page 5: ML Performance Metrics

Labelling the frequencies for **train**, **test** &  **validation** sets. The dataset contains an equal number of infected and healthy leaves.
ML Model History shows how the ML Model trained, increasing the accuracy and lowering the loss.

<img width="424" alt="Page5-ML" src="https://github.com/user-attachments/assets/76fac05e-7505-419b-98c4-d747746d54e0" />
<img width="794" alt="ML-Hist" src="https://github.com/user-attachments/assets/1ebc31e2-068c-4730-ae28-78176b5ca5b6" />
<img width="803" alt="ML-Perf" src="https://github.com/user-attachments/assets/ac3b839a-348f-45ab-9766-51be8213556f" />

## CRISP-DM

- The CRoss-Industry Standard Process for Data Mining (CRISP-DM), created in the end of 1996 by leaders of Daimler-Benz, is a non-proprietary, documented and freely available data mining methodology and process model.
- CRISP-DM provides a generic process model capable of being modified for the particular needs of any industry.
- This model encourages best practices and offers organizations the structure needed to realize better, faster results from data mining due the complete blueprint for conducting a data mining project.
- The data mining methodology and techniques combined with assistance from more experienced practitioners can be an essential tool to understand the concepts and steps involved in the entire data mining process. [Source](https://almirgouvea.github.io/The-Crisp-DM-Methodology/chapters/definition.html)

## Unfixed Bugs
- Heroku has not deployed my final project as there is a problem with the slug. Slug size has not been reduced however deployment has been successful on another site.
  - To solve this problem I would have to, either, include files into a .slugignore or reduce the images.

<img width="740" alt="Screenshot 2025-01-10 at 09 43 48" src="https://github.com/user-attachments/assets/59b938e2-3f0b-405b-9fb8-e2c5d02c0665" />

## Deployment

### Render

- The App live link is: https://mildew-detection-in-cherry-leaves-1.onrender.com/
- As [Render](https://render.com/) was used, Procfile and runtime.txt were not needed, so the files were removed.
- The project was deployed to Render using the following steps:

1. Log in to Render and create a new web hosting service.
2. Connect your corresponding repository with GitHub.
3. Confifure the settings so that the **Root Directory** is *blank*, **Environment** is *Python 3*, **Region** is *EU* and **Branch** is *main*.
4. Set the build command to `pip install -r requirements.txt && ./setup.sh`.
5. Set the start command to `streamlit run app.py`.
6. Choose the free plan.
7. On the advanced, add **PORT** as a Key and **8501** as it's value. Secondly, add **PYTHON_VERSION** as a Key and **3.12.2** as it's Value.
8. Select No on auto deployment and deploy.

### Heroku (Initial Use)

- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- numpy==1.26.1 - Numpy was used to convert the images into arrays.
- pandas==2.1.1 - Pandas was used to provided the foundation for the data to be in a dataframe.
- matplotlib==3.8.0 - Matplotlib was used for plotting both the images and data.
- seaborn==0.13.2 - Seaborn was used in conjunction with Matplotlib.
- streamlit==1.40.2 - Streamlit was used for running the app and creating the dashboard.
- tensorflow-cpu==2.16.1 - Tensorflow was the import used for the creation of the ML Model.
- keras>=3.0.0 - Keras was used in conjunction with Tensorflow for the creation of the ML Model.
 - plotly==5.17.0, Pillow==10.0.1, joblib==1.4.2, scikit-learn==1.3.1

## Platforms Used

[Gitpod](https://www.gitpod.io/).
[Github](https://github.com/).
[Render](https://render.com/).
[Kaggle](https://www.kaggle.com/).

## Validation

- Code was put through the [CI PEP8 Python Linter](https://pep8ci.herokuapp.com) and passed with screenshots provided.

<img width="835" alt="pep8-valid-1" src="https://github.com/user-attachments/assets/4035e548-27ea-46da-8f63-605bfedfeb3d" />
<img width="836" alt="pep8-valid-2" src="https://github.com/user-attachments/assets/e521611a-1739-4ca5-961d-49ace9603f40" />
<img width="804" alt="pep8-valid-3" src="https://github.com/user-attachments/assets/2d7ab029-b0ce-4282-82eb-c85b0f1e35cc" />

## Credits

- [Kaggle Cherry Leaves]([https://www.kaggle.com/](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)). - For the use of their data source.
- [Code Institute - Walkthrough Project 01 - Malaria Detector](https://codeinstitute.net/). - For the step by step guide to the understanding and inspiring the code during the project for example the code revolving around image data.
- [Code Institute - Walkthrough Project 02 - Churnometer](https://codeinstitute.net/). - For the step by step guide to the understanding and inspiring the code during the project for example the directories.
- [cla-cif](https://github.com/cla-cif) - Inspiration for the first model used before retrained later, alongside the module contents and walkthrough projects on models.

