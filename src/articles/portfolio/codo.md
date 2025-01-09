title: Codo
file: codo
date: 01.02.2024
---

# What is it?

Codo is a TUI(terminal-user-interface) application for Linux operating system written in C programming language,
which uses <a href="https://pubs.opengroup.org/onlinepubs/7908799/xcurses/curses.h.html" target="_blank">ncurses</a> for UI and <a href="https://sqlite.org/docs.html" target="_blank">SQlite</a> for database management. 

![Example image of Codo running]({{ url_for('static', filename='codo_example.png') }})
*Example image of Codo running*

<br>

# State of the application

As of the time of writing this Codo users are able to create, edit, and delete their to-do lists, the same goes for tasks. Tasks can be marked as done, when
all of the tasks in the same to-do list are done, the to-do list is also marked as done. I'm currently working on a subtask feature, which is about 90% done.

![Creating new to-do list]({{ url_for('static', filename='create_list.png') }})
*Creating new to-do list*

<br>

# Future

I'm planning to add some new functionalities that would enhance the use of application in various ways. Details windows would enable users to inspect their tasks and to-do lists to see more information about them, e.g. number of tasks in a list and the list's description, the same goes for tasks. Another addition would be keymaps, which could be used to smoothly operate in the Codo app in a Vim-like fashion, those keymaps of course could be changed via configuration file. The next thing that could be changed with the use of those config files would be the color theme of the application and default icons for various elements of the UI, e.g. tick icon, which appears when a task or list is done. Last but not least the search option to easily and efficiently find tasks by their name or description, is especially useful when the list grows to tens or hundreds of tasks.

<br>

## Here's a list of completed features and those planned for the future:
- [X] Task operations
    - [X] Add
    - [X] Delete
    - [X] Edit
    - [X] Change status
- [X] List operations
    - [X] Add
    - [X] Delete
    - [X] Edit
    - [X] Change status
- [ ] Subtasks (in-progress)
- [ ] Details window
- [ ] Color themes
- [ ] Keymaps
- [ ] Config files
- [ ] Search
- [ ] Scalable interface

<br>

# I'm really proud of:
- Custom array data structure, which can hold any type
- Deeper understanding and knowledge of C programming language

# Links:
- <a href="https://github.com/Korbielowski/codo/tree/main" target="_blank">Source code</a>
- <a href="https://tldp.org/HOWTO/NCURSES-Programming-HOWTO/index.html" target="_blank">NCURSES Programming HOWTO</a>