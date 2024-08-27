import React, { useState } from 'react';
import { uploadFile, summarizeFile } from '../api/api';

const FileUpload = ({ setSummarizedText }) => {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return;

        setLoading(true);
        try {
            // Upload the file
            const filePath = await uploadFile(file);

            // Request summarization
            const summary = await summarizeFile(filePath);
            setSummarizedText(summary);
        } catch (error) {
            console.error("Error summarizing the document:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <button type="submit" disabled={loading}>Upload & Summarize</button>
            </form>
            {loading && <p>Summarizing document...</p>}
        </div>
    );
};

export default FileUpload;
