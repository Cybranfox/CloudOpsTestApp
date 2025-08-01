/*
 * Zap animation controller using the Canvas API. This module defines several
 * animation states and handles transitions. In a real implementation you
 * would draw sprite frames or vector shapes; here we set up the structure.
 */
export default class ZapCanvasAnimator {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.state = 'idle';
    this.lastTime = 0;
    this.animations = {
      correct: this.drawCorrect.bind(this),
      wrong: this.drawWrong.bind(this),
      idle: this.drawIdle.bind(this),
      sleepy: this.drawSleepy.bind(this),
      levelUp: this.drawLevelUp.bind(this),
      boss: this.drawBoss.bind(this),
    };
  }

  play(state) {
    this.state = state;
    requestAnimationFrame(this.loop.bind(this));
  }

  loop(timestamp) {
    const dt = timestamp - this.lastTime;
    this.lastTime = timestamp;
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    const drawFunc = this.animations[this.state] || this.drawIdle;
    drawFunc(dt);
    // Continue loop if not idle
    if (this.state !== 'idle') {
      requestAnimationFrame(this.loop.bind(this));
    }
  }

  // Placeholder drawing functions
  drawCorrect(dt) {
    // Draw thumbs up + nodding head; replace with real sprites
    this.ctx.fillStyle = 'green';
    this.ctx.fillRect(50, 50, 100, 100);
  }

  drawWrong(dt) {
    this.ctx.fillStyle = 'red';
    this.ctx.fillRect(50, 50, 100, 100);
  }

  drawIdle(dt) {
    this.ctx.fillStyle = 'blue';
    this.ctx.fillRect(50, 50, 100, 100);
  }

  drawSleepy(dt) {
    this.ctx.fillStyle = 'purple';
    this.ctx.fillRect(50, 50, 100, 100);
  }

  drawLevelUp(dt) {
    this.ctx.fillStyle = 'gold';
    this.ctx.fillRect(50, 50, 100, 100);
  }

  drawBoss(dt) {
    this.ctx.fillStyle = 'orange';
    this.ctx.fillRect(50, 50, 100, 100);
  }
}
