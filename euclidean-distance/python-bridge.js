const appContainer = document.querySelector('#euclidean-distance .app');
const background = document.querySelector('#euclidean-distance .container_inner');

function runPython() {
  appContainer.innerHTML = `
    <py-script type="mpy" src="euclidean-distance/project.py" async="true" terminal>
    </py-script>`;
  background.style.transition = 'background-image 1s, opacity 200ms';
  background.style.opacity = '0';
  // Wait for the script to render, then fade out the background image
  setTimeout(() => {
    // After the fade-out transition, set the background image to 'none'
    setTimeout(() => {
      background.style.backgroundImage = 'none';
      background.style.opacity = '1'; // Reset opacity if needed
    }, 1000); // Match this duration with the transition duration
  }, 1000); // Adjust the timeout duration as needed
}