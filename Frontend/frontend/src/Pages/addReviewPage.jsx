import React, { useEffect } from "react";
import PropTypes from "prop-types";
import { useState } from "react";
function submitButonClicked(){

}

function AddReviewPage({ course_code }) {
  // These need to be changed to the actual values after getting the data from the backend. Possibly pass this as a prop from the parent component.
  const [courseProfessors, setcourseProfessors] = useState(null);
  const [allProfessors, setallProfessors] = useState(null);

  
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
    <label for="reviewtextarea" class="col-4 col-form-label">Review</label> 
    <div class="col-8">
      <textarea id="reviewtextarea" name="reviewtextarea" cols="40" rows="2" class="form-control" aria-describedby="reviewtextareaHelpBlock"></textarea> 
      <span id="reviewtextareaHelpBlock" class="form-text text-muted">Enter your review here</span>
    </div>
  </div>
  <div class="form-group row">
    <div class="col-4"></div> 
    <div class="col-8">
      <div class="custom-control custom-checkbox custom-control-inline">
        <input name="anon_checkbox" id="anon_checkbox_0" type="checkbox" class="custom-control-input" value="fish"/> 
        <label for="anon_checkbox_0" class="custom-control-label">Anonymous</label>
      </div>
    </div>
  </div>
  <div class="form-group row">
    <label for="professor_select" class="col-4 col-form-label">Professor</label> 
    <div class="col-8">
      <select id="professor_select" name="professor_select" class="custom-select">
        <option value="No professor">No Professor</option>
      </select>
    </div>
  </div>
  <div class="form-group row">
    <label for="text" class="col-4 col-form-label">Rating</label> 
    <div class="col-8">
      <input id="text" name="text" type="text" class="form-control" aria-describedby="textHelpBlock"/> 
      <span id="textHelpBlock" class="form-text text-muted">Out of 5</span>
    </div>
  </div> 
  <div class="form-group row">
    <div class="offset-4 col-8">
      <button name="submit" type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</form>
    </>
  );

  AddReviewPage.propTypes = { courseCode: PropTypes.string };
}

export default AddReviewPage;
