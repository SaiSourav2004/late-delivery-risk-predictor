import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# --- Page Config & Styling ---
st.set_page_config(
    page_title="Supply Chain Operations | Late Delivery Risk",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a professional dashboard look
st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #1E3A8A;
    }
    .risk-high { background-color: #FEE2E2; padding: 20px; border-radius: 10px; border-left: 5px solid #EF4444; }
    .risk-med { background-color: #FEF3C7; padding: 20px; border-radius: 10px; border-left: 5px solid #F59E0B; }
    .risk-low { background-color: #D1FAE5; padding: 20px; border-radius: 10px; border-left: 5px solid #10B981; }
    .stProgress > div > div > div > div {
        background-color: #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)

# --- Load ML Assets ---
@st.cache_resource
def load_assets():
    try:
        model = joblib.load("late_delivery_model.pkl")
        preprocessor = joblib.load("preprocessor.pkl")
        return model, preprocessor
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None

model, preprocessor = load_assets()

# --- Header Section ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("📦 Supply Chain Operations Dashboard")
    st.markdown("### Pre-Shipment Delivery Risk Assessment (POC)")
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2760/2760124.png", width=80) # Generic logistics icon
st.markdown("---")

# --- Form UI ---
with st.form("prediction_form"):
    st.markdown("#### Enter Order Details for Risk Assessment")
    
    # Create 4 logical business sections using columns
    col_cust, col_prod = st.columns(2)
    col_order, col_ship = st.columns(2)
    
    with col_cust:
        st.subheader("👤 Customer Information")
        customer_segment = st.selectbox("Customer Segment", ["Consumer", "Corporate", "Home Office"])
        customer_country = st.selectbox("Customer Country", ["EE. UU.", "Puerto Rico", "India", "Germany", "UK", "Other"])
        customer_state = st.selectbox("Customer State", ["CA", "NY", "TX", "FL", "IL", "Other"])
        
    with col_prod:
        st.subheader("🏷️ Product Information")
        department_name = st.selectbox("Department", ["Fitness", "Apparel", "Footwear", "Golf", "Outdoors", "Fan Shop"])
        category_name = st.selectbox("Category Name", ["Sporting Goods", "Cleats", "Women's Apparel", "Men's Footwear", "Cardio Equipment", "Accessories"])
        product_price = st.number_input("Unit Price ($)", min_value=1.0, value=59.99, step=1.0)

    st.markdown("<br>", unsafe_allow_html=True) # Spacer

    with col_order:
        st.subheader("🛒 Order Information")
        payment_type = st.selectbox("Payment Method", ["DEBIT", "TRANSFER", "PAYMENT", "CASH"])
        order_quantity = st.number_input("Order Quantity", min_value=1, max_value=50, value=1, step=1)
        
    with col_ship:
        st.subheader("🚚 Shipping Information")
        market = st.selectbox("Target Market", ["Pacific Asia", "USCA", "Europe", "Africa", "LATAM"])
        order_region = st.selectbox("Destination Region", ["South Asia", "Western Europe", "Central America", "North America", "Oceania"])
        order_country = st.selectbox("Destination Country", ["India", "USA", "Mexico", "France", "Australia", "China", "Other"])
        shipping_mode = st.selectbox("Requested Shipping Mode", ["Standard Class", "First Class", "Second Class", "Same Day"])

    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button("🔍 Run Risk Assessment", use_container_width=True)

# --- Background Business Logic & Calculations ---
# This hides the technical fields from the user while keeping the ML pipeline happy.
if submit_button:
    if model is None or preprocessor is None:
        st.error("⚠️ System Offline: Machine Learning model assets (.pkl files) are missing.")
    else:
        # Standard Business Assumptions
        discount_rate = 0.05       # Assume 5% standard discount
        profit_margin = 0.20       # Assume 20% standard profit margin
        
        # Derived Financials (Automated so user doesn't have to do math)
        sales = product_price * order_quantity
        discount_amount = sales * discount_rate
        order_item_total = sales - discount_amount
        profit_per_order = order_item_total * profit_margin
        
        # Build the DataFrame with EXACT feature names required by the notebook
        input_dict = {
            'Type': payment_type,
            'Benefit per order': profit_per_order,             # Auto-calculated
            'Sales per customer': order_item_total,            # Auto-calculated
            'Category Name': category_name,
            'Customer Country': customer_country,
            'Customer Segment': customer_segment,
            'Customer State': customer_state,
            'Department Name': department_name,
            'Latitude': 18.0,                                  # Default static value
            'Longitude': -66.0,                                # Default static value
            'Market': market,
            'Order Country': order_country,
            'Order Item Discount': discount_amount,            # Auto-calculated
            'Order Item Discount Rate': discount_rate,         # Default assumption
            'Order Item Product Price': product_price,         # Mirrored from Product Price
            'Order Item Profit Ratio': profit_margin,          # Default assumption
            'Order Item Quantity': order_quantity,
            'Sales': sales,                                    # Auto-calculated
            'Order Item Total': order_item_total,              # Auto-calculated
            'Order Profit Per Order': profit_per_order,        # Auto-calculated
            'Order Region': order_region,
            'Product Price': product_price,
            'Product Status': "0",                             # Assuming 0 = normal/in-stock status
            'Shipping Mode': shipping_mode
        }
        
        input_df = pd.DataFrame([input_dict])

        # --- ML Prediction ---
        with st.spinner("Analyzing historical supply chain data..."):
            try:
                # Transform and Predict
                processed_data = preprocessor.transform(input_df)
                probability = model.predict_proba(processed_data)[0][1] # Probability of Class 1 (Late)
                
                # --- Result Presentation ---
                st.markdown("---")
                st.subheader("📊 Assessment Results")
                
                # Determine Risk Categories and Executive Summary
                if probability >= 0.70:
                    risk_level = "High Risk"
                    summary = "The order is facing severe logistical bottlenecks and is highly likely to be delayed."
                    recommendation = "**Action Required:** Upgrade shipping to 'First Class' or 'Same Day' and proactively communicate with the customer."
                    status_alert = st.error
                elif probability >= 0.40:
                    risk_level = "Medium Risk"
                    summary = "The order has moderate risk factors. Monitor warehouse dispatch closely."
                    recommendation = "**Monitor Closely:** Ensure warehouse dispatch occurs within 24 hours to avoid cascading delays."
                    status_alert = st.warning
                else:
                    risk_level = "Low Risk"
                    summary = "The order is expected to be delivered on time with a low delay risk."
                    recommendation = "**On Track:** Proceed with standard logistics operations."
                    status_alert = st.success

                # 1. KPI Metrics Section
                col_kpi1, col_kpi2 = st.columns(2)
                with col_kpi1:
                    st.metric(label="Assessed Risk Level", value=risk_level)
                with col_kpi2:
                    st.metric(label="Delay Probability", value=f"{probability:.1%}")

                # 2. Executive Summary
                st.markdown("#### Executive Summary")
                status_alert(summary)

                # 3. Recommendation
                st.markdown("#### 📋 Recommendation")
                st.info(recommendation)
                    
                # 4. Top Risk Factors
                st.markdown("#### 🔍 Top Risk Factors")
                st.markdown(f"- **Destination:** {order_region} ({order_country})")
                st.markdown(f"- **Product Dept:** {department_name}")
                st.markdown(f"- **Customer Segment:** {customer_segment}")

            except Exception as e:
                st.error(f"Prediction Error: Please check input formats. Details: {str(e)}")