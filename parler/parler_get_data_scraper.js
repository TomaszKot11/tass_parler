const { exec } = require('child_process');
const fs = require('fs');

// https://github.com/castlelemongrab/parlance
const sampleAccounts = ['Johnnyjoe1083', 'LHolden', 'BuddyDavis21', 'Compatriot'];



const serializeToFile = (object, fileName) => {
    const data = JSON.stringify(object);
    fs.writeFile(`${fileName}.json`, data, (err) => {
        if (err) {
            throw err;
        }
        console.log(`JSON data in ${fileName}.json is saved`);
    });
}

fetchData = (accountName, packageOption, fileName) => {
    exec(`parlance ${packageOption} -u ${accountName} -c config.json`, (err, stdout, stderr) => {
        if (err) {
            console.log(`Error while fetching for ${accountName} ${err}`);
            return;
        }
        const stdoutArr = JSON.parse(stdout);
        console.log('.');
        serializeToFile(stdoutArr, fileName);
        console.log('.');
    });
}



for(var accountName of sampleAccounts) {
    // followers
    fetchData(accountName, 'followers', `${accountName}.followers`);
    // friends  -> following
    fetchData(accountName, 'following', `${accountName}.friends`);
}

console.log('Finished data fetching!');