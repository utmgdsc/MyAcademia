import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Form, Button, Row } from "react-bootstrap";
function LoginPage() {
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
              <Form.Label>Email or Username</Form.Label>
              <Form.Control type="text" placeholder="Enter email or username" />
            </Form.Group>

            <Form.Group controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Password" />
            </Form.Group>
            <br />

            <Button variant="primary" type="submit" block>
              Log In
            </Button>
          </Form>
          <p className="mt-3 text-center">
            Not a user? <a href="/signup">Register</a>
          </p>
        </div>
      </Container>
    </div>
  );
}

export default LoginPage;
