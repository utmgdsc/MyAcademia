import React from "react";
import WelcomePage from "./Pages/welcomepage";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import RedditReview from "./Components/redditreview";
import UserReview from "./Components/userreview";
import CourseInfoPage from "./Pages/courseInfoPage";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Routes,
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<WelcomePage />} />
          <Route path="/courseInfo" element={<CourseInfoPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
