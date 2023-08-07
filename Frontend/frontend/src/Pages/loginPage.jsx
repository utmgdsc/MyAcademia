import React, { useState, useRef, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
import { Container, Form, Button, Row } from "react-bootstrap";
function LoginPage() {
  const usernamelog = useRef();
  const passwordlog = useRef();
  const [payload, setpayload] = useState({
    username: "",
    password: "",
  });
  const [loginStatus, setloginStatus] = useState("");
  const handleLoginClick = (e) => {
    e.preventDefault();
    const username = usernamelog.current.value;
    const password = passwordlog.current.value;
    const payload = {
      username: username,
      password: password,
    };
    setpayload(payload);
    // console.log(payload);
    //Sending a post request to database with credentials expecting a response
    axios.post("/auth/token/login/",payload).then((response) => {
      if (response.data.auth_token) {
        console.log("Getting token")
        console.log(response.data.auth_token);
        localStorage.setItem("usertoken", JSON.stringify(response.data));
        console.log("Retrieving token form local storage");
        console.log(localStorage.getItem("usertoken"));
      }
      if (response.data.message) {
        setloginStatus(response.data.message);
      }
    }).catch((error) => {
      console.log(error);
      alert("Invalid Credentials");
    });
  };

  return (
    <div>
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
          </div>
        </Row>
      </Container>
      <Container
        className="d-flex align-items-center justify-content-center"
        style={{ minHeight: "100vh" }}
      >
        <div className="w-100" style={{ maxWidth: "400px" }}>
          <h2 className="text-center mb-4">Login</h2>
          <Form>
            <Form.Group controlId="formBasicEmail">
              <Form.Label> Username</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter email or username"
                ref={usernamelog}
              />
            </Form.Group>

            <Form.Group controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Password"
                ref={passwordlog}
              />
            </Form.Group>
            <br />

            <Button
              variant="primary"
              type="submit"
              block
              onClick={handleLoginClick}
            >
              Log In
            </Button>
          </Form>
          <p className="mt-3 text-center">
            Not a user? <a href="/signup">Register</a>
          </p>
          <h2>{loginStatus}</h2>
        </div>
      </Container>
    </div>
  );
}

export default LoginPage;
