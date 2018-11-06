let data=require('./data1.json');
let data1 = require('./data.json');


console.log(data[0].job.map(e => e.job_title))
console.log(data1[9].job.map(e => e.job_title))