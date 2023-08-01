import React, { useState } from "react";
import Navbar from "../Components/navbar";
import "../custom.scss";
function WelcomePage() {
  const [activeTab, setActiveTab] = useState("Home");

  const handleTabChange = (tabName) => {
    setActiveTab(tabName);
  };

  const aboutus =
    "MyAcademia is a website that allows students to refine their course enrollement process. ";
  const contactus = "Contact us at +1 234 567 8901 or at utmgdsc392@gmail.com";

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
      <Navbar activeTab={activeTab} onTabChange={handleTabChange} />
      <h1>Welcome to MyAcademia</h1>
      <div className="container">
        <h2 id="pageTitle">
          {activeTab === "Home" ? "About Us" : "Contact Information"}
        </h2>
        <p id="pageText">{activeTab === "Home" ? aboutus : contactus}</p>
      </div>
    </div>
  );
}

export default WelcomePage;
