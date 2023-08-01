import React from "react";
import PropTypes from "prop-types";

function AddReviewPage({ course_code }) {
  // These need to be changed to the actual values after getting the data from the backend. Possibly pass this as a prop from the parent component.
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
    <label for="reviewtextarea" class="col-4 col-form-label">Review:</label> 
    <div class="col-8">
      <textarea id="reviewtextarea" name="reviewtextarea" cols="40" rows="5" class="form-control" required="required"></textarea>
    </div>
  </div>
  <div class="form-group row">
    <label class="col-4"></label> 
    <div class="col-8">
      <div class="custom-control custom-checkbox custom-control-inline">
        <input name="anon_checkbox" id="anon_checkbox_0" type="checkbox" class="custom-control-input" value="Yes" aria-describedby="anon_checkboxHelpBlock"/>
        <label for="anon_checkbox_0" class="custom-control-label">Anoymous</label>
      </div> 
      <span id="anon_checkboxHelpBlock" class="form-text text-muted">Select this if you want to remain anonymous in the review. Otherwise, username will be displayed</span>
    </div>
  </div>
  <div class="form-group row">
    <label for="select" class="col-4 col-form-label">Professor</label> 
    <div class="col-8">
      <select id="select" name="select" class="custom-select" required="required" aria-describedby="selectHelpBlock">
        <option value="rabbit">No professor</option>
      </select> 
      <span id="selectHelpBlock" class="form-text text-muted">Select the professor for this review</span>
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
