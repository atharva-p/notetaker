function deleteNote(noteId) {
    // make a fetch request to the delete-note endpoint, and after the request is made redirect to the home view
    fetch("/delete-note", {
        method: "POST", 
        body: JSON.stringify({ noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/"; 
    }); 
}