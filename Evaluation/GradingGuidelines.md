# ACS 1120: Intro to Data Structures & Algorithms

## Grading Process

- Open project & code rubric in a new window for reference while reviewing scores/code
- Open the assignment in Gradescope
- Add project feedback in text area or in individual comments on each line of code
- If something is super broken, use your discretion if you want to Slack a student to fix it
- Aim to spend 8-10 minutes on average per project
- Set a timer to help you finish quickly

## How to Give Valuable Code Feedback

- Add comments as you see things, just quick notes, don’t bother with complete sentences
   - Not OK: Add more comments
   - OK: More comments in random_word function
   - Great: Add comments to complex code on lines 42-48 in random_word function
- Give both positive/supportive feedback so they know what they’re already doing well as well as constructive criticism so they know what and how they can improve
   - Supportive: The effort you put into the histograms code really shows!
   - Constructive: Your histogram_tuples function could be simplified with a for loop instead of a while loop
   - Supportive: Clean code and great variable names, makes it easy to understand
   - Constructive: Need to run random_word function many times in a loop and count up the results to truly test the relative probabilities of your sampler, not just twice
- Quickly scan your comments before submitting to ensure feedback is balanced

## Reusable Code Feedback Comments

Suggestions to Guide Tweet Generator feedback listed below.

### Random Dictionary Words

   - Did they use command-line arguments to pick how many words to select?
   - If the code selects 10 words, does it open the dictionary file 10 times or once?

### Histograms (Dictionaries, List of Lists, Tuples, Counts)

   - How many different ways did they attempt to build histograms? (dict, lists, tuples)
   - Is the code fairly simple, or too complex and could be simplified?
   - Note: They are not allowed to use the built-in collections.Counter class

### Sample Words by Frequency

   - Do they use a histogram as a function argument? (this is required)
   - Do they reconstruct the original list of word tokens? (this is not scalable)
   - Note: They are not allowed to use the built-in random.choices function

### Test Relative Probabilities

_Rubric row was replaced by unit tests for the sample method_

   - Did they run sampling function many times in a loop and count up the results?
   - Did they run on known text (one fish …) and print out the results for examination?
   - Are the results reasonable? (~50% fish, ~12.5% other words – NOT 20% each)
   - Run python3 dictogram.py and pytest dictogram_test.py to test this and print out a table of results with green/yellow/red text to show if results are correct
   - Run python3 listogram.py and pytest listogram_test.py in a similar way

### Create Flask Web App and Deploy to Heroku

   - Did they create a Flask server with at least one route attached to a function?
   - Did they deploy it to Heroku? (need requirements.txt file and live Heroku URL)
   - If they didn’t deploy to Heroku, can you at least run the Flask web app locally?


### Linked List Implementation

- First run the unit tests to check if all 16 pass: pytest linkedlist_test.py
- Check if their append and prepend methods run in O(1) time. If not, write some code feedback on how they can simplify their implementation to be more efficient. These will likely be very similar from one student to another since they’re relatively simple.
- Focus on the find and delete methods since there should be a bit more variation from one student to another. These should both iterate over all nodes (ideally just once) and run in O(N) time.
- Check that they annotated time complexity in docstrings above the main methods (append, prepend, find and delete) using the “TODO: Running time: O(???) …” placeholder text. Write feedback comments if they skipped this or analyzed it incorrectly.
- Also check the length method, which will iterate over all nodes and count how many were visited. However, there is an “alternative approach to calculate length” stretch challenge, which involves adding a new .size or .count integer property to keep track of the length and simply return the number when asked.
- See the list of linked list stretch challenges here when checking how many they solved.


### Hash Table Implementation

- First run the unit tests to check if all 9 pass: pytest hashtable_test.py
- The contains, get, set, and delete methods should call self._bucket_index(key) to use the key’s hash code to get the index of which bucket to look in and NOT loop over all the buckets. If not, write some code feedback on how they can simplify their method implementations and make them more efficient, which is the whole point of a hash table. An example of another inefficient implementation of the contains method is checking if key in self.keys() because calling .keys() produces a list (array) of all keys in the hash table then linear searches the list, and both operations have time complexity O(N).
- The beginning of each of these methods should be the same so they are likely all similar. However, the later parts should be different, especially in the set and delete methods.
- Check that they annotated time complexity in docstrings above the main methods using the “TODO: Running time: O(???) …” placeholder text. Write feedback comments if they skipped this or analyzed it incorrectly. If they used the key’s hash code to get the bucket index for the contains, get, set, and delete methods, then the time complexity should be O(L), where L is the load factor (average length of each linked list bucket). However, if they did NOT use the key’s hash code, but instead looped over all the buckets, then the time complexity should be O(B*L) = O(N). [For a quick refresher, view the hash table time complexity worksheet and select the text in the second chart to see my solutions.]
- Also check the length method, which will iterate over all the buckets and call the length method on each bucket to calculate the length of the linked list. However, note that there is an “alternative approach to calculate length” stretch challenge, which involves adding a new .size or .count integer property to keep track of the length.
- See the list of hash table stretch challenges here when checking how many they solved.


### Late Submissions

- If students submit their work after the deadline, please do a quick check of their commit history (which is easy to do when viewing the linkedlist.py or hashtable.py file on GitHub by clicking the “History” button at the top, next to “Raw” and “Blame”).
- As long as they made solid progress before the deadline with mostly on-time commits, I’ll automatically accept the late submission. It’s fine if they changed a few things in later commits, like fixing a few bugs or adding/correcting their time complexity annotations.
- Add a brief note in the “Notes from TAs or Instructor” column to note if all/most commits were before the deadline or if most meaningful work was done well after the deadline.
