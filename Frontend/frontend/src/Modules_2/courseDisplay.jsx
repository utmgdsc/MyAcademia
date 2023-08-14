import React,{ useState, useRef, useEffect } from "react";
import { Button, Container, Row, ButtonGroup } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
const course_display = () => {
    const [showTextBox, setShowTextBox] = useState(false);
    const [outputValue, setOutputValue] = useState('');
    const textAreaRef = useRef(null);
    const handleButtonClick = () => {
        const generatedOutput = "This is the output";
        setShowTextBox(true);
        setOutputValue(generatedOutput);
    };
}
export default course_display;