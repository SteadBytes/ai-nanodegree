// Mimic Me!
// Fun game where you need to express emojis being displayed

// --- Affectiva setup ---

// The affdex SDK Needs to create video and canvas elements in the DOM
var divRoot = $("#camera")[0]; // div node where we want to add these elements
var width = 640,
  height = 480; // camera image size
var faceMode = affdex.FaceDetectorMode.LARGE_FACES; // face mode parameter

// Initialize an Affectiva CameraDetector object
var detector = new affdex.CameraDetector(divRoot, width, height, faceMode);

// Enable detection of all Expressions, Emotions and Emojis classifiers.
detector.detectAllEmotions();
detector.detectAllExpressions();
detector.detectAllEmojis();
detector.detectAllAppearance();

// --- Utility values and functions ---

// Unicode values for all emojis Affectiva can detect
var emojis = [
  128528,
  9786,
  128515,
  128524,
  128527,
  128521,
  128535,
  128539,
  128540,
  128542,
  128545,
  128563,
  128561
];

// Update target emoji being displayed by supplying a unicode value
function setTargetEmoji(code) {
  $("#target").html("&#" + code + ";");
}

// Convert a special character to its unicode value (can be 1 or 2 units long)
function toUnicode(c) {
  if (c.length == 1) return c.charCodeAt(0);
  return (
    (c.charCodeAt(0) - 0xd800) * 0x400 + (c.charCodeAt(1) - 0xdc00) + 0x10000
  );
}

// Update score being displayed
function setScore(correct, total) {
  $("#score").html("Score: " + correct + " / " + total);
}

// Display log messages and tracking results
function log(node_name, msg) {
  $(node_name).append("<span>" + msg + "</span><br />");
}

// --- Callback functions ---

// Start button
function onStart() {
  if (detector && !detector.isRunning) {
    $("#logs").html(""); // clear out previous log
    detector.start(); // start detector
  }
  log("#logs", "Start button pressed");
}

// Stop button
function onStop() {
  log("#logs", "Stop button pressed");
  if (detector && detector.isRunning) {
    detector.removeEventListener();
    detector.stop(); // stop detector
  }
}

// Reset button
function onReset() {
  log("#logs", "Reset button pressed");
  if (detector && detector.isRunning) {
    detector.reset();
  }
  $("#results").html(""); // clear out results
  $("#logs").html(""); // clear out previous log

  resetGame()

}

// Add a callback to notify when camera access is allowed
detector.addEventListener("onWebcamConnectSuccess", function () {
  log("#logs", "Webcam access allowed");
});

// Add a callback to notify when camera access is denied
detector.addEventListener("onWebcamConnectFailure", function () {
  log("#logs", "webcam denied");
  console.log("Webcam access denied");
});

// Add a callback to notify when detector is stopped
detector.addEventListener("onStopSuccess", function () {
  log("#logs", "The detector reports stopped");
  $("#results").html("");
});

// Add a callback to notify when the detector is initialized and ready for running
detector.addEventListener("onInitializeSuccess", function () {
  log("#logs", "The detector reports initialized");
  //Display canvas instead of video feed because we want to draw the feature points on it
  $("#face_video_canvas").css("display", "block");
  $("#face_video").css("display", "none");

  initGame();
});

// Add a callback to receive the results from processing an image
// NOTE: The faces object contains a list of the faces detected in the image,
//   probabilities for different expressions, emotions and appearance metrics
detector.addEventListener("onImageResultsSuccess", function (
  faces,
  image,
  timestamp
) {
  var canvas = $("#face_video_canvas")[0];
  if (!canvas) return;

  // Report how many faces were found
  $("#results").html("");
  log("#results", "Timestamp: " + timestamp.toFixed(2));
  log("#results", "Number of faces found: " + faces.length);
  if (faces.length > 0) {
    // Report desired metrics
    log("#results", "Appearance: " + JSON.stringify(faces[0].appearance));
    log(
      "#results",
      "Emotions: " +
      JSON.stringify(faces[0].emotions, function (key, val) {
        return val.toFixed ? Number(val.toFixed(0)) : val;
      })
    );
    log(
      "#results",
      "Expressions: " +
      JSON.stringify(faces[0].expressions, function (key, val) {
        return val.toFixed ? Number(val.toFixed(0)) : val;
      })
    );
    log("#results", "Emoji: " + faces[0].emojis.dominantEmoji);

    // Call functions to draw feature points and dominant emoji (for the first face only)
    drawFeaturePoints(canvas, image, faces[0]);
    drawEmoji(canvas, image, faces[0]);

    gameUpdate(faces[0], timestamp);
  }
});

// --- Custom functions ---

// Draw the detected facial feature points on the image
function drawFeaturePoints(canvas, img, face) {
  // Obtain a 2D context object to draw on the canvas
  var ctx = canvas.getContext("2d");

  ctx.strokeStyle = "white";

  // Loop over each feature point in the face
  for (var id in face.featurePoints) {
    var featurePoint = face.featurePoints[id];
    ctx.beginPath();
    ctx.arc(featurePoint.x, featurePoint.y, 2.5, 0, Math.PI * 2);
    ctx.stroke();
  }
}

// Draw the dominant emoji on the image
function drawEmoji(canvas, img, face) {
  // Obtain a 2D context object to draw on the canvas
  let ctx = canvas.getContext("2d");
  ctx.font = "40px serif";
  let eyebrowFeaturePoint = face.featurePoints[10];
  ctx.fillText(
    face.emojis.dominantEmoji,
    eyebrowFeaturePoint.x,
    eyebrowFeaturePoint.y
  );
}

// TODO: Define any variables and functions to implement the Mimic Me! game mechanics

// NOTE:
// - Remember to call your update function from the "onImageResultsSuccess" event handler above
// - You can use setTargetEmoji() and setScore() functions to update the respective elements
// - You will have to pass in emojis as unicode values, e.g. setTargetEmoji(128578) for a simple smiley
// - Unicode values for all emojis recognized by Affectiva are provided above in the list 'emojis'
// - To check for a match, you can convert the dominant emoji to unicode using the toUnicode() function

// Optional:
// - Define an initialization/reset function, and call it from the "onInitializeSuccess" event handler above
// - Define a game reset function (same as init?), and call it from the onReset() function above

// <your code here>


function Alert(msg, alertClass) {
  this.parent = document.body;
  this.msg = msg;
  this.alertClass = alertClass;
  this.el = null;
}

Alert.prototype.build = function () {
  let html = `<div class="alert ${this.alertClass}" role="alert">${this.msg}</div>`;
  return html
}

Alert.prototype.show = function () {
  this.el = $(this.build()).appendTo(this.parent);
  setTimeout(() => {
    this.el.remove();
  }, 2500)
}

Alert.prototype.hide = function () {
  this.el.remove();
}

let targetEmoji;
let numRounds;
let numCorrect;
let currRoundStartTime;
const maxRoundTime = 10;

let alert = new Alert('BOOM that matched :) New round starting now!', 'alert-success').show();

function showAlert(alert, msg) {
  alert.text(msg)
  window.clearTimeout(timerHandle);
  if ($alert.hasClass('invisible')) {
    $alert.toggleClass("invisible visible")
  }
}


function initGame() {
  targetEmoji = randomEmoji(emojis);
  numRounds = 0;
  numCorrect = 0;
  startNewRound(0);
}

function resetGame() {
  targetEmoji = 0;
  numRounds = 0;
  numCorrect = 0
  currRoundStartTime = 0;
  $("#target").text("?");
}

function gameUpdate(face, timestamp) {
  if (timestamp.toFixed(0) - currRoundStartTime < maxRoundTime) {
    if (faceEmojiMatch(face, targetEmoji)) {
      numCorrect++;
      log("#logs", "BOOM that matched!");
      let alert = new Alert('BOOM that matched :) New round starting now!', 'alert-success').show();
      startNewRound(timestamp);
    }
  } else {
    log("#logs", "Too slow! New round starting now!");
    let alert = new Alert('Too slow :( New round starting now!', 'alert-danger').show();
    startNewRound(timestamp);
  }
}

function startNewRound(timestamp) {
  numRounds++;
  currRoundStartTime = timestamp.toFixed(0);
  targetEmoji = randomEmoji(emojis);
  setTargetEmoji(targetEmoji);
  setScore(numCorrect, numRounds);
  log("#logs", "New round - GO!");
}


function faceEmojiMatch(face, targetEmoji) {
  return toUnicode(face.emojis.dominantEmoji) == targetEmoji;
}

function randomEmoji(emojiList) {
  return emojiList[Math.floor(Math.random() * emojiList.length)];
}