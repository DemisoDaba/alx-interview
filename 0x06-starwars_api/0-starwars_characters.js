#!/usr/bin/node

const request = require('request');
const ID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const film = JSON.parse(response.body);
  const listChar = film.characters;
  for (const i in listChar) {
    request(`${listChar[i]}`, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const character = JSON.parse(response.body);
      console.log(character.name);
    });
  }
});
