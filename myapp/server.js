'use strict';
const express = require('express');
//const a = require('jomodul')

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  let date_ob = new Date();

  res.send('Hello World reee dfgjkljhkljkdsg' + date_ob.getSeconds());

});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);