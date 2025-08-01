/*
 * A simple Zap animation controller using CSS classes. States include idle,
 * correct, wrong and battle. You can extend with more animations as needed.
 */
export default class ZapController {
  constructor(imgElement) {
    this.img = imgElement;
    this.reset();
  }

  reset() {
    this.img.classList.remove('zap-correct', 'zap-wrong', 'zap-battle', 'zap-idle');
    this.img.classList.add('zap-idle');
  }

  play(state) {
    this.reset();
    switch (state) {
      case 'correct':
        this.img.classList.add('zap-correct');
        break;
      case 'wrong':
        this.img.classList.add('zap-wrong');
        break;
      case 'battle':
        this.img.classList.add('zap-battle');
        break;
      default:
        this.img.classList.add('zap-idle');
    }
  }
}
