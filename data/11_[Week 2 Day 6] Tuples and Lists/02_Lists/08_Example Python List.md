# Example: Python List

# Example: Python List

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Example: Python List

Icon Progress Bar (browser only)

2 min read

Lists provide a flexible way to store and manipulate data in Python. Unlike tuples (covered in the previous lesson), lists are mutable, allowing you to modify their contents. This mutability makes them suitable for situations where the collection of elements needs to be dynamic and adaptable. Lists maintain the order of elements you insert, and you can access elements by their position (index).

Imagine you're managing a task list for a project. You might start with a few tasks, but as the project progresses, new tasks may arise, and some might be completed and removed. A list is perfect for this scenario as it allows you to add, remove, and modify tasks throughout the project.

This code example below defines a task list and demonstrates how to add and remove items from the list.

```
# Create a task list  
task_list = ["Write code", "Design UI", "Test functionality"]  
  
# Add a new task  
task_list.append("Fix bugs")  # Now task_list is ["Write code", "Design UI", "Test functionality", "Fix bugs"]  
  
# Mark a task as complete (remove from list)  
task_list.remove("Write code")  # Now task_list is ["Design UI", "Test functionality", "Fix bugs"]
```

1. **Create a task list:** The code starts by creating a list named task\_list and assigning it three tasks: "Write code", "Design UI", and "Test functionality".
2. **Add a new task:** The append method is used to add a new task, "Fix bugs", to the end of the task\_list.
3. **Mark a task as complete:** The remove method is used to remove the task "Write code" from the task\_list, marking it as complete.
4. The code concludes by printing the updated task list, which now contains "Design UI", "Test functionality", and "Fix bugs".

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239242

Scraped At: 2026-05-14T15:54:45.335447
