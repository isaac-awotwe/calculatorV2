# import streamlit as st

# # App title
# st.title("🧮 My Python Calculator")

# # # Display a short welcome message
# # st.write("Welcome to My Python Calculator! Choose an operation and enter two numbers to calculate.")

# # # Define available operations
# # operations = ['+', '-', '*', '/']

# # # Input fields for the numbers
# # first_number = st.number_input("Enter the first number:", value=0.0, step=1.0)
# # operation = st.selectbox("Select an operation:", operations)
# # second_number = st.number_input("Enter the second number:", value=0.0, step=1.0)

# # # Calculate button
# # if st.button("Calculate"):
# #     if operation == '+':
# #         answer = first_number + second_number
# #     elif operation == '-':
# #         answer = first_number - second_number
# #     elif operation == '*':
# #         answer = first_number * second_number
# #     elif operation == '/':
# #         # Handle division by zero
# #         if second_number == 0:
# #             st.error("Error: Cannot divide by zero.")
# #         else:
# #             answer = first_number / second_number
# #     else:
# #         answer = None

# #     # Display result if valid
# #     if operation != '/' or second_number != 0:
# #         st.success(f"✅ Result: {first_number} {operation} {second_number} = {answer}")





# # import streamlit as st

# # if 'stage' not in st.session_state:
# #     st.session_state.stage = 0

# # def set_state(i):
# #     st.session_state.stage = i

# # if st.session_state.stage == 0:
# #     st.write("Click the button below to begin")
# #     st.button('Begin', on_click=set_state, args=[1])

# # if st.session_state.stage >= 1:
# #     # App title
# #     st.title("🧮 My Python Calculator")

# #     # Display a short welcome message
# #     st.write("Welcome to My Python Calculator! Choose an operation and enter two numbers to calculate.")


# # if st.session_state.stage >=2:
# #     first_number = st.text_input(
# #         "What is the first nummber?: ",
# #         on_change = set_state, args=[3]
# #         )

# #     if first_number is None:
# #         set_state(2)

# # if st.session_state.stage >=3:
# #     operations = ['+', '-', '*', '/']
# #     st.write("Available operations:"
# #     )

# #     for operation in operations:
# #         st.write(operation)
        
# # if st.session_state.stage >=4:
# #     operation = st.text_input(
# #         "Pick an operation:",
# #         on_change = set_state, args=[5]
# #         )

# #     if operation is None:
# #         set_state(4)


# # if st.session_state.stage >=5:
# #     second_number = st.text_input(
# #         "What is the second number: ",
# #         on_change = set_state, args=[6]
# #         )

# #     if second_number is None:
# #         set_state(5)


# # if operation == '+':
# #     answer = float(first_number) + float(second_number)
# # elif operation == '-':
# #     answer = float(first_number) - float(second_number)
# # elif operation == '*':
# #     answer = float(first_number) * float(second_number)
# # elif operation == '/':
# #     answer = float(first_number) / float(second_number)


# # if st.session_state.stage >=6:
# #     st.markdown(f"##### {first_number} {operation} {second_number} = {answer}")
# #     st.button("Start Over", on_click=set_state, args=[0])










# # import streamlit as st

# # # App title
# # st.title("🧮 My Python Calculator")

# # # Display a short welcome message
# # st.write("Welcome to My Python Calculator! Choose an operation and enter two numbers to calculate.")

# # # Define available operations
# # operations = ['+', '-', '*', '/']

# # # Input fields for the numbers
# # first_number = st.number_input("Enter the first number:", value=0.0, step=1.0)
# # operation = st.selectbox("Select an operation:", operations)
# # second_number = st.number_input("Enter the second number:", value=0.0, step=1.0)

# # # Calculate button
# # if st.button("Calculate"):
# #     if operation == '+':
# #         answer = first_number + second_number
# #     elif operation == '-':
# #         answer = first_number - second_number
# #     elif operation == '*':
# #         answer = first_number * second_number
# #     elif operation == '/':
# #         # Handle division by zero
# #         if second_number == 0:
# #             st.error("Error: Cannot divide by zero.")
# #         else:
# #             answer = first_number / second_number
# #     else:
# #         answer = None

# #     # Display result if valid
# #     if operation != '/' or second_number != 0:
# #         st.success(f"✅ Result: {first_number} {operation} {second_number} = {answer}")





# import streamlit as st

# if 'stage' not in st.session_state:
#     st.session_state.stage = 0

# def set_state(i):
#     st.session_state.stage = i

# if st.session_state.stage == 0:
#     st.write("Click the button below to begin")
#     st.button('Begin', on_click=set_state, args=[1])

# if st.session_state.stage >= 1:
#     # App title
#     st.title("🧮 My Python Calculator")

#     # Display a short welcome message
#     st.write("Welcome to My Python Calculator! Choose an operation and enter two numbers to calculate.")


# if st.session_state.stage >=2:
#     first_number = st.text_input(
#         "What is the first nummber?: ",
#         on_change = set_state, args=[3]
#         )

#     if first_number is None:
#         set_state(2)

# if st.session_state.stage >=3:
#     operations = ['+', '-', '*', '/']
#     st.write("Available operations:"
#     )
    
#     for operation in operations:
#         st.write(operation)
        
# if st.session_state.stage >=4:
#     operation = st.text_input(
#         "Pick an operation:",
#         on_change = set_state, args=[5]
#         )

#     if operation is None:
#         set_state(4)


# if st.session_state.stage >=5:
#     second_number = st.text_input(
#         "What is the second number: ",
#         on_change = set_state, args=[6]
#         )

#     if second_number is None:
#         set_state(5)


# if st.session_state.stage >=6:
#     answer = None
#     if operation == '+':
#         answer = float(first_number) + float(second_number)
#     elif operation == '-':
#         answer = float(first_number) - float(second_number)
#     elif operation == '*':
#         answer = float(first_number) * float(second_number)
#     elif operation == '/':
#         answer = float(first_number) / float(second_number)

#     st.markdown(f"##### {first_number} {operation} {second_number} = {answer}")
#     st.button("Start Over", on_click=set_state, args=[0])


import streamlit as st

# Stage-based Calculator (like the tip calculator)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin")
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    # App title
    st.title("🧮 Welcome to My Python Calculator")
    # Display a short welcome message
    name = st.text_input("What is your name?", on_change=set_state, args=[2])

#### Enter the first number, choose an operation, and then enter second number to calculate.

if st.session_state.stage >= 2:
    st.write(f"Hello {name.capitalize()}! Let's perform a calculation.")
    first_number = st.text_input(
        "What is the first number?:",
        on_change=set_state, args=[3]
    )
    if first_number is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write("Available operations: +, -, *, /")

   
    operation = st.text_input(
        "Pick an operation:",
        on_change=set_state, args=[4]
    )

    if operation is None:
        set_state(3)

if st.session_state.stage >= 4:
    second_number = st.text_input(
        "What is the second number?:",
        on_change=set_state, args=[5]
    )
    if second_number is None:
        set_state(4)

if st.session_state.stage >= 5:
    # first = st.session_state.get("first_number", "")
    # op = st.session_state.get("operation", "")
    # second = st.session_state.get("second_number", "")

    # # Validate inputs
    # try:
    #     a = float(first)
    #     b = float(second)
    #     if op == '+':
    #         answer = a + b
    #     elif op == '-':
    #         answer = a - b
    #     elif op == '*':
    #         answer = a * b
    #     elif op == '/':
    #         if b == 0:
    #             st.error("Error: Cannot divide by zero.")
    #             answer = None
    #         else:
    #             answer = a / b
    #     else:
    #         st.error("Please enter a valid operation: +, -, *, or /")
    #         answer = None

    #     if answer is not None:
    #         st.markdown(f"##### {a} {op} {b} = {answer}")
    # except ValueError:
    #     st.error("Please enter valid numeric values for the numbers.")

    first_number = float(first_number)
    second_number = float(second_number)
    if operation == '+':
        answer = first_number + second_number
    elif operation == '-':
        answer = first_number - second_number
    elif operation == '*':
        answer = first_number * second_number
    elif operation == '/':
        answer = first_number / second_number
    st.markdown(f"##### {first_number} {operation} {second_number} = {answer}")
    st.button("Start Over", on_click=set_state, args=[0])











