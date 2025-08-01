/**
 * ZapAnimator prototype for AWS Orbit mobile POC.
 *
 * This class manages the mascot's reaction states. Each state maps to a set
 * of CSS classes that trigger predefined keyframe animations defined in
 * stylesheets or Lottie sequences. You can extend this prototype to
 * integrate Lottie or canvas-based animations.
 */
export default class ZapAnimator {
  constructor(mascotElement, speechBubbleElement) {
    this.mascot = mascotElement;
    this.speech = speechBubbleElement;
    this.states = {
      correct: {
        cssClass: 'zap-celebrate',
        messages: [
          'Great job!',
          'You nailed it!',
          'Onward to the next challenge!'
        ]
      },
      wrong: {
        cssClass: 'zap-sad',
        messages: [
          'Keep trying!',
          'Almost there!',
          'Don\'t give up!'
        ]
      },
      streak: {
        cssClass: 'zap-streak',
        messages: [
          'Streak unlocked!',
          'You\'re on fire!',
          'Stellar streak!'
        ]
      },
      levelUp: {
        cssClass: 'zap-level-up',
        messages: [
          'Level up!',
          'Zap evolved!',
          'New abilities unlocked!'
        ]
      },
      hint: {
        cssClass: 'zap-hint',
        messages: [
          'Here\'s a hint…',
          'Think about the docs.',
          'Remember best practices!'
        ]
      }
    };
  }

  /**
   * Play a reaction state. Applies the appropriate CSS class and shows a
   * random encouraging message. Resets the previous state after the
   * animation completes.
   *
   * @param {string} stateName - One of 'correct', 'wrong', 'streak', 'levelUp', 'hint'
   */
  play(stateName) {
    const state = this.states[stateName];
    if (!state) return;
    // Remove existing state classes
    Object.values(this.states).forEach(s => this.mascot.classList.remove(s.cssClass));
    // Add new state class
    this.mascot.classList.add(state.cssClass);
    // Display random message
    const msg = state.messages[Math.floor(Math.random() * state.messages.length)];
    this.speech.textContent = msg;
    this.speech.classList.add('visible');
    // Hide message after 2 seconds
    setTimeout(() => {
      this.speech.classList.remove('visible');
      this.mascot.classList.remove(state.cssClass);
    }, 2000);
  }
}