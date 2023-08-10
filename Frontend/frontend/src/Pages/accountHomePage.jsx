import React from "react";
import { Button, Container, Row, ButtonGroup, Nav } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "./accountHomePage.css";
import Navbar from "../Components/navbar";
import axios from "axios";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

async function handleLogout(){
  const tokenObject = JSON.parse(sessionStorage.getItem("usertoken"));
  const token = tokenObject["auth_token"].toString();
  const config = {
    headers: {
      "Content-Type": "application/json",
      Authorization: "Token " + token, 
    },
  };
  await axios.post("/auth/token/logout/", {}, config);
  sessionStorage.removeItem("usertoken");
  sessionStorage.setItem("activeUser", "false");
  window.location.href = "/";
}

function AccountHomePage() {
  const navigate = useNavigate();
  useEffect(() => {
    // Check if the user is logged in and redirect to login page if not
    const activeUser = sessionStorage.getItem("activeUser");
    console.log(activeUser);
    if (activeUser === "false" || activeUser === null) {
      navigate("/login");
    }
  }, []);
  return (
    <>
    <Navbar />
      <Container fluid>
        <Row className="accounthp-justify-content-start">
          <div className="accounthp-text-left">
            <Button
              variant="primary"
              href="/account"
              className="mb-2 "
              id="accountbtn"
            >
              Account
            </Button>
            <Button variant="link" className="mb-2" id="logoutbtn" onClick={handleLogout}>
              Logout
            </Button>
          </div>
        </Row>
      </Container>
      <div class="accounthp-text-center">
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
