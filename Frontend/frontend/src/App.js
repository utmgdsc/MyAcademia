import AccountHomePage from './Pages/accountHomePage';
import CourseSearch from './Pages/courseSearch';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootstrap/dist/js/bootstrap.bundle.min";
import RedditReview from "./Components/redditreview";
import UserReview from "./Components/userreview";
import CourseInfoPage from "./Pages/courseInfoPage";
import AddReviewPage from "./Pages/addReviewPage";
import WelcomePage from "./Pages/welcomePage";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Routes,
} from "react-router-dom";
import { useRef } from "react";

function App() {
  const url = window.location.href; // http:myacademia.com/courseInfo/CSC108H5
  const course_code = url.split("/")[2];
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<WelcomePage />} />
          <Route path="/courseInfo/" element={<CourseInfoPage course_code={"CSC108H5"} />} />
          <Route path="/addReview/" element={<AddReviewPage/>} />
          <Route path="/accountHome/" element={<AccountHomePage/>} />
          <Route path="/courseSearch/" element={<CourseSearch/>} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;