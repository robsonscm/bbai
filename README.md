Data Load - Python/MySQL
--------------------------

Project created for the BrainBox Ai Challenge

Remarks and assumptions:
-------------------------
- The environment has Python 3.7 installed and working
    - I used PyEnv to set up python's version and venv. 
    - It should be transparent, but I thought it was worth it to mention.
- The environment has MySQL 5.7.32 installed and working.
    - I used a Brew installation of MySQL.
    - I went with the basic of basics in the official docs for Python/MySQL connector.
- The DB connection will be set up running ``` config-project ``` script
    - There's no user creation included in the project setup
    - I did not create a new user. I installed MySQL and used 'root' user with no password for TESTS ONLY.   
    -- DO NOT RECOMMEND IT FOR ANY REAL IMPLEMENTATION  --  
    -- BE ALWAYS AWARE OF YOUR DATA SECURITY            -- :)
    - Should you choose user/password, it must have all the privileges to create and CRUD the tables.
- For the DB connection I'm using a db-config file in the root folder. 
    - In a more realistic scenario, this should be stored safely in a vault/encrypted solution
- There are many other features I could imagine about this tiny service (e.g. allocation changes for the RPis, filter per box/MAC addr for the report, an import table to log imports and errors, etc.)
- There are some 'bad practices' and 'lazy' implementations I could work on with more time or, as we discussed, with iterations over the tool.
    

Usage
---------------------
Installation:  
- Clone the project  
    ```git clone https://github.com/robsonscm/bbai.git```
- Change to the directory where you cloned the repo  
    ```cd bbai```
- Install all the dependencies  
    ```pip install -r requirements.txt```
- Please make sure the ``` config-project ``` script is executable  
    ``` chmod +x config-project ```
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
    Database brainboxai_challenge does not exists.
    Database brainboxai_challenge created successfully.
    DB brainboxai_challenge is set up and working
    Creating table boxes: OK
    Creating table rpis: OK
  ```    
- The project is now set and ready to use. 
- You should now run the import script to load the DB --> ``` box-data-import ``` 
- Then run the report script to query the results --> ``` box-data-report ``` 

Help:  
- ```
    ▶ ./box-data-import -h                 
    Syntax to call this script:
    box-data-import <path/file 1> <path/file 2> <path/file ...>
  ```  
- ```
    ▶ ./box-data-report -h                   
    Syntax to call this script:
    box-data-report <start date> <end date>
    
    ## Date format must be <YYYY-MM-DD> ##
    ## If no date is informed, the result will include all boxes/RPi in the database ##
    ## If just one date is informed, this will be used as the <start date> ##
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

