secret_message = "   Programming in Python is not only powerful but also fun!   "

# Task 1
# Expected Output
# "PYTHON-POWERFUL"

# Dot chaining
clean_upper_msg = secret_message.strip().upper()
print(clean_upper_msg[15:21].upper() + "-" + clean_upper_msg[34:42].upper())


# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

msg = flipped_message[-1:-7:-1] + " 🗡️  " + flipped_message[-13:-21:-1] + " 🌸"
print(msg.lower())

# Task 1.3

# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️"

# Output
# SECRET_CODE✌️

key_pos = message.find("🔑")
print(message[key_pos + 1 :].upper())


# Solutions
# # secret_message = "   Programming in Python is not only powerful but also fun!   "
# # clean_secret_message = secret_message.strip()
# # clean_upper_msg = clean_secret_message.upper()
# # print(clean_upper_msg)
# # print(clean_upper_msg[15:21] + "-" + clean_upper_msg[34:42])


# secret_message = "   Programming in Python is not only powerful but also fun!   "
# # clean_secret_message = secret_message.strip()
# # clean_upper_msg = clean_secret_message.upper()

# # Dot Chaining
# clean_upper_msg = secret_message.strip().upper()
# print(clean_upper_msg)
# print(clean_upper_msg[15:21] + "-" + clean_upper_msg[34:42])


# # Task 1.1
# # Expected Output
# # "PYTHON-POWERFUL"


# # 1. Solve
# # 2. Make it better


# # Task 1.2
# flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# # Expected Output
# # "python 🗡️ powerful 🌸"

# flipped_message_reverse = flipped_message[::-1].lower()
# print(f"{flipped_message_reverse[0:6]} 🗡️ {flipped_message_reverse[12:20]} 🌸")


# # Task 1.3

# # After the 🔑
# message = "    🚨🔍📱🔑secret_code✌️"
# # Clue: find

# # Output
# # SECRET_CODE✌️
