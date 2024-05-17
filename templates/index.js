let currentIndex = 1;

function showNextElement() {
  // Hide the current element
  document.getElementById(`element${currentIndex}`).classList.add('d-none');

  // Increment index or reset to 1 if it reaches the maximum
  currentIndex = (currentIndex % 3) + 1;

  // Show the next element
  document.getElementById(`element${currentIndex}`).classList.remove('d-none');
}

// Call the showNextElement function every 3 seconds
setInterval(showNextElement, 10000);   
