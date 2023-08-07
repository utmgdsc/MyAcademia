import React, { useState, useRef, useEffect } from "react";
import {
  FloatingLabel,
  Form,
  Row,
  Col,
  Dropdown,
  Button,
  Container,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
const divStyle = {
  display: "flex",
  justifyContent: "center",
  padding: "50px",
};
const dropdownStyles = {
  maxHeight: "200px", // Set the maximum height here
  overflowY: "auto", // Add a vertical scrollbar when content exceeds the maximum height
};
function CourseSearch() {
  const [items, setItems] = useState([]);
  const [output_list, setOutput_list] = useState([]);

  useEffect(() => {
    // Fetch data from the server using axios
    axios
      .get("/api/getProgramAreas/")
      .then((response) => setItems(response.data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);
  // console.log(items);
  const [showTextBox, setShowTextBox] = useState(false);
  const [outputValue, setOutputValue] = useState(false);
  const textAreaRef = useRef(null);
  const [distribution, setdistribution] = useState("");
  const getDistribution = (event) => {
    const value = event.target.value;
    if (value === "Distribution") {
      setdistribution("");
    } else setdistribution(value);
  };
  const [program, setprogram] = useState("");
  const getProgramArea = (event) => {
    const programArea = event.target.value;
    if (programArea === "Program Area") {
      setprogram("");
    } else setprogram(programArea);
  };
  const [showForm, setShowForm] = useState(false);
  const formRef = useRef();

  const handleOutsideClick = (event) => {
    // Check if the clicked element is inside the form.
    if (formRef.current && !formRef.current.contains(event.target)) {
      setShowForm(false);
    }
  };

  useEffect(() => {
    const handleClickOutside = (event) => {
      // Check if the clicked element is inside the form.
      if (formRef.current && !formRef.current.contains(event.target)) {
        setShowForm(false);
      }
    };

    // Add event listener to detect clicks outside the form when the form is visible.
    if (showForm) {
      document.addEventListener("mousedown", handleClickOutside);
    }

    return () => {
      // Clean up by removing the event listener when the component is unmounted.
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [showForm]);
  let generatedOutput = [];
  const handleButtonClick = () => {
    setShowForm(true);
    const course_input = document.getElementById("course_code-textarea").value;
    const course_prereq = document.getElementById(
      "pre-requisites-textarea"
    ).value;
    const postdata = {
      course_code: course_input,
      pre_req: course_prereq,
      distribution: distribution,
      program_area: program,
    };
    console.log(postdata);
    axios
      .post("/api/courseSearch/", postdata)
      .then((response) => {
        // console.log(response);
        setOutput_list(response.data);
        console.log(response.data);
      })
      .catch((error) => console.error("Error fetching data:", error));
    generatedOutput = output_list;
    setShowTextBox(true);
    setOutputValue(generatedOutput);
  };
  //For navigating to course info page for the selected course
  const ResultChange = (event) => {
    event.preventDefault();
    setShowForm(false);
    const selectedValue = event.target.value;
    // If the selected value is not "Results", navigate to the selected URL
    window.location.href = `http://localhost:3000/courseInfo/${selectedValue}`;
  };
  //For removing the form after the search button is clicked

  return (
    <>
      <div
        style={{
          backgroundImage: `url(${require("../images/course_search_background.jpeg")})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          backgroundRepeat: "no-repeat",
          height: "100vh",
          width: "100vw",
          display: "flex",
          flexDirection: "column", // Set the flex direction to column
          alignItems: "center", // Center items horizontally
          justifyContent: "center", // Center items vertically
        }}
      >
        <Container fluid>
          <Row className="accounthp-justify-content-start">
            <div className="accounthp-text-left">
              <Button
                variant="primary"
                href="/"
                className="mb-2 "
                id="accountbtn"
              >
                Home
              </Button>
              <Button
                variant="secondary"
                href="/accountHomePage/"
                className="mb-2"
                id="logoutbtn"
              >
                Account Home Page
              </Button>
            </div>
          </Row>
        </Container>
        <h2 style={{ color: "white" }}>Course Search</h2>
        <br></br>
        <br></br>
        <br></br>
        <br></br>

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
            <p style={{ fontWeight: "bold" }}>
              Please enter the course code above
            </p>
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
            <p style={{ fontWeight: "bold" }}>
              Please enter the Pre-requisite above
            </p>
          </Col>
          <Col xs={8} md={3}>
            <Form.Select
              aria-label="Distribution-form"
              onChange={getDistribution}
              value={distribution}
            >
              <option>Distribution</option>
              <option value="Science">SCIENCE</option> 
              <option value="Humanities">HUMANITIES</option>
              <option value="Social Science">SOCIAL_SCIENCE</option>
              <option value="None">NONE</option>
            </Form.Select>
            <p style={{ fontWeight: "bold" }}>
              Selected distribution:{distribution}
            </p>
          </Col>
          <Col xs={8} md={3}>
            <Form.Select
              aria-label="program-form"
              onChange={getProgramArea}
              value={program}
            >
              <option>Program Area</option>
              {items.slice(1).map((item, index) => (
                <option value={item}>{item}</option>
              ))}
            </Form.Select>
            <p style={{ fontWeight: "bold" }}>Selected program:{program}</p>
          </Col>
        </Row>
        <br />
        <div class="btn-holder" style={divStyle}>
          <Button variant="primary" onClick={handleButtonClick}>
            Search
          </Button>
          {/* Render the text box conditionally based on the state */}
          {showForm && (
            <div>
              {/* <textarea ref={textAreaRef} value={outputValue} readOnly /> */}
              <Form.Select
                aria-label="Result-form"
                onChange={ResultChange}
                ref={formRef}
                // value={program}
              >
                <option>Results</option>
                {output_list.map((course) => (
                  <option value={course.course_code}>
                    {course.course_code}:{course.title}
                  </option>
                ))}
              </Form.Select>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default CourseSearch;
