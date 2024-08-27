import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import SummaryDisplay from './components/SummaryDisplay';
import './styles.css';

function App() {
    const [summarizedText, setSummarizedText] = useState('');

    return (
        <div className="App">
            <h1>Document Summarizer</h1>
            <FileUpload setSummarizedText={setSummarizedText} />
            <SummaryDisplay summarizedText={summarizedText} />
        </div>
    );
}

export default App;
