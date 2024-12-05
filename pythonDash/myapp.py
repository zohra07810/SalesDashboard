import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image  # To handle image


# Set the title of the app and customize the page layout
st.set_page_config(page_title="Twin A Furniture", layout="wide")

# Display Logo and Title
col1, col2 = st.columns([1, 5])  # Create two columns for logo and title
with col1:
    # Replace 'logo.png' with the actual file path or URL of your logo image
    logo = Image.open("pythonDash/twin.jpg")  # Adjust the path to your logo file
    st.image(logo, width=150)  # Adjust logo size (resize to 150px width)
with col2:
    st.title("Twin A Furniture")

    st.markdown("""
    **Mission:** To provide **Quality Furniture** at Extremely Competitive Low Prices that Every Family can Afford to Buy.  
    
    """)

# Display images below the description
st.subheader("Gallery")
col3, col4, col5, col6, col7, col8 = st.columns(6)  # Create three columns for pictures
image_size = (130, 130)  # Set a fixed width and height for the images

with col3:
    # Replace 'furniture1.jpg' with the actual file path or URL of your first image
    furniture1 = Image.open("doors.jpg")  # Adjust the path to your image
    furniture1_resized = furniture1.resize(image_size)  # Resize the image
    st.image(furniture1_resized, caption="", use_container_width=True)
with col4:
    # Replace 'furniture2.jpg' with the actual file path or URL of your second image
    furniture2 = Image.open("set.jpg")  # Adjust the path to your image
    furniture2_resized = furniture2.resize(image_size)  # Resize the image
    st.image(furniture2_resized, caption="", use_container_width=True)
with col5:
    # Replace 'furniture3.jpg' with the actual file path or URL of your third image
    furniture3 = Image.open("twinShop.jpg")  # Adjust the path to your image
    furniture3_resized = furniture3.resize(image_size)  # Resize the image
    st.image(furniture3_resized, caption="", use_container_width=True)
with col6:
    # Replace 'furniture3.jpg' with the actual file path or URL of your third image
    furniture4 = Image.open("tablewood.jpg")  # Adjust the path to your image
    furniture4_resized = furniture4.resize(image_size)  # Resize the image
    st.image(furniture4_resized, caption="", use_container_width=True)
with col7:
    # Replace 'furniture3.jpg' with the actual file path or URL of your third image
    furniture5 = Image.open("stairs.jpg")  # Adjust the path to your image
    furniture5_resized = furniture5.resize(image_size)  # Resize the image
    st.image(furniture5_resized, caption="", use_container_width=True)
with col8:
    # Replace 'furniture3.jpg' with the actual file path or URL of your third image
    furniture6 = Image.open("cabinet.jpg")  # Adjust the path to your image
    furniture6_resized = furniture6.resize(image_size)  # Resize the image
    st.image(furniture6_resized, caption="", use_container_width=True)


# Apply custom CSS for a black background and styled text
page_bg_style = """
<style>
    body {
        background-color: black;
        color: white;
    }
    .stMarkdown {
        color: black;
    }
    .stDataFrame tbody tr {
        background-color: #333;
        color: white;
    }
    .stDataFrame thead {
        background-color: #444;
        color: white;
    }
   .card {
    width: 170px;  /* Adjust width */
    height: 80px;   /* Reduce height */
    background-color: #333333;
    margin-right: 15px;  /* Add space between cards horizontally */
    padding: 5px;
    text-align: center;
    border-radius: 8px;
    color: white;  /* Ensure text color is white */
}

.card .value {
    font-size: 20px;  /* Adjust font size */
    font-weight: bold;
}

</style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

# File upload widget
uploaded_file = st.file_uploader("Upload an Excel File", type=["xlsx", "xls"])

# Process the uploaded file
if uploaded_file is not None:
    try:
        # Read the uploaded file
        df = pd.read_excel(uploaded_file)

        # Check for required columns
        required_columns = ['Total', 'Material Cost', 'Labor Cost', 'month', 'status', 'category']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"The following required columns are missing from the file: {', '.join(missing_columns)}")
        else:

        # Display the uploaded file preview
          st.subheader("Preview of Uploaded File")
          st.dataframe(df)

        # Display Basic Statistics and Plot Chart in the same row
        st.subheader("Basic Data Statistics")
        stats_col1, stats_col2 = st.columns([2, 3])  # Two columns for basic stats and plot chart
        
        with stats_col1:
            st.write(df.describe())

        with stats_col2:
            # Plot a simple chart based on the data, for example, 'Total Sales' distribution
            if 'Total' in df.columns:
                fig = px.histogram(df, x='Total', title="Distribution of Total Sales")
                fig.update_layout(
                    plot_bgcolor="black",
                    paper_bgcolor="black",
                    font=dict(color="white"),
                    title_font=dict(color="white"),
                    xaxis_title_font=dict(color="white"),
                    yaxis_title_font=dict(color="white"),
                    xaxis_tickfont=dict(color="white"),
                    yaxis_tickfont=dict(color="white")
                )
                st.plotly_chart(fig, use_container_width=True)

        # Sales Dashboard Title (placed above the cards)
        st.subheader("Sales Key Metrics")

        # Create a row with columns for cards (horizontal)
        cards_col1, cards_col2, cards_col3, cards_col4 = st.columns(4)  # 4 columns for 4 cards

        # Card for Total Sales
        with cards_col1:
            if 'Total' in df.columns:
                total_sales = df['Total'].sum()
                st.markdown(
                    f"<div class='card'><div class='value'>₱{int(total_sales):,}</div><div>Total Sales</div></div>",
                    unsafe_allow_html=True
                     )

        # Card for Material Costs
        with cards_col2:
            if 'Material Cost' in df.columns:
                total_material_costs = df['Material Cost'].sum()
                st.markdown(
                 f"<div class='card'><div class='value'>₱{int(total_material_costs):,}</div><div>Material Costs</div></div>",
                   unsafe_allow_html=True
                    )

        # Card for Labor Costs
        with cards_col3:
            if 'Labor Cost' in df.columns:
                total_labor_costs = df['Labor Cost'].sum()
                st.markdown(
                 f"<div class='card'><div class='value'>₱{int(total_labor_costs):,}</div><div>Labor Costs</div></div>",
                   unsafe_allow_html=True
                    )
        # Card for Total Orders (Counting rows)
        with cards_col4:
            total_orders = len(df)
            st.markdown(
                f"<div class='card'><div class='value'>{total_orders}</div><div>Total Orders</div></div>",
                  unsafe_allow_html=True
                   )

        # Create columns for Bar Chart, Donut Chart, and Pending vs Finished Projects
        chart_col1, chart_col2, chart_col3 = st.columns(3)

        # Sales by Category Bar Chart
        if 'category' in df.columns and 'Total' in df.columns:
            with chart_col1:
                st.markdown("<h3 style='text-align: center;'></h3>", unsafe_allow_html=True)
                sales_by_category = df.groupby('category')['Total'].sum().reset_index()
                fig_bar = px.bar(
                    sales_by_category, 
                    x='category', 
                    y='Total', 
                    title="Sales by Product", 
                    color_discrete_sequence=["#FFA07A"]
                )
                fig_bar.update_layout(
                    height=250,
                    margin=dict(l=20, r=20, t=30, b=20),
                    plot_bgcolor="black",
                    paper_bgcolor="black",
                    font=dict(color="white"),
                    title_font=dict(color="white"),
                    xaxis_title_font=dict(color="white"),
                    yaxis_title_font=dict(color="white"),
                    xaxis_tickfont=dict(color="white"),
                    yaxis_tickfont=dict(color="white"),
                    yaxis_title="Sales", 
                    xaxis_title="Products"
                )
                st.plotly_chart(fig_bar, use_container_width=True)

        # Donut Chart for Material vs Labor Costs
        if 'Material Cost' in df.columns and 'Labor Cost' in df.columns:
            with chart_col2:
                st.markdown("<h3 style='text-align: center;'></h3>", unsafe_allow_html=True)
                material_total = df['Material Cost'].sum()
                labor_total = df['Labor Cost'].sum()
                donut_data = pd.DataFrame({
                    "Cost Type": ["Material Cost", "Labor Cost"],
                    "Total": [material_total, labor_total]
                })
                fig_donut = px.pie(
                    donut_data, 
                    values='Total', 
                    names='Cost Type', 
                    hole=0.4, 
                    title="Cost Distribution", 
                    color_discrete_sequence=["#1E90FF", "#FF4500"]
                )
                fig_donut.update_layout(
                    height=250,
                    margin=dict(l=20, r=20, t=30, b=20),
                    plot_bgcolor="black",
                    paper_bgcolor="black",
                    font=dict(color="white"),
                    title_font=dict(color="white"),
                    legend_font=dict(color="white")
                )
                st.plotly_chart(fig_donut, use_container_width=True)

        # Pending vs Finished Projects by Month (Stacked Bar Chart)
        if 'month' in df.columns and 'status' in df.columns:
            with chart_col3:
                st.markdown("<h3 style='text-align: center;'></h3>", unsafe_allow_html=True)
                status_by_month = df.groupby(['month', 'status']).size().reset_index(name='Project Count')
                fig_status = px.bar(
                    status_by_month, 
                    x='month', 
                    y='Project Count', 
                    color='status', 
                    title="Pending vs Finished Projects by Month", 
                    barmode='stack', 
                    color_discrete_sequence=["#32CD32", "#FF6347"]
                )
                fig_status.update_layout(
                    height=250,
                    margin=dict(l=20, r=20, t=30, b=20),
                    plot_bgcolor="black",
                    paper_bgcolor="black",
                    font=dict(color="white"),
                    title_font=dict(color="white"),
                    xaxis_title_font=dict(color="white"),
                    yaxis_title_font=dict(color="white"),
                    xaxis_tickfont=dict(color="white"),
                    yaxis_tickfont=dict(color="white"),
                    legend_font=dict(color="white")
                )
                st.plotly_chart(fig_status, use_container_width=True)

        # Interactive Visualization for Total Sales by Month or All Months (Moved Below Charts)
        st.subheader("Interactive Visualization: Total Sales")

        # Option to choose between sales by selected month or all months
        sales_option = st.selectbox("Choose an option to visualize total sales", 
                                    ("Total Sales for a Selected Month", "Total Sales for All Months"))

        if 'month' in df.columns and 'Total' in df.columns:
            if sales_option == "Total Sales for a Selected Month":
                # Select a month for visualization
                months = df['month'].unique()
                selected_month = st.selectbox("Select a Month to View Total Sales", months)

                # Filter data for selected month and calculate total sales
                sales_by_month = df[df['month'] == selected_month].groupby('month')['Total'].sum().reset_index()

                # Display total sales for selected month
                st.write(f"Total Sales for {selected_month}: {sales_by_month['Total'].values[0]:,.2f}")

                # Plot sales data for the selected month
                fig_sales_month = px.bar(sales_by_month, x='month', y='Total', 
                                        title=f"Total Sales for {selected_month}", 
                                        color_discrete_sequence=["#98C5E5"])
                fig_sales_month.update_layout(
                    plot_bgcolor="black",
                    paper_bgcolor="black",
                    font=dict(color="white"),
                    title_font=dict(color="white"),
                    xaxis_title_font=dict(color="white"),
                    yaxis_title_font=dict(color="white"),
                    xaxis_tickfont=dict(color="white"),
                    yaxis_tickfont=dict(color="white")
                )
                st.plotly_chart(fig_sales_month, use_container_width=True)

            elif sales_option == "Total Sales for All Months":
    
        # Calculate total sales by month
             sales_by_month = df.groupby('month')['Total'].sum().reset_index()
        sales_by_month['Type'] = 'Actual'  # Label the actual sales

        # Forecast sales for the next two months
        forecasted_sales = sales_by_month['Total'].mean()
        next_months = ['Next Month 1', 'Next Month 2']  # Replace with actual month names if available
        forecast_data = pd.DataFrame({
            'month': next_months,
            'Total': [forecasted_sales, forecasted_sales],
            'Type': 'Forecasted'  # Label the forecasted sales
        })

        # Combine actual and forecasted data
        sales_with_forecast = pd.concat([sales_by_month, forecast_data], ignore_index=True)

        # Plot sales data for all months including forecasts
        fig_sales_all = px.bar(
            sales_with_forecast,
            x='month',
            y='Total',
            title="Total Sales for All Months (Including Forecasts)",
            color='Type',  # Use the 'Type' column for color mapping
            color_discrete_map={
                'Actual': "#4682B4",  # Blue color for actual sales
                'Forecasted': "#FFC0CB"  # Pink color for forecasted sales
            }
        )
        
        # Update layout for styling
        fig_sales_all.update_layout(
            plot_bgcolor="black",
            paper_bgcolor="black",
            font=dict(color="white"),
            title_font=dict(color="white"),
            xaxis_title_font=dict(color="white"),
            yaxis_title="Total Sales",  # Set y-axis label
            yaxis_title_font=dict(color="white"),
            xaxis_tickfont=dict(color="white"),
            yaxis_tickfont=dict(color="white"),
            legend_title_font=dict(color="white"),  # Set legend title font color
            legend_font=dict(color="white")  # Set legend text color
        )

        # Display the chart
        st.plotly_chart(fig_sales_all, use_container_width=True)
    
    except Exception as e:
        st.error(f"Error loading file: {e}")


            

            

                
