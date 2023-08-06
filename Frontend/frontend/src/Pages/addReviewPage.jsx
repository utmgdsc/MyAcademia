import React, { useEffect } from "react";
import PropTypes from "prop-types";
import { useState } from "react";
import axios from "axios";
function submitButonClicked() {}

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

async function getAllProfData() {
  try {
    const dataresponse = await axios.get("/api/allProfessors/");
    console.log(dataresponse.data);
    return dataresponse.data;
  } catch (error) {
    console.log(error);
  }
}

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
function handleSubmit() {
  //Get the values from the form and make a post request to the backend
  const review = document.getElementById("reviewtextarea").value;
  const anon = document.getElementById("anon_checkbox_0").value;
  const professor = document.getElementById("select").value;
  console.log(review);
  console.log(anon);
  console.log(professor);
}

function AddReviewPage({ course_code }) {
  const [courseProfessors, setcourseProfessors] = useState(null);
  const [allProfessors, setallProfessors] = useState(null);
  const [courseData, setCourseData] = useState(null);
  const ratings = [1, 2, 3, 4, 5];

  //Fetching the data from the backend
  useEffect(() => {
    async function fetchData() {
      try {
        const coursedata = await getcourseData(course_code);
        setCourseData(coursedata);
        if (courseData === null) {
          return;
        }
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
            <h1>Course Code: {course_code} </h1>
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
          <label class="col-4"></label>
          <div class="col-8">
            <div class="custom-control custom-checkbox custom-control-inline">
              <input
                name="anon_checkbox"
                id="anon_checkbox_0"
                type="checkbox"
                class="custom-control-input"
                value="Yes"
                aria-describedby="anon_checkboxHelpBlock"
              />
              <label for="anon_checkbox_0" class="custom-control-label">
                Anonymous
              </label>
            </div>
            <span id="anon_checkboxHelpBlock" class="form-text text-muted">
              Select this if you want to remain anonymous in the review.
              Otherwise, username will be displayed
            </span>
          </div>
        </div>
        <div class="form-group row">
          <label for="select" class="col-4 col-form-label">
            Professor
          </label>
          <div class="col-8">
            <select
              id="selectProfessor"
              name="selectProfessor"
              class="custom-select"
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
              class="custom-select"
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
