# !/usr/bin/env python3

import argparse
import requests
import json
import sys

# Help




# The parser function is used to parse the command line arguments:
# Reason ~ The reason why I implemented a parser function is because I wanted to make the script more user friendly
# to users of the application via the cli (command-line interface)
# For future use, a new argument can be added within the parser that will execute the neccessary commands within the Artificatory class.
def parser():
    parser = argparse.ArgumentParser(description="JFrog Production Engineering Academy - Jordan Tingling Take-Home Assignment.")
    """
    There are many different ways to parse the command line arguments, however, for this assignment the eight (8) API's to be implemented are:
    1. System Ping
    2. System Version
    3. Create User
    4. Delete User
    5. Get Storage Info
    6. Create Reposititory
    7. Update Repository
    8. List Repositories

    The following are the arguments that are required to be passed in:
    """
    parser.add_argument("-p", "--system_ping", action="store_true", help="Return the ping requested from the system", required=True) # System Ping
    parser.add_argument("-v", "--system_version", action="store_true", help="Return the version of the system", required=True) # System Version
    parser.add_argument("-cu", "--create-user", action="store_true", help="Create a new user", required=True) # Create User
    parser.add_argument("-du", "--delete-user", action="store_true", help="Delete a user", required=True) # Delete User
    parser.add_argument("-si", "--storage-info", action="store_true", help="Return the storage information of the systen", required=True) # Storage Info
    parser.add_argument("-cr", "--create-repository", action="store_true", help="Create a new repository", required=True) # Create Repository
    parser.add_argument("-ur", "--update-repository", action="store_true", help="Update a repository", required=True) # Update Repository
    parser.add_argument("-lr", "--list-repositories", action="store_true", help="List all repositories", required=True) # List Repositories
    arg = parser.parse_args()
    return arg

# The Artifactory class is used to do pretty much all of the main bulk of the work, creating and initializing the requests, sending the requests, and handling the responses.
# The Artifactory class is also used to handle the creation of the user, repository, and other API's.
# The Artifactory class is also used to handle the deletion of the user, repository, and other API's.
# The Artifactory class is also used to handle the storage information of the system.
# The Artifactory class is also used to handle the list of repositories.
# The Artifactory class is also used to handle the update of the repository.
# The Artifactory class is also used to handle the system version.
# The Artifactory class is also used to handle the system ping.
# The Artifactory class is also used to handle the creation of the repository.
# The Artifactory class is also used to handle the update of the repository.

# My reason behind creating a class is because I wanted to make the script more user friendly and also to make it more flexible and easily updatable / adjustable.
# Have all my functions containing the functionality of the API's be in the Artifactory class is beneficial to me as I can easily change the functionality easily and quickly of the API for that specified command.

class Artifactory:
    # The __init__ function is used to initialize the Artifactory class.
    def __init__(self):
        # The following are the variables that are used to initialize the Artifactory class.
        self.username, self.artifactory_url, self.token = self.user_authentication()
        self.arg = parser()

    # Recieve the username and password from the user
    def user_authentication(self):
        # I used a dictonary to store the username and password and header fields as well.
        # This is because it is more robust and modular to use a dictionary in this case as the information is stored in key-value pairs and can be changed easily 
        # depending on the user's needs or need's of the application. 
        user_dict = {}
        print("Welcome to My JFrog Artifactory API, please enter the given username and password.") # Welcome message
        user_dict["username"] = input("Username: ") # Username prompt ~ jordantingling6@gmail.com
        user_dict["password"] = input("Password: ") # Password ~ 
        headers_dict = {"Content-Type": "application/x-www-form-urlencoded"} # Header fields

        artifactory_url = f"https://{user_dict['username']}.jfrog.io/artifactory" # Artifactory URL
        token_api = f"api/security/token" # Token API
        # The implementation of the API's post request
        r = requests.post(artifactory_url + token_api, data=user_dict, headers=headers_dict, auth = (user_dict["username"], user_dict["password"])) # Post request
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            print("Congrats! The Authentication was successful.") # Success message
            return user_dict["username"], artifactory_url, r.json()["token"] # Return the username, artifactory url, and token
        else:
            print("Unfortunately, The Authentication was unsuccessful." + r.content.decode("utf-8")) # Error message
            sys.exit() # Exit the script

    # Below is my implementation of passing the arguments to the necessary functions. I call it my "switch" because It asks like a swicth, mixing and matching etc.
    def switch(self):
        if self.arg.system_ping: # If the user wants to use the system ping, the following code will be executed.
            self.system_ping()
        elif self.arg.system_version: # If the user wants to use the system version, the following code will be executed.
            self.system_version()
        elif self.arg.create_user: # If the user wants to use the create user, the following code will be executed.
            self.create_user()
        elif self.arg.delete_user: # If the user wants to use the delete user, the following code will be executed.
            self.delete_user()
        elif self.arg.storage_info: # If the user wants to use the storage information, the following code will be executed.
            self.storage_info()
        elif self.arg.create_repository: # If the user wants to use the create repository, the following code will be executed.
            self.create_repository()
        elif self.arg.update_repository: # If the user wants to use the update repository, the following code will be executed.
            self.update_repository()
        elif self.arg.list_repositories: # If the user wants to use the list repositories, the following code will be executed.
            self.list_repositories()
        else:
            print("Please enter a valid argument.") # Error message
    # A simple conditional statement to determine what the user wants to do and execute the necessary function.

    # The following are the functions that are used to create the user, repository, and other API's.
    def system_ping(self):
        # This function will request the Ping from the instance.
        r = requests.get(self.artifactory_url + "api/system/ping", auth = (self.username, self.token)) # Get request
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            print("The ping was successful.")
            print("Ping status: " + r.content.decode("utf-8")) # Print the ping status
        else:
            print("The ping was unsuccessful.")
        
    def system_version(self):
        # This function will request the system's current running version from the instance.
        r = requests.get(self.artifactory_url + "api/system/version", auth = (self.username, self.token))
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            print("System version: " + r.content.decode("utf-8"))
        else:
            print("The system version failed to be retrieved.")

    def create_user(self):
        # This function will create a new user in the Jfrog artifactory.
        create_user_dict = {}
        create_user_dict["username"] = input("Username: ") # Username prompt
        create_user_dict["password"] = input("Password: ") # Password prompt
        create_user_dict["admin"] = False # Admin status
        create_user_dict["email"] = input("Email: ") # Email prompt
        headers = {"Content-Type": "application/json"} # Header fields
        # The implementation of the API's put request on creating a new user
        r = requests.put(self.artifactory_url + "api/security/users/" + create_user_dict["username"], data=json.dumps(create_user_dict).encode('utf-8'), headers=headers, auth = (self.username, self.token))  # Put request
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            print("The user was successfully created.")
        else:
            print("The user was not created." + r.content.decode("utf-8")) # Error message

    # The Delete user function is used to delete a user from the Jfrog artifactory, it require way less arguments than the create user function and 
    # the same goes for the "create repository" function and "update repository" function as well.

    def delete_user(self):
        # This function will delete a user from the Jfrog artifactory.
        user_name = input("Username: ") # Username prompt
        # The implementation of the API's delete request on deleting a user
        r = requests.delete(self.artifactory_url + "api/security/users/" + user_name, auth = (self.username, self.token)) # Delete request
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            print("The user was successfully deleted.")
        else:
            print("The user was not deleted." + r.content.decode("utf-8"))


    def storage_info(self):
        # This function will request the storage information from the instance.
        r = requests.get(self.artifactory_url + "api/storage/info", auth = (self.username, self.token))
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            # Storage information will be returned in JSON format.
            print("Storage information: " + json.dumps(r.json(), indent=4))
        else:
            print("The storage information failed to be retrieved.")

    def create_repository(self):
        # This function will create a new repository in the Jfrog artifactory.
        create_repository_dict = {} # Create a dictionary to store the repository information
        create_repository_dict["key"] = input("Repository key: ") # Repository key prompt
        create_repository_dict["rclass"] = "local" # Repository class
        create_repository_dict["packageType"] = input("Package Type: ") # Package type prompt ~ "Linux Debian"
        create_repository_dict["description"] = input("Description: ") # Description prompt
        headers = {'Content-Type': 'application/json'} # Header fields
        # The implementation of the API's put request on creating a new repository
        r = requests.put(self.artifactory_url + "api/repositories/" + create_repository_dict["key"], data=json.dumps(create_repository_dict).encode('utf-8'), headers=headers, auth = (self.username, self.token)) # Put request
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            print("The repository was successfully created.")
        else:
            # I also passed in the status code in there to make it easier to see what happened to the creation and updating of a given repository.
            print("The repository was not created." + str(r.status_code) + "\n" + (r.content.decode("utf-8")))

    def update_repository(self):
        # This function will update a repository in the Jfrog artifactory.
        update_repository_dict = {}
        update_repository_dict["key"] = input("Repository key: ") # Repository key prompt
        update_repository_dict["description"] = input("Description: ") # Description prompt
        headers = {'Content-Type': 'application/json'} # Header fields
        # The implementation of the API's post request on updating a repository
        r = requests.post(self.artifactory_url + "api/repositories/" + update_repository_dict["key"], data=json.dumps(update_repository_dict).encode('utf-8'), headers=headers, auth = (self.username, self.token)) # Post request
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            print("The repository was successfully updated.")
        else:
            # I also passed in the status code in there to make it easier to see what happened to the creation and updating of a given repository.
            print("The repository was not updated." + str(r.status_code) + "\n" (r.content.decode("utf-8")))

    def list_repositories(self):
        # This function will request the list of repositories from the instance.
        r = requests.get(self.artifactory_url + "api/repositories", auth = (self.username, self.token))
        # If the request is successful, the following code will be executed.
        if r.status_code == 200:
            # The list of repositories will be returned in JSON format.
            print("List of repositories: " + json.dumps(r.json(), indent=4))
        else:
            print("The list of repositories failed to be retrieved.")

# The following code will be executed when the program is run.
if __name__ == "__main__":
    # Create a new instance of the Artifactory class.
    artifactory = Artifactory()
    artifactory.switch() # Switch function