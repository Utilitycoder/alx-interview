#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Retrieve the Movie ID from command line argument

if (!movieId) {
  console.log('Please provide a Movie ID as a command line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/films/${movieId}`;

// Function to fetch characters from the movie
function getCharactersFromMovie(movieUrl) {
  request(movieUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      // Function to fetch character names and print them
      function fetchAndPrintCharacterNames(urls, index = 0) {
        if (index < urls.length) {
          request(urls[index], (charError, charResponse, charBody) => {
            if (!charError && charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
              fetchAndPrintCharacterNames(urls, index + 1);
            } else {
              console.log('Error fetching character data.');
            }
          });
        }
      }

      fetchAndPrintCharacterNames(characterUrls);
    } else {
      console.log('Error fetching movie data.');
    }
  });
}

getCharactersFromMovie(apiUrl);
