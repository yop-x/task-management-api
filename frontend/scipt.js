const API_URL = "https://task-management-api-dutb.onrender.com/";

const taskList = document.getElementById("task-list");
const form = document.getElementById("task-form");

const title = document.getElementById("title");
const description = document.getElementById("description");
const status = document.getElementById("status");
const priority = document.getElementById("priority");
// Fetch and display tasks
async function loadTasks() {
  taskList.innerHTML = "Loading...";

  const res = await fetch(`${API_URL}/tasks`);
  const tasks = await res.json();

  taskList.innerHTML = "";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.className = task.status;

    li.innerHTML = `
      <span>
        <strong>${task.title}</strong> — ${task.description}
      </span>
      <button onclick="markDone('${task.id}')">Mark done</button>
    `;

    taskList.appendChild(li);
  });
}

// Create task
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const task = {
    title: title.value,
    description: description.value,
    status: status.value,
    priority: priority.value
  };

  await fetch(`${API_URL}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task)
  });

  form.reset();
  loadTasks();
});

// Mark task as done
async function markDone(id) {
  await fetch(`${API_URL}/tasks/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: "done" })
  });

  loadTasks();
}

// Initial load
loadTasks();
