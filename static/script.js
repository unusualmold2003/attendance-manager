async function submitAttendance() {
  const subject = document.getElementById("subject").value.trim();
  const attended = parseInt(document.getElementById("attended").value);
  const total = parseInt(document.getElementById("total").value);

  if (!subject || isNaN(attended) || isNaN(total) || attended > total) {
    alert("Please enter valid details.");
    return;
  }

  const res = await fetch("/api/attendance", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ subject, attended, total }),
  });

  const data = await res.json();
  alert(data.message);
}

async function fetchSummary() {
  const res = await fetch("/api/summary");
  const data = await res.json();

  const summary = document.getElementById("summary");
  if (data.length === 0) {
    summary.innerHTML = "<p class='text-gray-600'>No attendance records found.</p>";
    return;
  }

  summary.innerHTML = data
    .map(
      (item) => `
    <div class="p-4 border border-gray-200 rounded-md bg-gray-50 shadow-sm">
      <h3 class="text-lg font-semibold text-blue-700">${item.subject}</h3>
      <p>Attended: <span class="font-medium">${item.attended}</span> / <span class="font-medium">${item.total}</span></p>
      <p>Percentage: <span class="font-medium">${item.percentage}%</span></p>
      <p>Additional Classes Needed: <span class="font-medium">${item.additional_needed}</span></p>
    </div>
  `
    )
    .join("");
}
