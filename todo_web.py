import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    # Define our inout
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local)
    functions.write_todos('todos.txt', todos)


st.title('My Title')

# st.subheader('My subhead er')
# st.write('This is simple text.')
# st.checkbox('Buy products')
# Add key to check box to define checked status of todos

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # If we select any todo
        todos.pop(index)
        functions.write_todos('todos.txt',todos)  # Save changes in our text document
        del st.session_state[todo]  # Delete also from session
        st.rerun()

# Key helps the define funtion find our input , in on_change we write call our function without brackets
st.text_input(label='', placeholder='Enter a new todo....', on_change=add_todo, key='new_todo')

# st.session_state
