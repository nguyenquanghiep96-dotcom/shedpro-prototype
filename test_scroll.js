var fs = require('fs');
var html = fs.readFileSync('./public/v2/product/premium-shed/index.html', 'utf8');
console.log(html.includes('v2-active'));
