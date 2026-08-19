const fs = require('fs');
const https = require('https');
const cheerio = require('cheerio');
const path = require('path');

const html = fs.readFileSync('temp_shedpro.html', 'utf-8');
const $ = cheerio.load(html);

const styles = [];
$('#ssb-configurator-accordion-style .ssb-option.display-thumbnail').each((i, el) => {
    const $el = $(el);
    const category = $el.attr('data-component-categories') || '';
    const name = $el.find('.ssb-option-name').text().trim();
    const imgSrc = $el.find('img').attr('src');
    
    if (name && imgSrc) {
        styles.push({ name, category, imgSrc });
    }
});

fs.writeFileSync('styles.json', JSON.stringify(styles, null, 2));
console.log('Extracted ' + styles.length + ' styles.');
