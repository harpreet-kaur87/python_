import streamlit as st


def calculator(x,y,user_input):


    if user_input == 'Addition':
        return x + y 
    elif user_input == 'Subtraction':
        return x - y
    elif user_input == 'Multiplication':
        return x * y
    elif user_input == 'Division':
        return x//y
    else:
        return f'Please enter valid input'
    
def main():
    st.title('Simple Calculator')

    x = int(st.number_input('Enter the first number - '))
    y = int(st.number_input('Enter the second number - '))

    user_input = st.selectbox('Select the operation:', ['Addition','Subtraction', 'Multiplication', 'Division'])

    if st.button('Calculate'):
        result = calculator(x,y,user_input)
        st.write(f'Result:{result}')

if __name__ == "__main__":
    main()