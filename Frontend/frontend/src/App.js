
import React from "react";
import WelcomePage from "./Pages/welcomePage";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import AccountHomePage from './Pages/accountHomePage';
import CourseSearch from './Pages/courseSearch';
import "bootstrap/dist/js/bootstrap.bundle.min";
import RedditReview from "./Components/redditreview";
import UserReview from "./Components/userreview";
import CourseInfoPage from "./Pages/courseInfoPage";
import AddReviewPage from "./Pages/addReviewPage";
//import AccountHomePage from "./Pages/accountHomePage";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Routes,
} from "react-router-dom";
import { createContext, useContext, useState } from "react";


function App() {
  const url = window.location.href; // http:myacademia.com/courseInfo/CSC108H5
  const course_code = url.split("/")[4];
  return (
    <div className="App">
      {<Router>
        <Routes>
          <Route path="/" element={<WelcomePage />} />
          <Route path="/courseInfo/:course_code" element={<CourseInfoPage course_code={course_code} />} />
          <Route path="/addReview/:course_code" element={<AddReviewPage course_code={course_code}/>} />
          <Route path="/courseSearch/" element={<CourseSearch />} />
          <Route path="/accountHomePage/" element={<AccountHomePage />} />
        </Routes>
      </Router> }
    </div>
  );
}

export default App;
