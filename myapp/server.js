'use strict';
const a = require('jomodul')
const c = require('jomodul2')

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  let b = a.sayHello()
  res.send('Hello World' + Date.now()+ b + ' ' + c.sayHello());
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);