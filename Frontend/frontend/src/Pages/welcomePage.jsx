import React, { useState } from "react";
import Navbar from "../Components/navbar";
import "../custom.scss";
function WelcomePage({activeTab}) {
  const aboutus =
    "MyAcademia is a website that allows students to refine their course enrollement process. ";
  const contactus = "Contact us at +1 234 567 8901 or at utmgdsc392@gmail.com";
  let home = false;
  if (activeTab === "Home") {
    home = true;  
  }


  return (
    <div
      style={{
        backgroundImage: `url(${require("../images/homepage_background.jpeg")})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        height: "100vh",
        width: "100vw",
      }}
    >
      <Navbar />
      <h1>Welcome to MyAcademia</h1>
      <div className="container">
        <h2 id="pageTitle">
          { home ? "About Us" : "Contact Information"}
        </h2>
        <p id="pageText">{home ? aboutus : contactus}</p>
      </div>
    </div>
  );
}

export default WelcomePage;
