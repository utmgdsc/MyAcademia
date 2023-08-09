import React, { useEffect } from "react";
import PropTypes from "prop-types";
import { useState } from "react";
import axios from "axios";
import {useNavigate} from "react-router-dom";
// Get professors who have taught the course before
async function getCourseProfData(course_code) {
  try {
    const dataresponse = await axios.get(
      "/api/findProfessor/?course_code=" + course_code
    );
    console.log(dataresponse.data);
    return dataresponse.data;
  } catch (error) {
    console.log(error);
  }
}
// Get all professors from the database
async function getAllProfData() {
  try {
    const dataresponse = await axios.get("/api/allProfessors/");
    console.log(dataresponse.data);
    return dataresponse.data;
  } catch (error) {
    console.log(error);
  }
}
//Get the course data from the backend. This is used for validation
async function getcourseData(course_code) {
  try {
    const courseresponse = await axios.get("/api/courses/" + course_code);
    console.log(courseresponse.data);
    return courseresponse.data;
  } catch (error) {
    console.log(error);
    console.log("Error caught and returning null");
    return null;
  }
}
// Function to handle the submit button
async function handleSubmit() {
  //Get the values from the form and make a post request to the backend
  const review = document.getElementById("reviewtextarea").value;
  const anon = document.getElementById("anon_select").value;
  const rating = document.getElementById("selectRating").value;
  const professor_name = document.getElementById("selectProfessor").value;
  const course_code = document
    .getElementById("course_code")
    .innerHTML.split(" ")[2];
  const tokenObject = JSON.parse(sessionStorage.getItem("usertoken"));
  const token = tokenObject["auth_token"].toString();
  console.log(course_code);
  console.log(token);

  const config = {
    headers: {
      "Content-Type": "application/json",
      Authorization: "Token " +  token  // Replace with actual user token
    },
  };
  console.log(config);
  const postdata = {
    review: review,
    anonymous: anon,
    rating: rating,
    professor_name: professor_name,
    course_code: course_code,
  };
  const response = await axios.post("/api/createUserReview/", postdata, config);
  console.log("Response from backend");
  console.log(response);
  console.log(response.status);
  if (response.status == 201) {
    window.location.href = "/courseInfo/" + course_code;
  } else {
    alert(response.data);
  }
}

function AddReviewPage({ course_code }) {
  const [courseProfessors, setcourseProfessors] = useState(null);
  const [allProfessors, setallProfessors] = useState(null);
  const [courseData, setCourseData] = useState(null);
  const ratings = [1, 2, 3, 4, 5];
  const navigate = useNavigate();

  
  useEffect(() => {
    // Check if the user is logged in and redirect to login page if not
    const activeUser = sessionStorage.getItem("activeUser");
    console.log(activeUser)
    if(activeUser === "false" || activeUser === null){
      sessionStorage.setItem("fromaddreview", "true");
      sessionStorage.setItem("course_code", course_code)
      navigate("/login");
    }
    //Fetching the data from the backend
    async function fetchData() {
      try {
        const coursedata = await getcourseData(course_code);
        setCourseData(coursedata);
        const courseprofdata = await getCourseProfData(course_code);
        setcourseProfessors(courseprofdata);
        const allprofdata = await getAllProfData();
        setallProfessors(allprofdata);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);
  // If the course does not exist, then display an error message
  if (courseData == null) {
    return <h1>Page does not exist</h1>;
  }
  // Render the page with the information
  return (
    <>
      <div
        class="container text-left"
        style={{
          textAlign: "left",
        }}
      >
        <div class="row">
          <div class="col-8 border-primary">
            <h1 id="course_code">Course Code: {course_code} </h1>
          </div>
        </div>
      </div>
      <form>
        <div class="form-group row">
          <label for="reviewtextarea" class="col-4 col-form-label">
            Review:
          </label>
          <div class="col-8">
            <textarea
              id="reviewtextarea"
              name="reviewtextarea"
              cols="40"
              rows="5"
              class="form-control"
              required="required"
            ></textarea>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-4">Anonymous</label>
          <div class="col-2">
            <select
              class="form-select"
              aria-label="AnonSelect"
              id="anon_select"
            >
              <option selected value="false">
                No
              </option>
              <option value="true">Yes</option>
            </select>
            <span id="anon_checkboxHelpBlock" class="form-text text-muted">
              Select Yes if you want to be anonymous
            </span>
          </div>
        </div>
        <div class="form-group row">
          <label for="selectProfessor" class="col-4 col-form-label">
            Professor
          </label>
          <div class="col-2">
            <select
              id="selectProfessor"
              name="selectProfessor"
              class="form-select"
              required="required"
              aria-describedby="selectHelpBlock"
            >
              <option value="No Professor">No professor</option>
              {courseProfessors && // This is conditional rendering. If the value of courseProfessors is null, then the following code will not be executed. This is to prevent the code from crashing if the data is not fetched from the backend yet.
                courseProfessors.map((prof) => (
                  <option value={prof}>{prof}</option>
                ))}
              <option disabled="disabled"> --- </option>
              {allProfessors && // This is conditional rendering. If the value of courseProfessors is null, then the following code will not be executed. This is to prevent the code from crashing if the data is not fetched from the backend yet.
                allProfessors.map((prof) => (
                  <option value={prof}>{prof}</option>
                ))}
            </select>
            <span id="selectHelpBlock" class="form-text text-muted">
              Select the professor for this review
            </span>
          </div>
        </div>
        <div class="form-group row">
          <label for="reviewtextarea" class="col-4 col-form-label">
            Rating
          </label>
          <div class="col-1">
            <select
              id="selectRating"
              name="selectRating"
              class="form-select"
              required="required"
              aria-describedby="selectHelpBlock"
            >
              {ratings.map((rating) => (
                <option value={rating}>{rating}</option>
              ))}
            </select>
          </div>
        </div>
        <div class="form-group row">
          <div class="offset-4 col-8">
            <button
              name="submit"
              type="button"
              class="btn btn-primary"
              onClick={handleSubmit}
            >
              Submit
            </button>
          </div>
        </div>
      </form>
    </>
  );

  AddReviewPage.propTypes = { courseCode: PropTypes.string };
}

export default AddReviewPage;
