# Python Day 6: Exercises (Part 2) 🐍

These exercises cover the following Python concepts from Day 6:
- Truthy and Falsy Values
- Ternary Operators

## Exercise Difficulty Legend
- ⭐ - Basic
- ⭐⭐ - Straightforward 
- ⭐⭐⭐ - Moderate
- ⭐⭐⭐⭐ - Challenging
- ⭐⭐⭐⭐⭐ - Complex

## Truthy and Falsy Values ✅❌

<details>
<summary>Exercise 1: Value Evaluation (⭐)</summary>

### Task
For each of the following values, determine whether it is truthy or falsy.

```python
# Determine if each value is truthy or falsy
values = [
    0,                  # ?
    1,                  # ?
    -1,                 # ?
    "",                 # ?
    "Hello",            # ?
    [],                 # ?
    [0],                # ?
    {},                 # ?
    {"key": "value"},   # ?
    None,               # ?
    True,               # ?
    False,              # ?
    (),                 # ?
    (1,),               # ?
    set(),              # ?
    {1, 2}              # ?
]

def is_truthy(value):
    # Return True if the value is truthy, False if it's falsy
    pass
```

### Expected Output
```
0: Falsy
1: Truthy
-1: Truthy
"": Falsy
"Hello": Truthy
[]: Falsy
[0]: Truthy
{}: Falsy
{"key": "value"}: Truthy
None: Falsy
True: Truthy
False: Falsy
(): Falsy
(1,): Truthy
set(): Falsy
{1, 2}: Truthy
```

</details>

<details>
<summary>Exercise 2: Default Value Selection (⭐⭐)</summary>

### Task
Write a function that returns the first truthy value from a list, or a default value if none are truthy.

```python
def first_truthy(values, default="No truthy value found"):
    # Return the first truthy value in the list, or the default if none are truthy
    pass

# Test cases
print(first_truthy([0, "", [], None, "Hello", 42]))  # Should return "Hello"
print(first_truthy([0, "", [], None]))               # Should return "No truthy value found"
print(first_truthy([]))                              # Should return "No truthy value found"
```

### Expected Output
```
Hello
No truthy value found
No truthy value found
```

</details>

<details>
<summary>Exercise 3: Function Parameter Validation (⭐⭐⭐)</summary>

### Task
Create a function that validates its parameters using truthy/falsy checks and provides appropriate defaults.

```python
def process_order(customer_name, items, shipping_address, payment_method=None, coupon_code=None):
    """
    Process an order with parameter validation.
    
    Args:
        customer_name: Name of the customer (required)
        items: List of items in the order (required, must have at least one item)
        shipping_address: Address for shipping (required)
        payment_method: Method of payment (optional)
        coupon_code: Discount coupon code (optional)
    
    Returns:
        Dictionary containing the order details with validated parameters
    """
    # Validate required parameters
    # Use truthy/falsy evaluation and provide defaults for optional parameters
    # Return the processed order as a dictionary
    pass

# Test cases
valid_order = process_order("John Doe", ["Laptop", "Mouse"], "123 Main St", "Credit Card")
print(valid_order)

invalid_order = process_order("", [], "", None)
print(invalid_order)  # Should have appropriate defaults or error messages
```

### Expected Output
```
# Valid order:
{
    'customer_name': 'John Doe',
    'items': ['Laptop', 'Mouse'],
    'shipping_address': '123 Main St',
    'payment_method': 'Credit Card',
    'coupon_code': None,
    'status': 'Processed'
}

# Invalid order:
{
    'customer_name': 'Guest',
    'items': ['No items'],
    'shipping_address': 'Address required',
    'payment_method': 'Cash on Delivery',
    'coupon_code': None,
    'status': 'Invalid - Missing required information'
}
```

</details>

## Ternary Operators 🔄

<details>
<summary>Exercise 4: Simple Ternary Expressions (⭐⭐)</summary>

### Task
Rewrite the following if/else statements as ternary expressions.

```python
# 1. Age check
age = 20
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# 2. Score grading
score = 75
if score >= 70:
    result = "Pass"
else:
    result = "Fail"

# 3. Empty list check
my_list = [1, 2, 3]
if my_list:
    message = "List has elements"
else:
    message = "List is empty"

# Your ternary expressions here:
# status = ...
# result = ...
# message = ...
```

### Expected Output
```
status = "Adult"
result = "Pass"
message = "List has elements"
```

</details>

<details>
<summary>Exercise 5: Nested Ternary Operators (⭐⭐⭐)</summary>

### Task
Rewrite the following nested if/else statements as nested ternary operators.

```python
# 1. Grade calculation
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# 2. Ticket pricing
age = 25
is_student = False
if age < 12:
    price = "Child: $5"
elif age >= 65:
    price = "Senior: $8"
else:
    if is_student:
        price = "Student: $8"
    else:
        price = "Adult: $12"

# Your nested ternary expressions here:
# grade = ...
# price = ...
```

### Expected Output
```
grade = "B"
price = "Adult: $12"
```

</details>

<details>
<summary>Exercise 6: Practical Ternary Applications (⭐⭐⭐)</summary>

### Task
Create functions that use ternary operators for practical applications.

```python
def format_username(username):
    """
    Format a username: if valid (non-empty), return as is, otherwise return "guest"
    """
    # Your code here using ternary operator
    pass

def pluralize(word, count):
    """
    Return word as singular or plural based on count:
    e.g., "1 apple" or "2 apples"
    """
    # Your code here using ternary operator
    pass

def get_access_level(user):
    """
    Return access level based on user dictionary:
    - "admin" if user has admin status
    - "moderator" if user has moderator role but not admin
    - "user" otherwise
    """
    # Your code here using nested ternary operators
    pass

# Test cases
print(format_username("johndoe"))  # Should return "johndoe"
print(format_username(""))         # Should return "guest"

print(pluralize("apple", 1))       # Should return "1 apple"
print(pluralize("apple", 2))       # Should return "2 apples"

admin_user = {"name": "Admin", "is_admin": True, "is_moderator": True}
mod_user = {"name": "Moderator", "is_admin": False, "is_moderator": True}
regular_user = {"name": "User", "is_admin": False, "is_moderator": False}

print(get_access_level(admin_user))     # Should return "admin"
print(get_access_level(mod_user))       # Should return "moderator"
print(get_access_level(regular_user))   # Should return "user"
```

### Expected Output
```
johndoe
guest
1 apple
2 apples
admin
moderator
user
```

</details>

<details>
<summary>Exercise 7: Combining Truthy/Falsy with Ternary (⭐⭐⭐⭐)</summary>

### Task
Create functions that combine truthy/falsy evaluation with ternary operators for concise code.

```python
def safe_divide(a, b):
    """
    Safely divide a by b, returning "Cannot divide by zero" if b is 0
    """
    # Your code here using ternary with truthy/falsy check
    pass

def get_display_name(user_data):
    """
    Return a display name from user_data dictionary in following priority:
    1. full_name if available
    2. username if available
    3. email if available
    4. "Guest" if none available
    """
    # Your code here using nested ternary with truthy/falsy checks
    pass

def validate_form_field(field_value, field_name):
    """
    Return success or error message based on whether field_value is truthy
    """
    # Your code here
    pass

# Test cases
print(safe_divide(10, 2))   # Should return 5
print(safe_divide(10, 0))   # Should return "Cannot divide by zero"

user1 = {"full_name": "John Smith", "username": "jsmith", "email": "john@example.com"}
user2 = {"username": "jdoe", "email": "jane@example.com"}
user3 = {"email": "anonymous@example.com"}
user4 = {}

print(get_display_name(user1))  # Should return "John Smith"
print(get_display_name(user2))  # Should return "jdoe"
print(get_display_name(user3))  # Should return "anonymous@example.com"
print(get_display_name(user4))  # Should return "Guest"

print(validate_form_field("John", "name"))       # Success
print(validate_form_field("", "email"))          # Error
```

### Expected Output
```
5
Cannot divide by zero
John Smith
jdoe
anonymous@example.com
Guest
Success: name is valid
Error: email cannot be empty
```

</details>

## Bonus Challenge 🏆

<details>
<summary>Exercise 8: Form Validator (⭐⭐⭐⭐⭐)</summary>

### Task
Create a comprehensive form validation system that uses truthy/falsy checks and ternary operators to validate form fields and generate appropriate error messages.

```python
def validate_form(form_data):
    """
    Validate a form with the following rules:
    - username: required, at least 3 characters
    - email: required, must contain @
    - password: required, at least 8 characters
    - confirm_password: must match password
    - age: optional, must be a number between 18 and 120 if provided
    
    Return a dictionary with validation results and error messages
    """
    # Your implementation here
    pass

# Test cases
valid_form = {
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepass",
    "confirm_password": "securepass",
    "age": 25
}

invalid_form = {
    "username": "",
    "email": "invalid-email",
    "password": "short",
    "confirm_password": "different",
    "age": "not-a-number"
}

print(validate_form(valid_form))
print(validate_form(invalid_form))
```

### Expected Output
```
{
    "valid": True,
    "errors": {}
}

{
    "valid": False,
    "errors": {
        "username": "Username is required",
        "email": "Email must contain @",
        "password": "Password must be at least 8 characters",
        "confirm_password": "Passwords do not match",
        "age": "Age must be a number between 18 and 120"
    }
}
```

</details>

---

Good luck with these exercises! Remember to apply the concepts you've learned about truthy/falsy values and ternary operators. 🚀
