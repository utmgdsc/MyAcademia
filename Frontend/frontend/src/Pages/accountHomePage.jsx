import React from "react";
import { Button, Container, Row, ButtonGroup } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "./accountHomePage.css";
function AccountHomePage() {
  return (
    <>
      <Container fluid>
        <Row className="justify-content-start">
          <div className="text-left">
            <Button
              variant="primary"
              href="/account"
              className="mb-2 "
              id="accountbtn"
            >
              Account
            </Button>
            <Button variant="link" href="/" className="mb-2" id="logoutbtn">
              Logout
            </Button>
          </div>
        </Row>
      </Container>
      <div class="text-center">
        <Button variant="secondary" className="me-5" href="/coursesearch">
          Course-Search
        </Button>
        <Button className="me-2" variant="secondary" href="/degree-explorer">
          Degree-Explorer
        </Button>
      </div>
    </>
  );
}
export default AccountHomePage;
