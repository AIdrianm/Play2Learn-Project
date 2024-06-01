<template>
  <div class="math-facts">
    <h1>Math Facts Practice</h1>
    <div v-if="!gameFinished">
      <p>{{ question }}</p>
      <input v-model="userAnswer" @keyup.enter="checkAnswer" placeholder="Type your answer" />
      <button @click="checkAnswer">Submit</button>
      <p>Score: {{ score }}</p>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
    <div v-else>
      <h2>Game Over!</h2>
      <p>Your final score is: {{ score }}</p>
      <button @click="startNewGame">Play Again</button>
    </div>
  </div>
</template>

<script>
import { getRandomInteger, saveGameResult } from '../helpers/helpers';

export default {
  data() {
    return {
      question: '',
      answer: null,
      userAnswer: '',
      score: 0,
      gameFinished: false,
      errorMessage: ''
    };
  },
  methods: {
    generateQuestion() {
      const num1 = getRandomInteger(1, 20);
      const num2 = getRandomInteger(1, 20);
      this.question = `${num1} x ${num2} = ?`;
      this.answer = num1 * num2;
    },
    checkAnswer() {
      if (parseInt(this.userAnswer) === this.answer) {
        this.score += 1;
        this.userAnswer = '';
        this.generateQuestion();
      } else {
        this.errorMessage = 'Incorrect! Try again.';
        this.finishGame();
      }
    },
    startNewGame() {
      this.score = 0;
      this.gameFinished = false;
      this.userAnswer = '';
      this.errorMessage = '';
      this.generateQuestion();
    },
    finishGame() {
      this.gameFinished = true;
      const gameType = 'Math Facts Practice';
      const gameSettings = {
        operation: 'multiplication',
        maxNumber: 20
      };
      saveGameResult(gameType, gameSettings, this.score);
    }
  },
  mounted() {
    this.startNewGame();
  }
};
</script>

<style scoped>
.math-facts {
  text-align: center;
}
.error {
  color: red;
}
</style>
7777777777777777777777777777777