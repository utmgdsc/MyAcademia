import React from "react";
import "../custom.scss";
import axios from "axios";
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
  sessionStorage.removeItem("activeUser", "false");
  window.location.href = "/";
}
function Navbar() {
  const activeUser = sessionStorage.getItem("activeUser");
  return (
    <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
      <div className="container-fluid">
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <a className="nav-link" href="/">
              Home
            </a>
            <a className="nav-link" href="/contactInfo/">
              Contact Information
            </a>
            {activeUser === "true" ? (
              <a className="nav-link" onClick={handleLogout}>
                {" "}
                Logout{" "}
              </a>
            ) : (
              <a className="nav-link" href="/login/">
                {" "}
                Login{" "}
              </a>
            )}
            <a className="nav-link" href="/courseSearch/">
              CourseSearch
            </a>
            <a className="nav-link" href="/degreeExplorer/">
              Degree Explorer
            </a>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
