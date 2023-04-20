import streamlit as st
import functions

todos, last_timestamp = functions.read_todo_file()


def add_todo():
    todo = st.session_state["text_input"]
    todos.append(todo)
    functions.write_todo_file(todos)
    st.session_state["text_input"] = ""


def main():
    st.title("ToDo app")
    st.subheader("ToDo list")

    st.write(f"Last change: {last_timestamp}")

    for i, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(i)
            functions.write_todo_file(todos)
            del st.session_state[todo]
            st.experimental_rerun()

    st.text_input(label="Text input", label_visibility="hidden",
                  placeholder="type in new item",
                  on_change=add_todo, key="text_input")


if __name__ == "__main__":
    main()
