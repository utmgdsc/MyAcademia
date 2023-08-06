import React from "react";
import "../custom.scss";
function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
      <div className="container-fluid">
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <a
              className="nav-link" href="/"
            >
              Home
            </a>
            <a
              className="nav-link"
              href="/contactInfo/"
            >
              Contact Information
            </a>
            <a className="nav-link" href="/login">
              Login
            </a>
            <a className="nav-link" href="/courseSearch/">
              CourseSearch
            </a>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
