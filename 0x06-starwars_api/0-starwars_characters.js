#!/usr/bin/node

const axios = require('axios');

const filmId = process.argv[2];

const URL = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

axios.get(URL)
  .then(response => {
    const film = response.data;
    const characters = film.characters;

    const printCharacterName = async (characterUrl) => {
      try {
        const characterResponse = await axios.get(characterUrl);
        console.log(characterResponse.data.name);
      } catch (error) {
        console.error('Error:', error.response.status);
      }
    };

    characters.forEach(printCharacterName);
  })
  .catch(error => {
    console.error('Error:', error.response.status);
  });

