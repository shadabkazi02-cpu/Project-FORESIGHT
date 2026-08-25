import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Project FORESIGHT",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Project FORESIGHT")
st.subheader("Retail Demand Forecasting & Business Intelligence")

st.write(
    """
    An end-to-end retail analytics solution designed to transform
    transactional data into actionable business insights.
    """
)

st.divider()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("Project Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Project Overview",
        "Analytics Demo",
        "Business Recommendations"
    ]
)

# --------------------------------------------------
# Project Overview
# --------------------------------------------------

if page == "Project Overview":

    st.header("📌 Project Overview")

    st.write(
        """
        Project FORESIGHT combines data analysis, feature engineering,
        machine learning, demand forecasting and business intelligence
        to support retail decision-making.
        """
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Analytics", "Python")

    with col2:
        st.metric("Forecasting", "Machine Learning")

    with col3:
        st.metric("Visualization", "Power BI")

    with col4:
        st.metric("Deployment", "Streamlit")

    st.divider()

    st.header("🔄 Project Workflow")

    st.markdown(
        """
        **Raw Retail Data**

        ↓

        **Data Understanding**

        ↓

        **Data Cleaning & Preparation**

        ↓

        **Exploratory Data Analysis**

        ↓

        **Feature Engineering**

        ↓

        **Demand Forecasting Models**

        ↓

        **Forecast Analysis**

        ↓

        **Business Recommendations**

        ↓

        **Power BI Dashboard**
        """
    )

    st.divider()

    st.header("🛠️ Technologies Used")

    technologies = pd.DataFrame({
        "Technology": [
            "Python",
            "Pandas",
            "NumPy",
            "Matplotlib / Seaborn",
            "Scikit-learn",
            "XGBoost",
            "Power BI",
            "Streamlit"
        ],
        "Purpose": [
            "Data analysis and machine learning",
            "Data manipulation",
            "Numerical operations",
            "Data visualization",
            "Machine learning",
            "Gradient boosting forecasting",
            "Business intelligence",
            "Application deployment"
        ]
    })

    st.dataframe(
        technologies,
        use_container_width=True,
        hide_index=True
    )


# --------------------------------------------------
# Analytics Demo
# --------------------------------------------------

elif page == "Analytics Demo":

    st.header("📈 Interactive Retail Analytics")

    st.write(
        "Upload a retail CSV file to explore its basic structure and trends."
    )

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Dataset loaded successfully!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", f"{df.shape[0]:,}")

        with col2:
            st.metric("Columns", df.shape[1])

        with col3:
            st.metric(
                "Missing Values",
                f"{df.isna().sum().sum():,}"
            )

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        st.subheader("Column Information")

        column_info = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isna().sum().values
        })

        st.dataframe(
            column_info,
            use_container_width=True,
            hide_index=True
        )

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        if numeric_columns:

            st.subheader("Numeric Analysis")

            selected_column = st.selectbox(
                "Select a numeric column",
                numeric_columns
            )

            fig = px.histogram(
                df,
                x=selected_column,
                title=f"Distribution of {selected_column}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

        st.info(
            "Upload a CSV dataset to explore the data interactively."
        )


# --------------------------------------------------
# Business Recommendations
# --------------------------------------------------

else:

    st.header("💡 Business Recommendations")

    st.write(
        """
        Project FORESIGHT converts analytical and forecasting results
        into practical retail planning decisions.
        """
    )

    recommendations = [
        (
            "📦 Inventory Planning",
            "Use demand forecasts to maintain appropriate inventory levels "
            "and reduce stockout and overstock risk."
        ),
        (
            "📈 High-Demand Products",
            "Identify products with consistently strong demand and prioritize "
            "their availability."
        ),
        (
            "📉 Low-Demand Products",
            "Identify products with weak demand and review inventory or "
            "promotion strategies."
        ),
        (
            "🏪 Store Performance",
            "Compare store-level demand and sales patterns to identify "
            "locations requiring operational attention."
        ),
        (
            "🎯 Promotional Planning",
            "Analyze promotional effects to support better pricing and "
            "promotion decisions."
        ),
        (
            "🔮 Demand Forecasting",
            "Use machine-learning forecasts as an input for future inventory "
            "and sales planning."
        )
    ]

    for title, description in recommendations:

        with st.expander(title):

            st.write(description)

    st.divider()

    st.success(
        "Project FORESIGHT connects machine-learning forecasting "
        "with practical retail business decisions."
    )
