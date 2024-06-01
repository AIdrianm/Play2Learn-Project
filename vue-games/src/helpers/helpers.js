import axios from 'axios';

export function saveGameResult(gameType, gameSettings, finalScore) {
    axios.post('/save_game_result/', {
        game_type: gameType,
        game_settings: gameSettings,
        final_score: finalScore
    })
    .then(response => {
        console.log('Game result saved:', response);
    })
    .catch(error => {
        console.error('Error saving game result:', error);
    });
}

export function getRandomInteger(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}