import React from "react";
import PropTypes from "prop-types";

function UserReview({ userName, rating, review}) {
  // These need to be changed to the actual values after getting the data from the backend. Possibly pass this as a prop from the parent component.
  
  return (
    <div class="container text-left"style={{
      textAlign: "left",
    }}>
      <div class="row text-left">
        <div class="col-2 border-primary text-left"><p class="text-left"><strong>{userName}</strong></p></div>
        <div class="col-5 border-primary text-left"><p class="text-left">{review}</p></div>
        <div class="col-2 border-secondary"><p class="text-left">{rating}</p></div>
      </div>
    </div>
  );

  UserReview.propTypes = { userName: PropTypes.string, rating: PropTypes.number, review: PropTypes.string };

}

export default UserReview;
