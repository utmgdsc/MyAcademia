import React from "react";
import PropTypes from "prop-types";

function RedditReview({ review, SAV }) {
  // These need to be changed to the actual values after getting the data from the backend. Possibly pass this as a prop from the parent component.
  return (
    <div class="container text-left"style={{
      textAlign: "left",
    }}>
      <div class="row">
        <div class="col-8 border-primary"><p class="text-left">{review}</p></div>
        <div class="col border-secondary"><p class = "text-left">{SAV}</p></div>
      </div>
    </div>
  );

  RedditReview.propTypes = { review: PropTypes.string, SAV: PropTypes.number };
}

export default RedditReview;
