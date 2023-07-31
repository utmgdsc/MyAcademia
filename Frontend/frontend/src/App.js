
import AccountHomePage from './Pages/accountHomePage';
import CourseSearch from './Pages/courseSearch';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
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
      <CourseSearch />
    </div>
  );
}

export default App;