const scrape = require('website-scraper');

const options = {
  urls: ['https://demo.shedpro.co/product/garden-shed/'],
  directory: './public',
  request: {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
  },
  filenameGenerator: 'bySiteStructure',
  recursive: false,
  maxDepth: 1,
  sources: [
    { selector: 'img', attr: 'src' },
    { selector: 'link[rel="stylesheet"]', attr: 'href' },
    { selector: 'script', attr: 'src' },
    { selector: 'source', attr: 'src' }
  ]
};

scrape(options)
  .then((result) => {
    console.log('Successfully scraped the website');
  })
  .catch((err) => {
    console.error('An error occurred:', err);
  });
