var express = require('express');
var app = express(); 
app.use('/', express.static(__dirname  + '/dist'))
app.listen(4000, ()=>{
    console.log('4000번 서버가 열렸습니다.')
});