import streamlit as st
import pandas as pd
import plotly.express as px


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Analytics for Metro Atlanta Nonprofits",
    page_icon="📊",
    layout="wide"
)


# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    [
        "Home",
        "About Me",
        "Services",
        "Examples of Work",
        "Analytics Demo",
        "Contact"
    ]
)



# -------------------------
# Home Page
# -------------------------

if page == "Home":

    st.title("📊 Analytics for Metro Atlanta Nonprofits")

    st.subheader(
        "Helping nonprofits spend less time managing spreadsheets "
        "and more time serving their communities."
    )


    st.write(
        """
        Many nonprofits collect valuable information about their programs,
        donors, volunteers, and communities — but that information often
        lives across dozens of spreadsheets and disconnected systems.

        I help organizations organize their data, automate reports,
        and create simple dashboards so leaders can make informed decisions.
        """
    )


    st.success(
        """
        Free Data Analytics Support for Local Organizations
        """
    )


    st.divider()


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "Education",
            "M.S. Applied" \
            " Mathematics"
        )


    with col2:
        st.metric(
            "Specialty",
            "Statistics & Analytics"
        )


    with col3:
        st.metric(
            "Location",
            "Lilburn, GA"
        )



# -------------------------
# About Me
# -------------------------

elif page == "About Me":

    st.title("About Me")


    col1, col2 = st.columns([1,2])


    with col1:
        st.image(
            "Images/headshot.JPG",
            width=350
        )


    with col2:

        st.write(
        """
        My name is Edgar Derricho, and I am a Gwinnett County native
        with a Master's degree in Applied Mathematics with a concentration
        in Statistics from Georgia State University.

        I specialize in helping organizations turn messy data into clear,
        useful information.

        As a way of serving my community, I volunteer my analytics skills
        to nonprofit organizations throughout Metro Atlanta.
        """
        )


    st.divider()


    st.subheader("My Goal")

    st.info(
        """
        Help organizations spend less time fighting with spreadsheets
        and more time focused on their mission.
        """
    )


# -------------------------
# Services
# -------------------------

elif page == "Services":

    st.title("How I Can Help")


    services = {

    "Data Cleaning & Organization":
    [
        "Clean Excel spreadsheets",
        "Remove duplicate records",
        "Standardize information",
        "Create maintainable systems"
    ],


    "Automated Reports & Dashboards":
    [
        "Program participation reports",
        "Donation dashboards",
        "Volunteer reports",
        "Grant reporting summaries",
        "Leadership KPI dashboards"
    ],


    "Data Consolidation":
    [
        "Excel files",
        "Google Sheets",
        "CSV files",
        "Databases"
    ],


    "Volunteer & Donor Analytics":
    [
        "Volunteer trends",
        "Donor patterns",
        "Program participation",
        "Community reach"
    ],


    "Database Creation":
    [
        "Secure data storage",
        "Easy searching",
        "Fast reporting"
    ],


    "Advanced Analytics":
    [
        "Growth analysis",
        "Resource allocation",
        "Trend identification",
        "Program improvement"
    ]

    }


    for title, items in services.items():

        with st.expander(title):

            for item in items:
                st.write("✓", item)


# -------------------------
# Examples
# -------------------------

elif page == "Examples of Work":

    st.title("Examples of My Work")


    st.subheader(
        "Example 1: Nonprofit Impact Dashboard"
    )


    st.write(
        """
        Before:

        - Multiple spreadsheets
        - Manual reporting
        - Difficult trend analysis

        

        After:

        - Interactive dashboard
        - Automated summaries
        - Leadership metrics
        """
    )

    st.image(
                "Images/dashboard.png",
                width=1000
            )

    st.divider()


    st.subheader(
        "Example 2: Data Cleaning Project"
    )


    st.write(
        """
        Before:

        - Duplicate records
        - Missing information
        - Inconsistent formatting

        """
    )

    st.image(
            "Images/before_spreadsheet.png",
            width=1000
    )
    
    st.write(
        """
        After:
    
            - Organized database
            - Clean reporting structure
            - Easier access
            """
    )
        
    st.image(
        "Images/after_spreadsheet.png",
        width=1000
    )
    
# -------------------------
# Analytics Demo
# -------------------------

elif page == "Analytics Demo":

    st.title("📈 Nonprofit Impact Analytics Dashboard")

    st.write(
        """
        This dashboard demonstrates how nonprofit organizations can
        analyze volunteer engagement, financial performance,
        and program impact.
        """
    )


    # -------------------------
    # Create Example Dataset
    # -------------------------

    data = pd.DataFrame({

        "Year":
        [
            2020,2020,2020,2020,2020,
            2021,2021,2021,2021,2021,
            2022,2022,2022,2022,2022,
            2023,2023,2023,2023,2023,
            2024,2024,2024,2024,2024
        ],


        "Event Type":
        [
            "Food Drive",
            "Community Outreach",
            "Youth Program",
            "Fundraiser",
            "Training",

            "Food Drive",
            "Community Outreach",
            "Youth Program",
            "Fundraiser",
            "Training",

            "Food Drive",
            "Community Outreach",
            "Youth Program",
            "Fundraiser",
            "Training",

            "Food Drive",
            "Community Outreach",
            "Youth Program",
            "Fundraiser",
            "Training",

            "Food Drive",
            "Community Outreach",
            "Youth Program",
            "Fundraiser",
            "Training"
        ],


        "Volunteers":
        [
            35,45,25,60,20,
            40,55,30,75,25,
            50,65,40,90,35,
            60,80,50,110,45,
            70,95,65,130,55
        ],


        "Volunteer Hours":
        [
            140,220,180,300,100,
            170,280,230,380,130,
            220,340,300,450,170,
            270,430,360,560,220,
            320,520,470,700,280
        ],


        "Revenue":
        [
            5000,7000,4000,15000,2000,
            6500,9000,5500,18000,3000,
            8000,11000,7500,22000,4000,
            9500,14000,9000,27000,5000,
            12000,17000,12000,32000,7000
        ],


        "Expenses":
        [
            2500,3500,2000,7000,1000,
            3000,4500,2500,8500,1500,
            3500,5500,3500,10000,2000,
            4500,7000,4500,12000,2500,
            5500,8500,6000,14000,3000
        ]

    })


    data["Net Impact"] = (
        data["Revenue"] -
        data["Expenses"]
    )



    # -------------------------
    # Filters
    # -------------------------


    st.sidebar.subheader("Dashboard Filters")


    start_year = st.sidebar.selectbox(
        "Starting Year",
        sorted(data["Year"].unique()),
        index=0
    )


    end_year = st.sidebar.selectbox(
        "Ending Year",
        sorted(data["Year"].unique()),
        index=4
    )


    event_options = [
        "All Events"
    ] + sorted(
        data["Event Type"].unique()
    )


    selected_event = st.sidebar.selectbox(
        "Event Type",
        event_options
    )



    # Filter Data

    filtered = data[
        (data["Year"] >= start_year) &
        (data["Year"] <= end_year)
    ]


    if selected_event != "All Events":

        filtered = filtered[
            filtered["Event Type"]
            == selected_event
        ]



    # -------------------------
    # KPI Metrics
    # -------------------------


    total_revenue = filtered["Revenue"].sum()

    total_volunteers = filtered["Volunteers"].sum()

    total_hours = filtered["Volunteer Hours"].sum()


    revenue_per_volunteer = (
        total_revenue /
        total_volunteers
    )


    revenue_per_hour = (
        total_revenue /
        total_hours
    )


    col1,col2,col3,col4 = st.columns(4)


    col1.metric(
        "Total Revenue",
        f"${total_revenue:,.0f}"
    )


    col2.metric(
        "Volunteers",
        f"{total_volunteers:,}"
    )


    col3.metric(
        "Revenue / Volunteer",
        f"${revenue_per_volunteer:,.2f}"
    )


    col4.metric(
        "Revenue / Volunteer Hour",
        f"${revenue_per_hour:,.2f}"
    )



    st.divider()



    # -------------------------
    # Revenue Efficiency Charts
    # -------------------------


    yearly = (
        filtered
        .groupby("Year")
        .sum(numeric_only=True)
        .reset_index()
    )


    yearly["Revenue per Volunteer"] = (
        yearly["Revenue"] /
        yearly["Volunteers"]
    )


    yearly["Revenue per Volunteer Hour"] = (
        yearly["Revenue"] /
        yearly["Volunteer Hours"]
    )



    fig1 = px.line(
        yearly,
        x="Year",
        y="Revenue per Volunteer",
        markers=True,
        title="Revenue per Volunteer Over Time"
    )


    st.plotly_chart(
        fig1,
        use_container_width=True
    )



    fig2 = px.line(
        yearly,
        x="Year",
        y="Revenue per Volunteer Hour",
        markers=True,
        title="Revenue per Volunteer Hour Over Time"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



    # -------------------------
    # Volunteer Hours by Event
    # -------------------------


    event_hours = (
        filtered
        .groupby("Event Type")
        ["Volunteer Hours"]
        .sum()
        .reset_index()
    )


    fig3 = px.bar(
        event_hours,
        x="Event Type",
        y="Volunteer Hours",
        title="Volunteer Hours by Event Type"
    )


    st.plotly_chart(
        fig3,
        use_container_width=True
    )


# -------------------------
# Contact
# -------------------------

elif page == "Contact":

    st.title("Interested in Improving Your Organization's Data?")


    st.write(
        """
        I would love to meet with your organization and learn about
        your current challenges.

        Whether you need help organizing spreadsheets, creating reports,
        or understanding your data better, I am happy to discuss ways
        I can help.
        """
    )


    st.write(
        """
        **Edgar Derricho**

        📧 ederricho@yahoo.com

        LinkedIn: https://www.linkedin.com/in/edgar-d25489/

        Portfolio: https://public.tableau.com/app/profile/edgar.derricho1935/vizzes
        """
    )
