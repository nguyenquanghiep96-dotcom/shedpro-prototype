const fs = require('fs');
const path = require('path');
const svg = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-svg"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/><path d="m15 5 4 4"/></svg>`;
fs.writeFileSync(path.join(__dirname, 'public/v1/shedpro-design/assets/icons/raw/ic-edit-shed.svg'), svg);
