# Welcome to my JFrog Production Engineering Academy - Home Assignment
## Description
My name is Jordan Tingling and this is my JFrog Production Engineering Academy - Home Assignment submission.
The research for this project was vast and learning the JFrog Artifactory service was challenging but rewarding. From my research the JFrog CLI is an absolutely amazing and interesting tool to use in order to manage, maintain and access your entire suite of Artifacts and repositories etc. Understanding the JFrog API access was definately more challenging than understanding the CLI, however, with the use of multiple online resources, videos, articles and documentations provided by JFrog or Third-party sources, I was able to understand the concepts, syntax and use cases in order to complete this assignment to the best of my ability.

## Installation
They are two ways to install the project:
The first one:

```cmd
pip3 install jordantingling -i  https://jordantingling.jfrog.io/artifactory/tingling-jfrog-assignment/jordantingling

```
username: jordantingling \
password: jordan762Mj!

The second:

``` cmd
git clone https://github.com/SirTingling/jfrog-assessment.git
pip3 install -r requirements.txt
cd jfrog-project/
```

## Usage
python3 jfrog-artifactory.py [-h] [-p] [-v] [-si] [-lr] [-cr] [-dr] [-ur] [-cu] [-du]

optional arguments: 

flag | long                | description
---- |---------------------|--------------------------------
-h   | --help              | Show all the available arguments and commands
-p   | --system_ping       | Return the ping requested from the system
-v   | --system_version    | Return system version
-cu  | --create_user       | Create a new user
-du  | --delete_user       | Delete a user
-si  | --get_storage_info  | Return the storage information of the system
-cr  |  --create-repository  |  Create a new repository
-dr  | --delete_repository | Delete repository
-ur  | --update_repository | Update a repository
-lr  | --list_repositories | List all repositories

## The Resources I used

It was callenging, these resources brought me up to speed on very essential topics, tools and how they work etc in a limited time span.

1. [JFrog's official Documentation](https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API)
2. [How to Generate an access Token](https://www.youtube.com/watch?v=OQ4_ZGCnqIo)
3. [JFrog artifactory overview](https://academy.jfrog.com/jfrog-artifactory-overview-2020/443201)
4. [JFrog Confluence](https://www.jfrog.com/confluence/display/RTF)
5. [JFrog Artifactory REST API](https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API)

Even these webinars and videos were great sources of information:

6. [Artifact Management with JFrog Artifactory](https://www.youtube.com/watch?v=GneNpJI7YFc&t=2908s)
7. [One CLI to Rule Them All](https://www.youtube.com/watch?v=8WHOPdMlz-A&t=3636s)
8. [Artifactory Management with JFrog Artifactory](https://www.youtube.com/watch?v=bKp1Vif9oO4&t=2495s)

I needed a Python CLI script to manage an Artifactory SaaS instance with all the necessary features, these are the resources that helped me:

9. [Python Library "argparse"](https://docs.python.org/3/library/argparse.html)
10. [Jfrog's REST-API-Examples](https://github.com/jfrog/artifactory-scripts/tree/master/REST-API-Examples)

