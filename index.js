const express = require("express");
const app = express();
const PORT = process.env.PORT;
const PORT3 = "3000";
app.get("/", (req, res) => {
  res.send({ hello: "world" });
});

app.get("/hello", (req, res) => {
  res.send("in hello");
});

app.get("/python", (req, res) => {
  var spawn = require("child_process").spawn;
  var process = spawn("python", [
    "./testPython.py",
    req.query.inputData, // for example ~ 3
  ]);
  process.stdout.on("data", function (data) {
    res.send(data.toString());
  });
});

app.get("/movie", (req, res) => {
  var spawn = require("child_process").spawn;
  var process = spawn("python", [
    "./DataRecommend.py",
    req.query.inputData, // for example ~ 3
  ]);
  process.stdout.on("data", function (data) {
    res.send(data.toString() + " recommended");
  });
});

app.get("/test", (req, res) => {
  var spawn = require("child_process").spawn;
  var process = spawn("python", [
    "./testpy.py",
    req.query.inputData, // for example ~ 3
  ]);
  process.stdout.on("data", function (data) {
    res.send(data.toString());
  });
});

app.listen(PORT);
