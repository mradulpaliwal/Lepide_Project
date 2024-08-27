import React from 'react';

const SummaryDisplay = ({ summarizedText }) => {
    return (
        <div>
            <h3>Summarized Text</h3>
            <p>{summarizedText}</p>
        </div>
    );
};

export default SummaryDisplay;
