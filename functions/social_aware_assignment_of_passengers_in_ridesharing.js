const { spawn } = require('child_process');

exports.handler = (event, context, callback) => {
    const python = spawn('python', ['./social_aware_assignment_of_passengers_in_ridesharing.py']);
    let output = '';

    python.stdout.on('data', function(data) {
        output += data;
    });

    python.on('close', (code) => {
        callback(null, {
            statusCode: 200,
            body: output
        });
    });
};