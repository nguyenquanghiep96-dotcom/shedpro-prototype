const fs = require('fs');

const categories = {
  25: ['carport'],
  26: ['tiny home', 'victorian cabin', '2 story'],
  22: ['porch'],
  24: ['metal'],
  20: ['dog kennel', 'chicken coop', 'horse run-in', 'loafing shed', 'livestock'],
  19: ['greenhouse', 'teahouse', 'pergola', 'pavilion'],
  18: ['shed', 'aframe', 'chalet', 'cabin', 'cottage', 'barn', 'windsor', 'lakeside', 'studio', 'lean-to', 'hip roof', 'rancher', 'streamline', 'eave'],
  23: ['special']
};

let html = fs.readFileSync('public/v2/product/premium-shed/index.html', 'utf-8');

html = html.replace(/<li class="ssb-option display-thumbnail " data-href="[^"]*">.*?<span class="ssb-option-name">(.*?)<\/span>\s*<\/li>/gs, (match, name) => {
    let lowerName = name.toLowerCase();
    let assignedIds = ['all'];
    for (let id in categories) {
        if (categories[id].some(kw => lowerName.includes(kw))) {
            assignedIds.push(id);
        }
    }
    // Default to Utility Sheds (18) if no other matched (besides 'all')
    if (assignedIds.length === 1) {
        assignedIds.push(18);
    }
    
    return match.replace('<li class="ssb-option display-thumbnail "', `<li class="ssb-option display-thumbnail " data-category-ids="${assignedIds.join(',')}"`);
});

fs.writeFileSync('public/v2/product/premium-shed/index.html', html);
console.log('Categories assigned!');
