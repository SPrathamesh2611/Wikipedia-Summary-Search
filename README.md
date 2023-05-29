# Wikipedia-Summary-Search
The code snippet is utilizing the `wikipedia` library. To install the `wikipedia` library on your system, you can use the following command in the terminal:

```
pip install wikipedia
```

This command uses `pip`, the package installer for Python, to download and install the `wikipedia` library from the Python Package Index (PyPI). Make sure you have a stable internet connection while running this command. Once the installation is complete, you'll be able to import and use the `wikipedia` module in your Python code.

# Description
The provided code showcases a basic application built using the Tkinter library in Python, which allows users to search for information on Wikipedia and display the summary of the searched query. Here's an introduction to the code:

The code begins by importing two modules: `Tk` from Tkinter and `wikipedia`.

- `Tk` is used to create the main application window and manage the graphical user interface (GUI).
- `wikipedia` is a Python library that provides functionalities for interacting with the Wikipedia API and fetching information.

Next, a function named `on_press` is defined. This function is triggered when the user clicks the "search" button. It retrieves the user's query from the `get_q` Entry widget and uses the `wikipedia.summary` function to fetch the summary of the queried topic from Wikipedia. The retrieved summary is then inserted into the Text widget named `text` using `text.insert(INSERT, ...)`.

The `root` variable is initialized as an instance of the Tk class, representing the main application window. It is given the title "WIKIEPEDI APP".

Several GUI elements are created within the root window:
- A Label widget with the text "Question".
- An Entry widget named `get_q` where the user can input their search query.
- A Button widget named `submit` with the text "search" that calls the `on_press` function when clicked.
- A Text widget named `text` where the summary of the queried topic will be displayed.

Finally, the main event loop is started using `root.mainloop()`, which ensures that the application remains open and responsive to user interactions.

The line `print(result)` appears to be an error, as the `result` variable is not defined in the provided code snippet.

Overall, this code demonstrates a simple Tkinter-based application that allows users to search and retrieve summaries of topics from Wikipedia using the `wikipedia` library.
