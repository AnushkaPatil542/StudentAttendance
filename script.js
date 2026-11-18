
let students = ["Rahul", "Priya", "Amit"];
let attendance = {};

function updateStudents() {
    let dropdown = document.getElementById("student");

    dropdown.innerHTML = "";

    students.forEach(name => {
        let option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        dropdown.appendChild(option);
    });

    document.getElementById("total").innerText =
        students.length;
}

function addStudent() {
    let name = document.getElementById("studentName").value.trim();

    if (name === "") {
        alert("Enter Student name");
        return;
    }

    if (students.includes(name)) {
        alert("Student already exists");
        return;
    }

    students.push(name);

    document.getElementById("studentName").value = "";

    updateStudents();
}

function markAttendance() {
    let name = document.getElementById("student").value;
    let status = document.getElementById("status").value;

    attendance[name] = status;

    displayAttendance();
}

function displayAttendance() {
    let records = document.getElementById("records");

    records.innerHTML = "";

    let present = 0;
    let absent = 0;

    students.forEach(name => {
        let status = attendance[name] || "Not Marked";

        if (status === "Present") present++;
        if (status === "Absent") absent++;

        records.innerHTML += `
            <tr>
                <td>${name}</td>
                <td>${status}</td>
            </tr>
        `;
    });

    document.getElementById("present").innerText = present;
    document.getElementById("absent").innerText = absent;
}

updateStudents();
displayAttendance();
