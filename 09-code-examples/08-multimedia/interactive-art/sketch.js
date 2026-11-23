// Interactive Animated Art — Kilele TechPath, Pathway 8 (Multimedia)
// Uses the p5.js creative coding library.

let x = 100;
let y = 100;

let speedX = 3;
let speedY = 2;

function setup() {
    createCanvas(600, 400);
}

function draw() {

    background(20, 30, 50);

    fill(0, 220, 255);

    noStroke();

    circle(x, y, 60);

    x += speedX;
    y += speedY;

    if (x > width - 30 || x < 30) {
        speedX *= -1;
    }

    if (y > height - 30 || y < 30) {
        speedY *= -1;
    }
}
