import React from "react";
import UserReview from "../Components/userreview";
import RedditReview from "../Components/redditreview";
import Navbar from "../Components/navbar";
import "bootstrap/dist/css/bootstrap.min.css";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from "react";
import QuestionTooltip from "../Components/questiontooltip";

// Classes to store relevant data
class UserReviewData {
  constructor(username, review, rating, professor) {
    this.username = username;
    this.rating = rating;
    this.review = review;
    this.professor = professor;
  }
}

class RedditReviewData {
  constructor(review, SAV) {
    this.review = review;
    this.SAV = SAV;
  }
}

class CourseData {
  constructor(
    course_code,
    course_title,
    description,
    distribution,
    pre_req,
    credit,
    recommended_prep,
    program_area,
    exclusions,
    redditReviews,
    userReviews,
    averageRating
  ) {
    this.course_code = course_code;
    this.course_title = course_title;
    this.description = description;
    this.distribution = distribution;
    this.pre_req = pre_req;
    this.redditReviews = redditReviews;
    this.userReviews = userReviews;
    this.averageRating = averageRating;
    this.credit = credit;
    this.recommended_prep = recommended_prep;
    this.program_area = program_area;
    this.exclusions = exclusions;
  }
}

async function getCourseData(course_code) {
  try {
    const courseresponse = await axios.get("/api/courses/" + course_code);
    const redditReviewresponse = await axios.get(
      "/api/getOnlineReviews/?course_code=" + course_code
    );
    const userReviewresponse = await axios.get(
      "/api/getUserReviews/?course_code=" + course_code
    );

    const courseInformation = new CourseData(
      courseresponse.data.course_code,
      courseresponse.data.title,
      courseresponse.data.description,
      courseresponse.data.distribution,
      courseresponse.data.pre_req,
      courseresponse.data.credit,
      courseresponse.data.recommended_prep,
      courseresponse.data.program_area,
      courseresponse.data.exclusions,
      [],
      [],
      courseresponse.data.avg_rating
    );

    // Loop through reddit reviews, extract relevant data as RedditReviewData object and add to array
    const redditreviews = redditReviewresponse.data.map(
      (review) =>
        new RedditReviewData(review.review, review.sentiment_analysis_value)
    );
    courseInformation.redditReviews = redditreviews;

    // Loop through user reviews, extract relevant data as UserReviewData object and add to array
    const userreviews = userReviewresponse.data.map(
      (review) =>
        new UserReviewData(
          review.username,
          review.review,
          review.rating,
          review.Professor
        )
    );
    courseInformation.userReviews = userreviews;
    return courseInformation;
  } catch (error) {
    console.log("Error in getCourseData");
    console.log(error);
  }
}
function CourseInfoPage({ course_code }) {
  //These need to be changed to actual values. The idea is we pass in the course code as a prop then use axios to
  // get the course information from the backend. Then we can use that information to populate the page.
  const [courseData, setCourseData] = useState(null);
  // We need to use async here because we are using await. This is because axios.get is asynchronous and we need to wait for it to finish before we can use the data
  useEffect(() => {
    async function fetchData() {
      try {
        const data = await getCourseData(course_code);
        setCourseData(data);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);
  if (!courseData) {
    return <div>Course doesn't exist</div>;
  } else {
    console.log(courseData);
  }

  const course_title = courseData.course_title;
  const description = courseData.description;
  const distribution = courseData.distribution;
  const pre_req = courseData.pre_req;
  const recommended_prep = courseData.recommended_prep;
  const credit = courseData.credit;
  const averageRating = courseData.averageRating;
  const handleAddReviewClick = () => {
    window.location.href = "/addReview/" + course_code;
  };
  return (
    <div>
      <Navbar />
      <div
        class="container text-left"
        style={{
          textAlign: "left",
        }}
      >
        <div class="row">
          <div class="col-4">
            <h2> Course Code: {course_code}</h2>
          </div>
          <div class="col">
            <h2>Title : {course_title}</h2>
          </div>
        </div>
        <div class="row">
          <div class="col-4">
            <h3> Distribution: {distribution}</h3>
          </div>
        </div>
        <div class="row">
          <div class="col-4">
            <h3> Pre requisites: {pre_req}</h3>
          </div>
          <div class="col-4">
            <h3> Recommended Prep: {recommended_prep}</h3>
          </div>
          <div class="col-4">
            <h3> Credit: {credit}</h3>
          </div>
        </div>
        <div class="row">
          <div class="col-11">
            <nav>
              <div class="nav nav-tabs" id="nav-tab" role="tablist">
                <button
                  class="nav-link active"
                  id="nav-home-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#nav-home"
                  type="button"
                  role="tab"
                  aria-controls="nav-home"
                  aria-selected="true"
                >
                  Description
                </button>
                <button
                  class="nav-link"
                  id="nav-profile-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#nav-profile"
                  type="button"
                  role="tab"
                  aria-controls="nav-profile"
                  aria-selected="false"
                >
                  User Reviews
                </button>
                <button
                  class="nav-link"
                  id="nav-contact-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#nav-contact"
                  type="button"
                  role="tab"
                  aria-controls="nav-contact"
                  aria-selected="false"
                >
                  Online Reviews
                </button>
              </div>
            </nav>
            <div class="tab-content" id="nav-tabContent">
              <div
                class="tab-pane fade show active"
                id="nav-home"
                role="tabpanel"
                aria-labelledby="nav-home-tab"
                tabindex="0"
              >
                <p>{description}</p>
              </div>
              <div
                class="tab-pane fade"
                id="nav-profile"
                role="tabpanel"
                aria-labelledby="nav-profile-tab"
                tabindex="0"
              >
                <div class="row">
                  <div class="col-5">
                    {" "}
                    <h3>Average Course Rating: {averageRating} </h3>
                  </div>
                </div>
                <div class="row text-left">
                  <div class="col-2 border-primary text-left">
                    <p class="text-left">
                      <strong>Username</strong>
                    </p>
                  </div>
                  <div class="col-5 border-primary text-left">
                    <p class="text-left">Review</p>
                  </div>
                  <div class="col-2 border-secondary">
                    <p class="text-left">Professor</p>
                  </div>
                  <div class="col-2 border-secondary">
                    <p class="text-left">Rating</p>
                  </div>
                </div>
                {courseData.userReviews.map((review) => (
                  <UserReview
                    review={review.review}
                    rating={review.rating}
                    professor={review.professor}
                    username={review.username}
                  />
                ))}
                <div class="row">
                  <div class="col-2">
                    <button
                      type="button"
                      class="btn btn-primary"
                      onClick={handleAddReviewClick}
                    >
                      Add Review
                    </button>
                  </div>
                </div>
              </div>
              <div
                class="tab-pane fade"
                id="nav-contact"
                role="tabpanel"
                aria-labelledby="nav-contact-tab"
                tabindex="0"
              >
                <div class="row text-left">
                  <div class="col-8 border-primary text-left">
                    <p class="text-left">Review</p>
                  </div>
                  <div class="col-2 border-secondary">
                    <p class="text-left">
                      SAV <QuestionTooltip text="Sentiment Analysis Value. This is a value between -1 and 1 representing the tone of the review with -1 being negative, 0 being neutral and 1 being positive"/>
                    </p>
                  </div>
                </div>
                {courseData.redditReviews.map((review) => (
                  <RedditReview review={review.review} SAV={review.SAV} />
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default CourseInfoPage;
