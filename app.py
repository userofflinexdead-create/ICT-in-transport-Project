import streamlit as st

# Configure the page settings
st.set_page_config(
    page_title="ICT in Transport - Islamabad",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Menu Navigation
page = st.sidebar.radio(
    "Navigation Menu",
    ["Home", "Group Members", "Applications", "Uses & Benefits", "Energy Usage", "Challenges", "Gallery"]
)

# ----------------- HOME PAGE -----------------
if page == "Home":
    st.title("ICT in Transport")
    st.subheader("Islamabad Capital Territory Region")
    
    st.markdown("""
    Information and Communication Technology (ICT) plays a major role in modernizing transportation systems. 
    In the Islamabad Capital Territory, ICT helps manage traffic flow, reduces travel delays, and improves passenger safety. 
    By using smart technologies, the city is transforming its public transit and roads into a more efficient network.
    """)
    
    # Islamabad Metro Bus Image from Wikimedia
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/e/e0/Islamabad-Rawalpindi_Metro_Bus_System_Saddar_Station%2C_Rawalpindi.jpg",
        caption="Islamabad-Rawalpindi Metro Bus System System",
        use_container_width=True
    )

# ----------------- GROUP MEMBERS PAGE -----------------
elif page == "Group Members":
    st.title("Group Members")
    st.subheader("Project Team Details")
    
    # Student Data Table Dictionary
    students_data = {
        "Serial No.": [1, 2, 3, 4, 5],
        "Student Name": ["Huzaifa Ahmed", "Farhan Ali Shahid", "Shah Mohammad", "Mohammad Musab", "Syed Mohammad Aun"],
        "Roll Number": ["25-ME-68", "25-ME-204", "25-ME-140", "25-ME-60", "25-ME-224"]
    }
    st.table(students_data)

# ----------------- APPLICATIONS PAGE -----------------
elif page == "Applications":
    st.title("ICT Applications")
    st.subheader("Key Technologies in Modern Transport")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📷 Traffic Cameras / CCTV")
        st.write("Used to monitor road conditions and detect accidents in real time.")
        st.markdown("---")
        
        st.markdown("### 🗺️ GPS Tracking")
        st.write("Helps passengers track buses and drivers navigate using the shortest routes.")
        st.markdown("---")
        
        st.markdown("### 🎟️ E-Ticketing")
        st.write("Provides paperless, digital ticketing via mobile apps and smart cards.")
        
    with col2:
        st.markdown("### 🚦 Smart Traffic Signals")
        st.write("Changes signal timing automatically based on current vehicle rush.")
        st.markdown("---")
        
        st.markdown("### 💳 RFID Tolling")
        st.write("Allows vehicles to pay toll tax automatically without stopping at booths.")
        st.markdown("---")
        
        st.markdown("### 🔌 Electric Buses & Ride-hailing")
        st.write("Eco-friendly transport managed through smart mobile apps.")

# ----------------- USES & BENEFITS PAGE -----------------
elif page == "Uses & Benefits":
    st.title("Uses & Benefits")
    st.subheader("Why ICT is Crucial for Transportation")
    
    st.markdown("""
    * **Better Traffic Management:** Reduces traffic jams by adjusting signal timings dynamically.
    * **Enhanced Safety:** Monitoring roads helps prevent accidents and speeds up emergency response.
    * **Real-time Information:** Passengers get live arrival times for buses, saving them hours of waiting.
    * **Fuel Saving:** Smoother traffic flow means vehicles waste less fuel idling on roads.
    * **Better Planning:** Authorities can use traffic data to design better roads and public routes for the future.
    """)

# ----------------- ENERGY USAGE PAGE -----------------
elif page == "Energy Usage":
    st.title("Energy Usage & Environmental Impact")
    st.subheader("How ICT Interacts with Energy Consumption")
    
    st.markdown("### 1. How to Increase ICT Usage for Better Transport")
    st.write("Deploying more electronic devices like sensors, live cameras, and tracking systems makes public transit faster and more attractive. This massive deployment encourages citizens to shift away from private cars, lowering overall city energy footprints.")
    
    st.markdown("### 2. How to Decrease ICT Device Footprint to Save Server Energy")
    st.write("When traffic volume is extremely low (like late at night), certain electronic nodes, duplicate cameras, and backup servers can be put on automated standby or low-power modes to directly save electricity.")
    
    st.markdown("### 3. Methods to Reduce Energy Consumption")
    st.info("💡 **Optimized Routing:** Algorithms guide public fleets via the absolute shortest paths, dramatically reducing fuel waste.\n\n"
            "⏰ **Smart Scheduling:** Running fewer transport fleets during off-peak hours based on real historical data predictions avoids empty trips.")
    
    st.markdown("### 4. Input Methods: Speech-to-Text (STT) vs. Touch Buttons")
    st.warning("⚠️ **Energy Deficit Comparison:** Using STT (Speech-to-Text) requires heavy, continuous artificial intelligence computing power and active network transmission. This setup consumes **significantly more electrical energy** than a simple touch or physical button input.")

# ----------------- CHALLENGES PAGE -----------------
elif page == "Challenges":
    st.title("Challenges & Constraints")
    st.subheader("Minor Defects in Implementation")
    
    st.warning("🌐 **Network Issues:** Poor internet connectivity can cause delays in updating live bus tracking and digital payment processing.")
    st.warning("🔒 **Privacy Concerns:** Constant tracking and camera monitoring raise security worries for passenger data privacy.")
    st.warning("💰 **High Setup Cost:** Installing expensive sensors, servers, and automated tools requires a large initial financial investment.")

# ----------------- GALLERY PAGE -----------------
elif page == "Gallery":
    st.title("Visual Gallery")
    st.subheader("ICT Systems in Action")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/e/ec/Smart_Traffic_Light.jpg",
            caption="Smart Traffic Signal with Built-in Grid Sensors",
            use_container_width=True
        )
        
    with col2:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/b8/Traffic_control_camera_in_London.jpg",
            caption="High-Definition Closed-Circuit Traffic Camera",
            use_container_width=True
        )
