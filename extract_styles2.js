const fs = require('fs');
const cheerio = require('cheerio');
const html = fs.readFileSync('temp_shedpro.html', 'utf-8');
const $ = cheerio.load(html);

console.log($('#ssb-configurator-accordion-style .ssb-option.display-thumbnail').first().parent().html());
