const editButtons = document.getElementsByClassName("btn-edit");
const commentLevel_Value = document.getElementById("id_level");
const commentRating_Value = document.getElementById("id_rating");
const commentPlat_Bool = document.getElementById("id_platinum_achieved");
const commentGame_Version = document.getElementById("id_game_version");
const commentBody = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");


    let commentLevel = document.getElementById(`level${commentId}`).innerText;
    let commentRating = document.getElementById(`rating${commentId}`).innerText;
    let commentGameVersion = document.getElementById(`game_version${commentId}`).innerText;
    let commentText = document.getElementById(`text${commentId}`).innerText;


    commentLevel_Value.value = commentLevel;
    commentRating_Value.value = commentRating;
    commentGame_Version.value = commentGameVersion;
    commentBody.value = commentText;



    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }