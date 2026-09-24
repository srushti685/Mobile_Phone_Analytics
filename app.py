import streamlit as st
import pandas as pd
import plotly.express as px
import joblib


# ---------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------

st.set_page_config(
    page_title="Mobile Phone Analytics",
   
    layout="wide"
)


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

data = pd.read_csv("mobile_powerbi_data.csv")
model_pipeline = joblib.load("model.pkl")


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title(" Mobile Phone Analytics Dashboard")

st.write(
    "Explore mobile phone prices, specifications, ratings and performance."
)


# ---------------------------------------------------
# SIDEBAR FILTER
# ---------------------------------------------------

st.sidebar.header(" Filters")

brand_list = sorted(data["brand"].dropna().unique().tolist())

selected_brand = st.sidebar.selectbox(
    "Select Brand",
    ["All Brands"] + brand_list
)


# Apply brand filter

if selected_brand == "All Brands":
    filtered_data = data.copy()
else:
    filtered_data = data[data["brand"] == selected_brand]


# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

st.subheader(" Key Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Phones",
        len(filtered_data)
    )

with col2:
    st.metric(
        "Average Price",
        f"₹{filtered_data['price_inr'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Maximum Price",
        f"₹{filtered_data['price_inr'].max():,.0f}"
    )

with col4:
    st.metric(
        "Minimum Price",
        f"₹{filtered_data['price_inr'].min():,.0f}"
    )


# ---------------------------------------------------
# CHART 1 - PHONES BY BRAND
# ---------------------------------------------------

st.subheader(" Number of Phones by Brand")

brand_count = (
    filtered_data["brand"]
    .value_counts()
    .reset_index()
)

brand_count.columns = ["brand", "count"]

fig1 = px.bar(
    brand_count,
    x="brand",
    y="count",
    title="Number of Phones by Brand"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)


# ---------------------------------------------------
# CHART 2 - AVERAGE PRICE BY BRAND
# ---------------------------------------------------

st.subheader(" Average Price by Brand")

brand_price = (
    filtered_data
    .groupby("brand")["price_inr"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    brand_price,
    x="brand",
    y="price_inr",
    title="Average Price by Brand"
)

fig2.update_yaxes(
    title="Average Price (₹)"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# ---------------------------------------------------
# CHART 3 - PRICE CATEGORY
# ---------------------------------------------------

st.subheader(" Price Category Distribution")

category_count = (
    filtered_data["price_category"]
    .value_counts()
    .reset_index()
)

category_count.columns = ["price_category", "count"]

fig3 = px.pie(
    category_count,
    names="price_category",
    values="count",
    title="Mobile Phones by Price Category"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


# ---------------------------------------------------
# MOBILE PHONE DETAILS
# ---------------------------------------------------

st.subheader(" Mobile Phone Details")

columns_to_show = [
    "name",
    "brand",
    "price_inr",
    "ram_gb",
    "storage_gb",
    "battery_mah",
    "user_rating_10",
    "expert_rating_10"
]

st.dataframe(
    filtered_data[columns_to_show],
    use_container_width=True
)


# ---------------------------------------------------
# SPECIFICATIONS & PERFORMANCE
# ---------------------------------------------------

st.header(" Specifications & Performance")

st.subheader(" RAM vs Price")

fig4 = px.scatter(
    filtered_data,
    x="ram_gb",
    y="price_inr",
    hover_name="name",
    title="RAM vs Price"
)

fig4.update_xaxes(title="RAM (GB)")
fig4.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ---------------------------------------------------
# STORAGE VS PRICE
# ---------------------------------------------------

st.subheader(" Storage vs Price")

fig5 = px.scatter(
    filtered_data,
    x="storage_gb",
    y="price_inr",
    hover_name="name",
    title="Storage vs Price"
)

fig5.update_xaxes(title="Storage (GB)")
fig5.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig5,
    use_container_width=True
)


# ---------------------------------------------------
# BATTERY VS PRICE
# ---------------------------------------------------

st.subheader(" Battery vs Price")

fig6 = px.scatter(
    filtered_data,
    x="battery_mah",
    y="price_inr",
    hover_name="name",
    title="Battery vs Price"
)

fig6.update_xaxes(title="Battery (mAh)")
fig6.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig6,
    use_container_width=True
)


# ---------------------------------------------------
# ANTUTU SCORE VS PRICE
# ---------------------------------------------------

st.subheader(" AnTuTu Score vs Price")

fig7 = px.scatter(
    filtered_data,
    x="antutu_score_num",
    y="price_inr",
    hover_name="name",
    title="AnTuTu Score vs Price"
)

fig7.update_xaxes(title="AnTuTu Score")
fig7.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig7,
    use_container_width=True
)


# ---------------------------------------------------
# DISPLAY SIZE VS PRICE
# ---------------------------------------------------

st.subheader(" Display Size vs Price")

fig8 = px.scatter(
    filtered_data,
    x="display_inches",
    y="price_inr",
    hover_name="name",
    title="Display Size vs Price"
)

fig8.update_xaxes(title="Display Size (inches)")
fig8.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig8,
    use_container_width=True
)


# ---------------------------------------------------
# REAR CAMERA VS PRICE
# ---------------------------------------------------

st.subheader(" Rear Camera vs Price")

fig9 = px.scatter(
    filtered_data,
    x="rear_camera_mp",
    y="price_inr",
    hover_name="name",
    title="Rear Camera vs Price"
)

fig9.update_xaxes(title="Rear Camera (MP)")
fig9.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig9,
    use_container_width=True
)


# ---------------------------------------------------
# USER RATING VS PRICE
# ---------------------------------------------------

st.subheader(" User Rating vs Price")

fig10 = px.scatter(
    filtered_data,
    x="user_rating_10",
    y="price_inr",
    hover_name="name",
    title="User Rating vs Price"
)

fig10.update_xaxes(title="User Rating (10)")
fig10.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig10,
    use_container_width=True
)


# ---------------------------------------------------
# EXPERT RATING VS PRICE
# ---------------------------------------------------

st.subheader(" Expert Rating vs Price")

fig11 = px.scatter(
    filtered_data,
    x="expert_rating_10",
    y="price_inr",
    hover_name="name",
    title="Expert Rating vs Price"
)

fig11.update_xaxes(title="Expert Rating (10)")
fig11.update_yaxes(title="Price (₹)")

st.plotly_chart(
    fig11,
    use_container_width=True
)


# ---------------------------------------------------
# USER RATING DISTRIBUTION
# ---------------------------------------------------

st.subheader(" User Rating Distribution")

fig12 = px.histogram(
    filtered_data,
    x="user_rating_10",
    nbins=10,
    title="Distribution of User Ratings"
)

fig12.update_xaxes(title="User Rating (10)")
fig12.update_yaxes(title="Number of Phones")

st.plotly_chart(
    fig12,
    use_container_width=True
)


# ---------------------------------------------------
# EXPERT RATING DISTRIBUTION
# ---------------------------------------------------

st.subheader(" Expert Rating Distribution")

fig13 = px.histogram(
    filtered_data,
    x="expert_rating_10",
    nbins=10,
    title="Distribution of Expert Ratings"
)

fig13.update_xaxes(title="Expert Rating (10)")
fig13.update_yaxes(title="Number of Phones")

st.plotly_chart(
    fig13,
    use_container_width=True
)


# ---------------------------------------------------
# TOP 10 PHONES BY USER RATING
# ---------------------------------------------------

st.header(" Top Mobile Phones")

st.subheader(" Top 10 Phones by User Rating")

top_user_rating = (
    filtered_data
    .sort_values("user_rating_10", ascending=False)
    .head(10)
)

fig14 = px.bar(
    top_user_rating,
    x="user_rating_10",
    y="name",
    orientation="h",
    title="Top 10 Phones by User Rating"
)

fig14.update_xaxes(title="User Rating (10)")
fig14.update_yaxes(title="Phone")

st.plotly_chart(
    fig14,
    use_container_width=True
)


# ---------------------------------------------------
# TOP 10 PHONES BY EXPERT RATING
# ---------------------------------------------------

st.subheader(" Top 10 Phones by Expert Rating")

top_expert_rating = (
    filtered_data
    .sort_values("expert_rating_10", ascending=False)
    .head(10)
)

fig15 = px.bar(
    top_expert_rating,
    x="expert_rating_10",
    y="name",
    orientation="h",
    title="Top 10 Phones by Expert Rating"
)

fig15.update_xaxes(title="Expert Rating (10)")
fig15.update_yaxes(title="Phone")

st.plotly_chart(
    fig15,
    use_container_width=True
)


# ---------------------------------------------------
# TOP 10 PHONES BY SPECIFICATION SCORE
# ---------------------------------------------------

st.subheader(" Top 10 Phones by Specification Score")

top_spec_score = (
    filtered_data
    .sort_values("spec_score", ascending=False)
    .head(10)
)

fig16 = px.bar(
    top_spec_score,
    x="spec_score",
    y="name",
    orientation="h",
    title="Top 10 Phones by Specification Score"
)

fig16.update_xaxes(title="Specification Score")
fig16.update_yaxes(title="Phone")

st.plotly_chart(
    fig16,
    use_container_width=True
)


# ---------------------------------------------------
# PRICE PREDICTION
# ---------------------------------------------------

st.header(" Mobile Phone Price Prediction")

st.write("Enter the phone specifications below to predict its price.")

col1, col2 = st.columns(2)

with col1:

    brand_input = st.selectbox(
        "Brand",
        sorted(data["brand"].dropna().unique())
    )

    processor_input = st.selectbox(
        "Processor",
        sorted(data["processor"].dropna().unique())
    )

    spec_score_input = st.number_input(
        "Specification Score",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    ram_input = st.number_input(
        "RAM (GB)",
        min_value=1.0,
        max_value=32.0,
        value=8.0
    )

    storage_input = st.number_input(
        "Storage (GB)",
        min_value=1.0,
        max_value=2048.0,
        value=128.0
    )

    battery_input = st.number_input(
        "Battery (mAh)",
        min_value=500.0,
        max_value=10000.0,
        value=5000.0
    )

with col2:

    display_input = st.number_input(
        "Display Size (inches)",
        min_value=3.0,
        max_value=10.0,
        value=6.5
    )

    antutu_input = st.number_input(
        "AnTuTu Score",
        min_value=0.0,
        value=500000.0
    )

    rear_camera_input = st.number_input(
        "Rear Camera (MP)",
        min_value=0.0,
        max_value=250.0,
        value=50.0
    )

    front_camera_input = st.number_input(
        "Front Camera (MP)",
        min_value=0.0,
        max_value=100.0,
        value=16.0
    )

    user_rating_input = st.number_input(
        "User Rating (10)",
        min_value=0.0,
        max_value=10.0,
        value=8.0
    )

    expert_rating_input = st.number_input(
        "Expert Rating (10)",
        min_value=0.0,
        max_value=10.0,
        value=8.0
    )


if st.button(" Predict Price"):

    input_data = pd.DataFrame({
        "brand": [brand_input],
        "processor": [processor_input],
        "spec_score": [spec_score_input],
        "ram_gb": [ram_input],
        "storage_gb": [storage_input],
        "battery_mah": [battery_input],
        "display_inches": [display_input],
        "antutu_score_num": [antutu_input],
        "rear_camera_mp": [rear_camera_input],
        "front_camera_mp": [front_camera_input],
        "user_rating_10": [user_rating_input],
        "expert_rating_10": [expert_rating_input]
    })

    predicted_price = model_pipeline.predict(input_data)[0]

    st.success(
        f"Predicted Price: ₹{predicted_price:,.0f}"
    )
