# Week-04-Day-20-AM

### Part A — Concept Application (40%)

#### 1. Using only loops (no built-in functions), implement:
*   **Find the maximum and minimum** element in a list
*   **Count frequency** of each element using a dictionary <br>
[Solution](min_max_freq.py)

#### 2. Using a while loop, implement:
*   **Reverse a number** (e.g., 123 → 321)
*   Check whether a number is a **palindrome** <br>
[Solution](rev_palindrome.py)

#### 3. Work with tuples and dictionaries:
*   **Convert a list of tuples** `[(key, value)]` into a dictionary without using built-in conversion
*   Find the **key with the highest value** in a dictionary using loops only <br>
[Solution](tuple_to_dict.py)

#### 4. Implement a function using `*args`:
*   Accept multiple numbers and return their **sum and average** (without using `sum()`) <br>
[Solution](sum_avg_usng_args.py)

#### 5. Implement a function using `**kwargs`:
*   Accept **student names and marks**
*   Return the student with the **highest marks** <br>
[Solution](highest_marks.py)

---

### Part B — Stretch Problem (30%)

#### Create a custom class `Vector`:
*   **Initialize** with a tuple of numbers
*   **Implement the following dunder methods:**
    *   `__add__` → vector addition
    *   `__sub__` → vector subtraction
    *   `__mul__` → scalar multiplication
    *   `__repr__` → readable output
*   **Test your class** with multiple examples <br>
[Solution](custom_vector_class.py)


---

### Part C — Interview Ready (20%)

#### Q1 — What is the difference between `*args` and `**kwargs`?
*   When would you use each?

**`*args`**: Passes a variable number of **non-keyword (positional)** arguments as a **tuple**. Use it when you don't know how many inputs the user will provide. <br>
**`**kwargs`**: Passes variable **keyword-named** arguments as a **dictionary**. Use it for named parameters or configurations.


#### Q2 (Coding) — Create a class `Student`:
*   **Attributes:** `name`, `marks`
*   **Methods:**
    *   **Calculate grade** (A/B/C)
    *   **Display student details** using `__str__`

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80: return "A"
        elif self.marks >= 60: return "B"
        else: return "C"

    def __str__(self):
        return f"Student: {self.name} | Grade: {self.get_grade()}"
```


#### Q3 — What are **dunder methods** in Python?
*   Why are they important?
*   Give 3 examples.

**Dunder methods** (short for "double underscore") are special, predefined methods in Python that start and end with two underscores, such as `__init__` or `__str__`. Also known as **magic methods**, they are not meant to be called directly by you; instead, the Python interpreter calls them automatically in response to specific actions or built-in functions.

#### Why They Are Important
Dunder methods are crucial because they allow your custom objects to behave like native Python types. They enable:

*   **Operator Overloading:** You can define what happens when you use operators like `+`, `-`, or `==` on your own classes.
*   **Seamless Integration:** Your objects can work naturally with built-in functions like `len()`, `print()`, or `iter()`.
*   **Pythonic Code:** They help you write code that is more intuitive and readable by following standard Python conventions.

#### Common Examples

1.  **`__init__(self, ...)` (Initialization):**
    This is the most common dunder method. It acts as a constructor, automatically setting up an object's initial state when a new instance of a class is created.

2.  **`__str__(self)` (String Representation):**
    This method defines what is shown when you use `print()` or `str()` on an object. It is intended to return a "user-friendly," human-readable string.

3.  **`__len__(self)` (Length):**
    When you call the built-in `len()` function on an object, Python looks for this method. Implementing it allows your custom collection or object to report its size just like a list or string.

---

### Part D — AI-Augmented Task (10%)

#### 1. Prompt AI:
> "Explain Python dunder methods with examples for beginners and include a custom class implementation."

#### 2. Document prompt and output:
*   [Insert the AI-generated response here or link to a separate file]

[AI_Output](AI_output.md) for the above given prompt.

#### 3. Evaluate:
*   **Are the examples correct?**
*   **Is the class implementation working?**

Yes, the examples are correct, and the class implementation is fully functional. The code accurately demonstrates how Python uses dunder methods to bridge the gap between custom objects and built-in language features.

#### Why the Implementation Works
*   **Initialization (`__init__`)**: Properly sets up the `title` and `pages` attributes when you create a new `Book` instance.
*   **String Representation (`__str__`)**: Correctly returns a formatted string. When you call `print(book1)`, Python implicitly calls `book1.__str__()` to get a human-readable output instead of a memory address.
*   **Operator Overloading (`__add__`)**: Successfully redefines the `+` operator. Instead of throwing a `TypeError`, it extracts the `pages` value from both objects and returns their sum.

#### Verified Results
When the code is executed, it produces the following expected outputs:
*   `print(book1)`: `'The Hobbit' (310 pages)`
*   `book1 + book2`: `460` (the sum of 310 and 150)












