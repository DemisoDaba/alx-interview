# Star Wars Characters

This script fetches and prints all characters of a Star Wars movie based on the provided movie ID.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using node (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var
- Install Node 10
    ```bash
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```
- Install semi-standard
    ```bash
    sudo npm install semistandard --global
    ```
- Install request module and use it
    ```bash
    sudo npm install request --global
    export NODE_PATH=/usr/lib/node_modules
    ```

## Usage

To run the script, provide the movie ID as a positional argument:

```bash
./0-starwars_characters.js <movie_id>

