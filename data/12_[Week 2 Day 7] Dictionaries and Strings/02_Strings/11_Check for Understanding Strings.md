# Check for Understanding: Strings

# Check for Understanding: Strings

## ![](https://moringa.instructure.com/courses/1391/files/620140/preview?) Check for Understanding: Strings

Icon Progress Bar (browser only)

Now is your opportunity to see how much you can recall from the topic! Take a moment to answer the questions below. These are not graded, but they will allow you to check how much you are putting together the content in this lesson and review before moving to a new topic. 

### Quick Check: Strings Scenario

As a junior developer, you are building a simple application to display personalized messages to users based on their input. You want to create a greeting message by combining the user's first and last names into a full name and then adding a greeting.

You write the following Python code:

```
# User's first and last name  
first_name = "John"  
last_name = "Doe"  
  
# Creating a full name  
full_name = first_name + " " + last_name  
  
# Generating a greeting message  
greeting = "Hello, " + full_name + "!"  
  
# Extracting the first letter of the first name  
initial = first_name[0]
```

**After executing the code above, which of the following statements is correct about the variables `full_name`, `greeting`, and `initial`?**

The variable `full_name` will store the string "John Doe", and `greeting` will store the string "Hello, John Doe!"; `initial` will store the string "J".
:   **Correct:** The `full_name` is created by concatenating `first_name`, a space `" "`, and `last_name`, resulting in `"John Doe"`. The `greeting` combines `"Hello, "`, the `full_name`, and `"!"`, forming `"Hello, John Doe!"`. The `initial` is correctly extracted as the first letter of `first_name`, which is `"J"`.

The variable `full_name` will store the string "JohnDoe" without any spaces, `greeting` will store the string "Hello, JohnDoe!", and `initial` will store the string "J".
:   **Incorrect**, because a space is included between `first_name` and `last_name`, so `full_name` will be `"John Doe"`, not `"JohnDoe"`.

The variable `full_name` will store the string "John Doe", `greeting` will store the string "Hello, John Doe!", but `initial` will store the entire first name "John".
:   **Incorrect**, because `initial` should store only the first letter of `first_name`, not the entire name.

The variable `full_name` will store the string "John Doe", and `greeting` will store the string "Hello, John Doe!"; however, trying to extract the initial using `initial = first_name[0]` will cause an error because strings are immutable.
:   This is incorrect because while strings are immutable, you can still access individual characters by indexing, so extracting the initial with `first_name[0]` will not cause an error.

Check Answer

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239283

Scraped At: 2026-05-14T15:58:01.490551
