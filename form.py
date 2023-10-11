import streamlit as st

def main():
    st.title("Student Registration Form")

    # Input fields for student information
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    department = st.text_input("Department")
    address = st.text_area("Address")
    submit_button = st.button("Submit")

    if submit_button:
        # Display the submitted information
        st.write("Submitted Information:")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")
        st.write(f"Gender: {gender}")
        st.write(f"Department: {department}")
        st.write(f"Address: {address}")

if __name__ == "__main__":
    main()
