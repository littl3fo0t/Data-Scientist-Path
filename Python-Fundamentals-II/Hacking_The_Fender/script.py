# Step 1: Import the csv module
import csv

# Step 2: Create an empty list
compromised_users = []

# Step 3: Open the csv file
with open("passwords.csv") as password_file:
    # Step 4: Use the csv reader for parsing
    password_csv = csv.DictReader(password_file)

    # Step 5: Loop through each row of the csv file
    for password_row in password_csv:
        # Step 6: Test out the code by pritning out the usernames
        #print(password_row["Username"])

        # Step 7: Append each username to the compromised_users list
        compromised_users.append(password_row["Username"])

# Step 8: Open a new file to write to
with open("compromised_users.txt", "w") as compromised_user_file:
    # Step 9: Loop through each compromised user
    for user in compromised_users:
        # Step 10: Write each compromised user to the txt file
        compromised_user_file.write(user)
        compromised_user_file.write("\n")

# Step 11: Import the json module
import json

# Step 12: Open a new json file
with open("boss_message.json", "w") as boss_message:
    # Step 13: Create a dictionary
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}

    # Step 14: Write out the above dict to the json file
    json.dump(boss_message_dict, boss_message)

# Step 15: Open a new csv file
with open("new_passwords.csv", "w") as new_passwords_obj:
    # Step 16: Create a multiline string
    slash_null_sig = """
            _  _     ___   __  ____             
        / )( \   / __) /  \(_  _)            
        ) \/ (  ( (_ \(  O ) )(              
        \____/   \___/ \__/ (__)             
        _  _   __    ___  __ _  ____  ____  
        / )( \ / _\  / __)(  / )(  __)(    \ 
        ) __ (/    \( (__  )  (  ) _)  ) D ( 
        \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
                ____  __     __   ____  _  _ 
        ___   / ___)(  )   / _\ / ___)/ )( 
        (___)  \___ \/ (_/\/    ___ \) __ (
            (____/\____/\_/\_/(____/\_)(_/
        __ _  _  _  __    __                
        (  ( \/ )( \(  )  (  )               
        /    /) \/ (/ (_/\/ (_/\             
        \_)__)\____/\____/\____/
        """
    
    # Step 17: Write the multiline string to the new csv file
    new_passwords_obj.write(slash_null_sig)