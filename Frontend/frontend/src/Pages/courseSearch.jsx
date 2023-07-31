import React, { useState, useRef, useEffect } from "react";
import {
  FloatingLabel,
  Form,
  Row,
  Col,
  Dropdown,
  Button,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
//import courseDisplay from "./courseDisplay";
const divStyle = {
  display: "flex",
  justifyContent: "flex-end",
  padding: "50px",
};

function CourseSearch() {
  // const course_display = React.useRef(null);
  // const course_display_method=()=>{if (courseDisplay.current) {
  //     course_display.current.handleButtonClick();
  //   }
  // };
  let items = [];
  axios.get("api/getProgramAreas/").then((response) => {
    items = response.data;
    console.log(items);
  });
  // console.log(items);
  const [showTextBox, setShowTextBox] = useState(false);
  const [outputValue, setOutputValue] = useState("");
  const textAreaRef = useRef(null);
  const handleButtonClick = () => {
    const course_input = document.getElementById("course_code-textarea").value;
    const course_prereq = document.getElementById(
      "pre-requisites-textarea"
    ).value;
    const course_distribution = document.getElementById(
      "dropdown-distribution"
    ).value;

    const generatedOutput = "This is the output";
    setShowTextBox(true);
    setOutputValue(generatedOutput);
  };
  return (
    <>
      <h2>Course Search</h2>
      <Row>
        <Col xs={8} md={3}>
          <FloatingLabel
            controlId="course_code-textarea"
            label="Course Code(ABCH5)"
            className="mb-3"
          >
            <Form.Control
              as="textarea"
              placeholder="Smaller Input"
              size="sm"
              style={{ height: "10px", resize: "none", width: "auto" }} // Adjust the height as needed
            />
          </FloatingLabel>
        </Col>
        <Col xs={8} md={3}>
          <FloatingLabel
            controlId="pre-requisites-textarea"
            label="Pre-requisites(ABCH5)"
            className="mb-3"
          >
            <Form.Control
              as="textarea"
              placeholder="Smaller Input"
              size="sm"
              style={{ height: "10px", resize: "none", width: "auto" }} // Adjust the height as needed
            />
          </FloatingLabel>
        </Col>
        <Col xs={8} md={3}>
          <Dropdown>
            <Dropdown.Toggle variant="success" id="dropdown-distribution">
              Distribution
            </Dropdown.Toggle>

            <Dropdown.Menu>
              <Dropdown.Item href="#/action-1">SCIENCE</Dropdown.Item>
              <Dropdown.Item href="#/action-2">HUMANITIES</Dropdown.Item>
              <Dropdown.Item href="#/action-3">SOCIAL_SCIENCE</Dropdown.Item>
              <Dropdown.Item href="#/action-4">NONE</Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        </Col>
        <Col xs={8} md={3}>
          <Dropdown>
            <Dropdown.Toggle variant="success" id="dropdown-basic">
              Program Area
            </Dropdown.Toggle>

            <Dropdown.Menu>
              {items.map((item, index) => (
                <Dropdown.Item key={index} href="#/action-1">
                  {item}
                </Dropdown.Item>
              ))}
              {/* // <Dropdown.Item href="#/action-1">Computer Science</Dropdown.Item>
              // <Dropdown.Item href="#/action-2">Anthropology</Dropdown.Item>
              // <Dropdown.Item href="#/action-3">Something else</Dropdown.Item> */}
            </Dropdown.Menu>
          </Dropdown>
        </Col>
      </Row>
      <br />
      <div class="btn-holder" style={divStyle}>
        <Button variant="primary" onClick={handleButtonClick}>
          Search
        </Button>
        {/* Render the text box conditionally based on the state */}
        {showTextBox && (
          <textarea ref={textAreaRef} value={outputValue} readOnly />
        )}
      </div>
    </>
  );
}

export default CourseSearch;
