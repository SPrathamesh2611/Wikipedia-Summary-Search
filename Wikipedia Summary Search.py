from tkinter import *
import wikipedia

def on_press():
    # Retrieve the user's query from the Entry widget
    query = get_q.get()
    
    # Fetch the summary of the queried topic from Wikipedia
    summary = wikipedia.summary(query)
    
    # Insert the retrieved summary into the Text widget
    text.insert(INSERT, summary)


# Create the main application window
root = Tk()
root.title("WIKIEPEDI APP")

# Create a Label widget for the question
question = Label(root, text='Question')
question.pack()

# Create an Entry widget for user input
get_q = Entry(root, bd=5)
get_q.pack()

# Create a Button widget for searching
submit = Button(root, text='Search', command=on_press)
submit.pack()

# Create a Text widget for displaying the retrieved summary
text = Text(root)
text.pack()

# Start the main event loop
root.mainloop()

# Note: The line below seems to be an error as 'result' is not defined in the provided code
print(result)
