import React from "react";
import "../custom.scss";
function Navbar({ activeTab, onTabChange }) {
  return (
    <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
      <div className="container-fluid">
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <a
              className={`nav-link ${activeTab === "Home" ? "active" : ""}`}
              onClick={() => onTabChange("Home")}
            >
              Home
            </a>
            <a
              className={`nav-link ${activeTab === "Contact" ? "active" : ""}`}
              onClick={() => onTabChange("Contact")}
            >
              Contact Information
            </a>
            <a className="nav-link" href="/login">
              Login
            </a>
            <a className="nav-link" href="/courseInfo/CSC108H5">
              CourseSearch
            </a>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
