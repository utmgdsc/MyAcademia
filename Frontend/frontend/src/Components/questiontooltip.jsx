import React from "react";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
// Will create a question mark tooltip that will appear when hovered over
function QuestionTooltip({ text }) {
  const renderTooltip = (props) => (
    <Tooltip id="tooltip" {...props}>
      {text}
    </Tooltip>
  );

  return (
    <>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <OverlayTrigger
      placement="top"
      delay={{ show: 250, hide: 400 }}
      overlay={renderTooltip}
    >
      <span class="material-symbols-outlined">help</span>
    </OverlayTrigger>
  </>
  );
}

export default QuestionTooltip;