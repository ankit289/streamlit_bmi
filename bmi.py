import streamlit as st

def calculate_bmi(height, weight):
    return weight / ((height/100) ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# Sidebar with BMI information
st.sidebar.title('BMI Information')
st.sidebar.write("""
BMI (Body Mass Index) is a measure of body fat based on your height and weight. It is commonly used to categorize individuals into underweight, normal weight, overweight, or obese.
""")
st.sidebar.write("""
- **Underweight:** BMI less than 18.5 😟
- **Normal weight:** BMI between 18.5 and 24.9 🙂
- **Overweight:** BMI between 25 and 29.9 😕
- **Obese:** BMI 30 or greater 😟
""")

st.title('BMI Calculator')

height = st.number_input('Height (in cm)', min_value=0.0, step=1.0)
weight = st.number_input('Weight (in kg)', min_value=0.0, step=0.1)

if st.button('Calculate BMI'):
    bmi = calculate_bmi(height, weight)
    bmi_category = interpret_bmi(bmi)
    
    # Display BMI value and category
    st.write(f'Your BMI is: **{bmi:.2f}**')
    st.write(f'You are in the **{bmi_category}** category.')
    
    # Display colored meter
    if bmi_category == 'Underweight':
        st.markdown("""
        <style>
        .meter { 
            height: 20px;
            width: 200px;
            background-color: #f4f4f4;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .meter-fill { 
            height: 100%;
            width: 100%;
            background-color: #2ecc71; 
            border-radius: 10px;
        }
        </style>
        <div class="meter">
          <div class="meter-fill"></div>
        </div>
        """, unsafe_allow_html=True)
    elif bmi_category == 'Normal weight':
        st.markdown("""
        <style>
        .meter { 
            height: 20px;
            width: 200px;
            background-color: #f4f4f4;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .meter-fill { 
            height: 100%;
            width: 100%;
            background-color: #f39c12; 
            border-radius: 10px;
        }
        </style>
        <div class="meter">
          <div class="meter-fill"></div>
        </div>
        """, unsafe_allow_html=True)
    elif bmi_category == 'Overweight':
        st.markdown("""
        <style>
        .meter { 
            height: 20px;
            width: 200px;
            background-color: #f4f4f4;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .meter-fill { 
            height: 100%;
            width: 100%;
            background-color: #e74c3c; 
            border-radius: 10px;
        }
        </style>
        <div class="meter">
          <div class="meter-fill"></div>
        </div>
        """, unsafe_allow_html=True)
    else:  # Obese
        st.markdown("""
        <style>
        .meter { 
            height: 20px;
            width: 200px;
            background-color: #f4f4f4;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .meter-fill { 
            height: 100%;
            width: 100%;
            background-color: #3498db; 
            border-radius: 10px;
        }
        </style>
        <div class="meter">
          <div class="meter-fill"></div>
        </div>
        """, unsafe_allow_html=True)
