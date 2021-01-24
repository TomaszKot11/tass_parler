const { exec } = require('child_process');
const fs = require('fs');

const MST = 's%3ALcDqosWVeX24zx2Vyx7UDbnn8TIBUitHGkzMrCSpDaSjlQ9RlBRUlot7Y9tofA7AXy7oaP9Ta5Ps34r7A3qDs54pViVnkdc8SKhMqW8UNPAmU20Z67X7BBgf9ti7EGTC.sEC6TLc8kP%2FAaKNLGPJzai8kRjxoWfrusit9bxX0Ksc';
const JST = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOjE4MjkwNzIyLCJ1c2VySWQiOjEyMzE1MjI1LCJwZXJtaXNzaW9ucyI6MjU2LCJ2ZXJpZmllZCI6ZmFsc2UsImlhdCI6MTYwODMyNjU0NywiZXhwIjoxNjA4MzI2ODQ3fQ.QHTyK4HiNyEGDNeWb8arv4-Qst7v92JYFvEceUamPeXJcVdQySHZR3ZIyM8viFHpfZSXHOpASxKpCTRxOapEwQ';

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
    exec(`parlance ${packageOption} -u ${accountName} -c auth.json`, (err, stdout, stderr) => {
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