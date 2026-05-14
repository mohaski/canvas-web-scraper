# Check for Understanding: File Handling and Logging

# Check for Understanding: File Handling and Logging

## ![](https://moringa.instructure.com/courses/1391/files/620140/preview?) Check for Understanding: File Handling and Logging

Icon Progress Bar (browser only)

Now is your opportunity to see how much you can recall from the topic! Take a moment to answer the questions below. These are not graded, but they will allow you to check how much you are putting together the content in this lesson and review before moving to a new topic. 

### Quick Check: Python Application

You are a junior developer tasked with maintaining a Python application that reads data from a file and logs various events during its execution. The application needs to handle situations where the file may not exist, the file might be empty, and it must record these events in a log file for future analysis.

**Given the scenario, which of the following statements about file handling and logging is correct?**

If the data file does not exist, the program will log an error message and terminate abruptly.
:   This is incorrect. If the file does not exist, the program should handle the error gracefully by logging the issue and continuing to run without crashing.

The log file will only contain entries if the data file is read and processed successfully.
:   This is incorrect. The log file will contain entries for various events, including errors and warnings, not just successful file reads and data processing.

If the data file is empty, the program will log a warning indicating that there is no data to process and will not proceed with further processing.
:   **Correct:**  If the data file is empty, the application will recognize that there is no data to work with, log a warning, and halt further processing.

The log file will not record any messages unless the logging level is set to the most detailed level (DEBUG).
:   This is incorrect. Even with the logging level set to INFO or higher, relevant events like errors, warnings, and information messages will still be recorded in the log file.

[Check Answer](#)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239295

Scraped At: 2026-05-14T15:58:44.867411
