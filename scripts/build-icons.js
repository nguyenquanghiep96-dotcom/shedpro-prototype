const fs = require('fs');
const path = require('path');

const RAW_DIR = path.join(__dirname, '../public/v1/shedpro-design/assets/icons/raw');
const OUT_DIR = path.join(__dirname, '../public/v1/shedpro-design/assets/icons');

const files = fs.readdirSync(RAW_DIR).filter(f => f.endsWith('.svg'));

let cssContent = `/* Icon Design System */
.icon {
    display: inline-block;
    width: 24px;
    height: 24px;
    background-color: currentColor;
    -webkit-mask-size: contain;
    mask-size: contain;
    -webkit-mask-repeat: no-repeat;
    mask-repeat: no-repeat;
    -webkit-mask-position: center;
    mask-position: center;
    vertical-align: middle;
}
`;

let spriteContent = `<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">\n`;

files.forEach(file => {
    const name = path.basename(file, '.svg');
    let svgContent = fs.readFileSync(path.join(RAW_DIR, file), 'utf8');

    // Clean up SVG
    svgContent = svgContent.replace(/fill="#2B3B63"/gi, 'fill="currentColor"');
    svgContent = svgContent.replace(/class="[^"]*"/gi, '');
    
    // Attempt to extract viewBox, default to 0 0 24 24
    let viewBoxMatch = svgContent.match(/viewBox="([^"]+)"/);
    let viewBox = viewBoxMatch ? viewBoxMatch[1] : '0 0 24 24';

    let symbolContent = svgContent
        .replace(/<svg[^>]*>/, `<symbol id="${name}" viewBox="${viewBox}">`)
        .replace(/<\/svg>/, '</symbol>');
        
    // For CSS Mask, properly encode for data URI
    let dataUriSvg = svgContent
        .replace(/\r?\n|\r/g, ' ')
        .replace(/"/g, "'")
        .replace(/%/g, '%25')
        .replace(/#/g, '%23')
        .replace(/</g, '%3C')
        .replace(/>/g, '%3E');
    
    cssContent += `
.${name} {
    -webkit-mask-image: url("data:image/svg+xml;charset=utf-8,${dataUriSvg}");
    mask-image: url("data:image/svg+xml;charset=utf-8,${dataUriSvg}");
}
`;

    spriteContent += `  ${symbolContent}\n`;
});

spriteContent += `</svg>`;

fs.writeFileSync(path.join(OUT_DIR, 'icons.css'), cssContent);
fs.writeFileSync(path.join(OUT_DIR, 'sprite.svg'), spriteContent);

console.log(`Successfully built ${files.length} icons into icons.css and sprite.svg`);
