const express = require('express');
const fs = require('fs').promises;
const path = require('path');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, '../call-bot-frontend/public')));

const logFilePath = path.join('C:', 'Users', 'apt20', 'OneDrive', 'Desktop', 'Bland caller lists', 'callers.log');

app.post('/log-caller', async (req, res) => {
    const { phone_number, timestamp } = req.body;
    if (!phone_number || !timestamp) {
        return res.status(400).json({ error: 'Phone number and timestamp required' });
    }

    try {
        const logEntry = `${timestamp} - ${phone_number}\n`;
        await fs.appendFile(logFilePath, logEntry);
        res.status(200).json({ message: 'Caller logged successfully' });
    } catch (error) {
        console.error('Error writing to file:', error);
        res.status(500).json({ error: 'Failed to log caller' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});