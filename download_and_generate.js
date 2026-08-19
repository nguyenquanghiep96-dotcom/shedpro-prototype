const fs = require('fs');
const https = require('https');
const cheerio = require('cheerio');
const path = require('path');

const imgDir = path.join(__dirname, 'public/assets/images/styles');
if (!fs.existsSync(imgDir)) {
    fs.mkdirSync(imgDir, { recursive: true });
}

function downloadImage(url, filepath) {
    return new Promise((resolve, reject) => {
        if (!url) return resolve();
        https.get(url, (res) => {
            if (res.statusCode !== 200) {
                return reject(new Error('Failed to download ' + url));
            }
            const file = fs.createWriteStream(filepath);
            res.pipe(file);
            file.on('finish', () => {
                file.close();
                resolve();
            });
        }).on('error', (err) => {
            fs.unlink(filepath, () => reject(err));
        });
    });
}

async function main() {
    const html = fs.readFileSync('temp_shedpro.html', 'utf-8');
    const $ = cheerio.load(html);

    let styles = [];
    $('#ssb-configurator-accordion-style .ssb-option.display-thumbnail').each((i, el) => {
        const $el = $(el);
        const name = $el.find('.ssb-option-name').text().trim();
        let imgSrc = $el.find('img').attr('src');
        const dataHref = $el.attr('data-href');
        
        if (name && imgSrc) {
            styles.push({ name, imgSrc, dataHref });
        }
    });

    // Reorder: Chalet, Aframe, Premium Shed, Log Cabin at the top
    const topNames = ['Chalet', 'Aframe', 'Premium Shed', 'Log Cabin'];
    const topStyles = [];
    const otherStyles = [];
    
    styles.forEach(s => {
        const idx = topNames.indexOf(s.name);
        if (idx !== -1) {
            topStyles[idx] = s;
        } else {
            otherStyles.push(s);
        }
    });
    
    // Remove empty slots if any of the top 4 are missing
    styles = topStyles.filter(Boolean).concat(otherStyles);

    let newHtml = '<ul class="ssb-configurator-options ">\n';

    for (let i = 0; i < styles.length; i++) {
        const s = styles[i];
        if (!s.imgSrc.startsWith('http')) {
            s.imgSrc = 'https:' + s.imgSrc; // Handle protocol-relative URLs if any
        }
        
        // Ensure valid extension
        let ext = path.extname(new URL(s.imgSrc).pathname) || '.jpg';
        const filename = s.name.replace(/[^a-z0-9]/gi, '_').toLowerCase() + ext;
        const filepath = path.join(imgDir, filename);
        
        await downloadImage(s.imgSrc, filepath);
        
        const localSrc = `../../assets/images/styles/${filename}`;
        
        newHtml += `					<li class="ssb-option display-thumbnail " data-href="${s.dataHref || '#'}">
						<div class="ssb-thumbnail">
							<img src="${localSrc}" alt="">
						</div>
						<span class="ssb-option-name">${s.name}</span>
					</li>\n`;
    }

    newHtml += '				</ul>';
    
    fs.writeFileSync('new_styles.html', newHtml);
    console.log('Downloaded images and generated new_styles.html with ' + styles.length + ' items.');
}

main().catch(console.error);
