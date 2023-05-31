import React, { useState, useEffect } from 'react';
import './Recorder.css';
import { ReactMic } from 'react-mic';
import axios from 'axios';

export function Recorder() {
    const [record, setRecord] = useState(false);
    const [isAnalyzing, setAnalyzing] = useState(false);
    const [isWordDetected, setWordDetected] = useState(false);

    const toggleRecording = () => {
        setRecord(!record);
        setAnalyzing(record);
    };

    const onStop = async (recordedBlob) => {
        const file = new File([recordedBlob.blob], "recordedAudio.webm", {
            type: "audio/webm",
        });

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post("http://localhost:8000/audio/", formData);
            if(response.data.result === true) {
                setWordDetected(true);
            }
            setAnalyzing(false);
        } catch (error) {
            console.error('Error while sending audio blob to server:', error);
            setAnalyzing(false);
        }
    };

    // reset isWordDetected when record status changes
    useEffect(() => {
        setWordDetected(false);
    }, [record]);

    let displayText;
    if (isAnalyzing) {
        displayText = "Analyzing...";
    } else if (record) {
        displayText = "Recording...";
    } else if (isWordDetected) {
        displayText = <span><span style={{color: 'red'}}>"לחזור"</span> was said</span>;
    } else if (isWordDetected === false) {
        displayText = '"לחזור" wasn\'t said';
    } else {
        displayText = 'Record Audio';
    }

    return (
        <div className="recorder-container">
            <ReactMic
                record={record}
                onStop={onStop}
                strokeColor="#000000"
                backgroundColor="#FFFFFF" />
            <button onClick={toggleRecording} className={`record-button ${record ? 'stop' : 'start'}`} />
            <p className="word">{displayText}</p>
        </div>
    );
}
