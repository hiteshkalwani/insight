# Importing packages: streamlit for the frontend, requests to make the api calls
import streamlit as st
import requests


def get_service_details(service: str) -> list:
    """
    Making an API request to backend service to get the details for each service. This function returns, list of names of trained models 
    :param service: MLP service that is being used.
    :return: List of names of trained models
    """
    models = ["Model_1", "Model_2"]

    return models


def disaply_page(service: str, models: list):
    """
    This function is used to generate the page for each service. It returns,
    :param service: String of the service being selected from the side bar.
    :param models: List of trained models that have been trained for this service.
    :return: model, input_text run_button: Selected model from the drop down, input text by the user and run botton to kick off the process.
    """
    st.header(service)
    model: str = st.selectbox("Transformer Model", models)
    input_text: str = st.text_area("Enter Text here")
    if service == "Information Extraction":
        query: str = st.text_input("Enter query here.")
        run_button: bool = st.button("Run")
        return model, input_text, query, run_button
    else:
        run_button: bool = st.button("Run")
        return model, input_text, run_button


def run_inference(service: str, model: str, text: str, query: str = None):
    """
    This function is used to send the api request for the actual service for the specifed model to the
    :param service: String for the actual service.
    :param model: Model that is slected from the drop down.
    :param text: Input text that is used for analysis and to run inference.
    :param query: Input query for Information extraction use case.
    :return: results from the inference done by the model.
    """
    return


def main():
    st.sidebar.header("Select the Natural Language Processing Service")
    service = st.sidebar.radio(
        label="",
        options=[
            "Project Insight",
            "News Classification",
            "Named Entity Recognition",
            "Sentiment Analysis",
            "Summarization",
            "Information Extraction",
        ],
    )

    if service == "Project Insight":
        st.header("This is the Project Insight about Page...")
    else:
        models = get_service_details(service)
        if service == "Information Extraction":
            model, input_text, query, run_button = disaply_page(service, models)
        else:
            model, input_text, run_button = disaply_page(service, models)
            query = str()
        if run_button:
            # st.write(model)
            # st.write(input_text)
            run_inference(service, model, input_text, query)


if __name__ == "__main__":
    main()