import React, { useState } from "react";
import Navbar from "../Components/navbar";
import "../custom.scss";
function WelcomePage({activeTab}) {
  const aboutus =
    "MyAcademia is a website that allows students to refine their course enrollement process.   We provide a platform for UTM students to share their experiences with courses they have taken as well as rate their professors. Our Course Search Component helps you filter out courses based on your preferences and then redirects you to our Course Info Page where the user can see the  basic information about the course along with a feature to view 10 online reddit review of that course and also add their own review for other students to see. Our Degree Explorer Component will help the user generate a degree plan based on specific inputs given by the user like courses taken, credits etc and will generate the user a list of courses (basically a plan) for the credits they chose. ";
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
