
const fs = require('fs');

const filePath = 'C:/Users/ALK/Documents/aleo/imageDisplay/images'
const imageList = []


fs.readdir(filePath, (err,files) => {
    if(err){
        console.error(err);
    }

files.forEach((file,index) => {
    imageList.push(file)
})
console.log(imageList)

});

