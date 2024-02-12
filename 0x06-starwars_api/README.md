# Star Wars Characters

This script fetches and prints all characters of a Star Wars movie based on the provided movie ID.

## Requirements
- Node.js installed
- The `request` module
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

