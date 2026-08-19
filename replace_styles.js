const fs = require('fs');
let html = fs.readFileSync('public/v2/product/premium-shed/index.html', 'utf-8');
const newStyles = fs.readFileSync('new_styles.html', 'utf-8');

const startIndex = html.indexOf('<ul class="ssb-configurator-options ssb-configurator-style-sub-cat has-default">');
const endIndexStr = '</ul>';
let searchIndex = html.indexOf(endIndexStr, startIndex);
// The first </ul> after startIndex is the end of the styles list.
const endIndex = searchIndex + endIndexStr.length;

if (startIndex !== -1 && searchIndex !== -1) {
    html = html.substring(0, startIndex) + newStyles + html.substring(endIndex);
    fs.writeFileSync('public/v2/product/premium-shed/index.html', html);
    console.log('Replaced successfully!');
} else {
    console.log('Failed to find markers.');
}
