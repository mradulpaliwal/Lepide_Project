export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    return data.file_path;
};

export const summarizeFile = async (filePath) => {
    const response = await fetch('http://localhost:8000/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ file_path: filePath })
    });

    const data = await response.json();
    return data.summary;
};
