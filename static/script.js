// Welcome message
console.log("Task Manager Loaded!");

// Confirm before deleting a task
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", (e) => {
            if (!confirm("Are you sure you want to delete this task?")) {
                e.preventDefault();
            }
        });
    });
});