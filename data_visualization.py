import streamlit as st
import pandas as pd
import plotly.express as px


# add a title
st.title("Data Visualization App")

# add a subheader in the sidebar
st.sidebar.subheader("Visualization Settings")

# add a file uploader
uploaded_file = st.sidebar.file_uploader(
    label="Upload your CSV or Excel file here",
    type=["csv", "xlsx"],
)

# would you like to display the dataset?
display_data = st.sidebar.checkbox(
    label="Would you like to view the uploaded dataset?")

global df
global numeric_columns
global non_numeric_columns
# account for cases where uploaded file is not None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # uploaded_file.seek(0)

    # try:
    #     df = pd.read_csv(uploaded_file)
    #
    # except Exception as e:
    #     df = pd.read_excel(uploaded_file)

    if display_data:
        st.write(df)

    # extract numeric columns as a list
    numeric_columns = list(df.select_dtypes('float', 'int').columns)

    # extract the non-numeric columns
    non_numeric_columns = list(df.select_dtypes('object').columns)

    # append None values to non_numeric list
    non_numeric_columns.append('None')

    # st.write(numeric_columns)
    # st.write(non_numeric_columns)

# add a select widget
chart_select = st.sidebar.selectbox(
    label="Select the Visualization type",
    options=['Scatter Plot', 'Line Plot', 'Histogram'],
)

try:
    if chart_select == 'Scatter Plot':
        st.sidebar.subheader("Settings of Scatter Plot")
        x_value = st.sidebar.selectbox(label="X axis",
                                       options=numeric_columns)
        y_value = st.sidebar.selectbox(label="Y axis",
                                       options=numeric_columns)
        specify_color = st.sidebar.checkbox(
            label="Would you like to specify the color?")
        if specify_color:
            color_value = st.sidebar.selectbox(label="Color",
                                               options=non_numeric_columns)

            plot = px.scatter(data_frame=df,
                              x=x_value,
                              y=y_value,
                              color=color_value,)
        else:
            plot = px.scatter(data_frame=df,
                              x=x_value,
                              y=y_value)
        # display chart in streamlit
        st.plotly_chart(plot)

except Exception as e:
    print(e)


