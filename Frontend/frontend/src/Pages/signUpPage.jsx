import React, { useState, useRef, useEffect } from "react";
import { Container, Form, Button, Row } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import Navbar from "../Components/navbar";
import axios from "axios";
const SignupPage = () => {
  const usernameRef = useRef();
  const emailRef = useRef();
  const passwordRef = useRef();
  const firstNameRef = useRef();
  const lastNameRef = useRef();
  const [payload, setpayload] = useState({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
  });
  const handleSignupClick = (e) => {
    e.preventDefault();
    const username = usernameRef.current.value;
    const email = emailRef.current.value;
    const password = passwordRef.current.value;
    const first_name = firstNameRef.current.value;
    const last_name = lastNameRef.current.value;
    const payload = {
      first_name: first_name,
      last_name: last_name,
      username: username,
      email: email,
      password: password,
    };
    setpayload(payload);
    // console.log(payload);
    console.log(payload);

    axios
      .post("/auth/users/", payload)
      .then((response) => {
        if (response.status === 201) {
          window.location.href = "/login";
        } else {
          alert(response.data);
        }
      })
      .catch((error) => {
        console.log(error.response);
        alert(Object.values(error.response.data).toString());
      });
  };

  return (
    <>
      <Navbar />
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
            <h2 className="text-center mb-4">Sign Up MyAcademia</h2>

            <Form onSubmit={handleSignupClick}>
              <Form.Group controlId="formBasicUsername">
                <Form.Label>First Name</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Enter First Name"
                  ref={firstNameRef}
                />
              </Form.Group>
              <br />
              <br />
              <Form.Group controlId="formBasicUsername">
                <Form.Label>Last Name</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Enter last Name"
                  ref={lastNameRef}
                />
              </Form.Group>
              <br />
              <br />
              <Form.Group controlId="formBasicUsername">
                <Form.Label>UserName</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Enter username"
                  ref={usernameRef}
                />
              </Form.Group>
              <br />
              <br />

              <Form.Group controlId="formBasicEmail">
                <Form.Label>Email</Form.Label>
                <Form.Control
                  type="email"
                  placeholder="Enter email"
                  ref={emailRef}
                />
              </Form.Group>
              <br />
              <br />
              <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Password"
                  ref={passwordRef}
                />
              </Form.Group>
              <br />
              <br />
              <Button
                variant="primary"
                type="submit"
                block
                onClick={handleSignupClick}
              >
                Sign Up
              </Button>
            </Form>
          </div>
        </Container>
      </div>
    </>
  );
};

export default SignupPage;
