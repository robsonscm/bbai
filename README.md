Data Load - Python/MySQL
--------------------------

Project created for the BrainBox Ai Challenge

Remarks and assumptions:
-------------------------
- The environment has Python 3.7 installed and working
    - I used PyEnv to set up python's version and venv. 
    - It should be transparent, but just in case something looks weird to you in the project/execution.
- The environment has MySQL 5.7.32 installed and working.
    - I used a Brew installation of MySQL.
    - I went with the basic of basics in the official docs for Python/MySQL connector.
- The DB connection will be set up running ``` config-project ``` script
    - There's no user creation included in the project setup
    - I did not create a new user. I installed MySQL and used 'root' user with no password for tests only.   
    -- DO NOT RECOMMEND IT FOR ANY REAL IMPLEMENTATION - BE ALWAYS AWARE OF YOUR DATA SECURITY -- :)
    - The user/password you choose must have all the privileges to create and CRUD the tables.
- For the DB connection I'm using a db-config file in the root folder. 
    - In a more realistic scenario, this should be stored safely in a vault/encrypted solution
    

Usage
---------------------
Installation:  
- Clone the project using ```git clone https://github.com/robsonscm/bbai.git```
- To install all the dependencies, please, run ```pip install -r requirements.txt```
- Please make sure the ``` config-project ``` script is executable
  - ``` chmod +x config-project ```
- run the ``` config-project ``` script
  - if all goes well, and you choose to just go with the default values, you should have an output like this:
  ```
  ▶ ./config-project   
  =============== Project Setup =================
  Let's set up the database connection first
  host [default:127.0.0.1]: 
  db name [default:brainboxai_challenge]: 
  username [default:root]: 
  password [default:]: 
  DB is set up and working
  Creating table boxes: already exists.
  Creating table rpis: already exists.
  (venv) 
  ```    
- The project is now set and ready to use. 
- You should now run the import script to load the DB --> ``` box-data-import ``` 
- Then run the report script to query the results --> ``` box-data-report ``` 

Help:  
- ```
    ▶ ./box-data-import -h                 
    Syntax to call this script:
    box-data-import <file 1> <file 2> <file n>
    (venv)
  ```  
- ```
    ▶ ./box-data-report -h                       
    Syntax to call this script:
    box-data-report <start date> <end date>
    
    ## If no date is informed, the result will include all boxes/RPi in the database ##
    ## If just one date is informed, this will be used as the <start date> ##
    (venv) 
  ```  

Tech stack
---------------------
- Python  
    - https://www.python.org/downloads/
    - Version 3.7.10
- MySQL
    - https://www.mysql.com/downloads/
    - Version 5.7.32
- PyEnv
  - https://github.com/pyenv/pyenv-virtualenv
  - https://opensource.com/article/20/4/pyenv
  - Version 1.2.23

