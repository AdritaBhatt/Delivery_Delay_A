# Create a DataFrame from the input values
input_data = pd.DataFrame([{
    'Delivery_Distance': delivery_distance,
    'Traffic_Congestion': traffic_congestion,
    'Weather_Condition': weather_condition,
    'Delivery_Slot': delivery_slot,
    'Driver_Experience': driver_experience,
    'Num_Stops': num_stops,
    'Vehicle_Age': vehicle_age,
    'Road_Condition_Score': road_condition_score,
    'Package_Weight': package_weight,
    'Fuel_Efficiency': fuel_efficiency,
    'Warehouse_Processing_Time': warehouse_processing_time
}])

if st.button('Predict Delivery Delay'):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    st.subheader('Prediction Result:')
    if prediction[0] == 1:
        st.error(f"Delivery is likely to be Delayed (Probability: {prediction_proba[0][1]:.2f})")
    else:
        st.success(f"Delivery is likely to be On Time (Probability: {prediction_proba[0][0]:.2f})")

st.write("\n--- Notes ---")
st.write("\n- **Delivery_Distance**: Distance for the delivery.")
st.write("- **Traffic_Congestion**: Level of traffic congestion (1=low, 5=high).")
st.write("- **Weather_Condition**: Severity of weather conditions (1=good, 5=severe).")
st.write("- **Delivery_Slot**: Designated time slot for delivery (1, 2, or 3).")
st.write("- **Driver_Experience**: Years of experience of the delivery driver.")
st.write("- **Num_Stops**: Number of stops the driver has to make.")
st.write("- **Vehicle_Age**: Age of the delivery vehicle.")
st.write("- **Road_Condition_Score**: Quality of road conditions (1=poor, 5=excellent).")
st.write("- **Package_Weight**: Weight of the package.")
st.write("- **Fuel_Efficiency**: Fuel efficiency of the vehicle.")
st.write("- **Warehouse_Processing_Time**: Time taken for package processing at the warehouse.")
